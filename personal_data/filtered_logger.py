#!/usr/bin/env python3
"""
Filtered Logger Module

This module provides functionality to obfuscate personally identifiable
information (PII) in log messages using regular expressions.
"""

import re
import logging
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """
    Obfuscate specified fields in a log message.

    Args:
        fields: List of field names to obfuscate
        redaction: String to replace field values with
        message: The log message containing field-value pairs
        separator: Character that separates fields in the message

    Returns:
        The log message with specified fields obfuscated
    """
    pattern = '|'.join(
        f'{field}=[^{separator}]*' for field in fields
    )
    return re.sub(
        pattern,
        lambda m: m.group().split('=')[0] + '=' + redaction,
        message
    )


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """
        Initialize RedactingFormatter with fields to redact.

        Args:
            fields: List of field names to redact in log messages
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Format the specified record with PII redaction.

        Args:
            record: LogRecord to format

        Returns:
            Formatted log record with specified fields redacted
        """
        record.msg = filter_datum(self.fields, self.REDACTION,
                                  record.getMessage(), self.SEPARATOR)
        return super().format(record)


# Test the function and class
if __name__ == "__main__":
    # Test filter_datum
    fields = ["password", "date_of_birth"]
    messages = [
        "name=egg;email=eggmin@eggsample.com;password=eggcellent;"
        "date_of_birth=12/12/1986;",
        "name=bob;email=bob@dylan.com;password=bobbycool;"
        "date_of_birth=03/04/1993;"
    ]

    print("Testing filter_datum:")
    for message in messages:
        print(filter_datum(fields, 'xxx', message, ';'))

    print("\nTesting RedactingFormatter:")
    # Test RedactingFormatter
    message = ("name=Bob;email=bob@dylan.com;ssn=000-123-0000;"
               "password=bobby2019;")
    log_record = logging.LogRecord("my_logger", logging.INFO, None, None,
                                   message, None, None)
    formatter = RedactingFormatter(fields=("email", "ssn", "password"))
    print(formatter.format(log_record))
