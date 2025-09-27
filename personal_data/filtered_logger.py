#!/usr/bin/env python3
"""
Filtered Logger Module

This module provides functionality to obfuscate personally identifiable
information (PII) in log messages using regular expressions.
"""

import re
import logging
from typing import List


# PII fields constant - these are the important fields to redact
PII_FIELDS = ("name", "email", "phone", "ssn", "password")


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


def get_logger() -> logging.Logger:
    """
    Create and configure a logger for user data.

    Returns:
        Configured logging.Logger object
    """
    # Create logger named "user_data"
    logger = logging.getLogger("user_data")

    # Set logging level to INFO
    logger.setLevel(logging.INFO)

    # Prevent propagation to other loggers
    logger.propagate = False

    # Create StreamHandler
    handler = logging.StreamHandler()

    # Set formatter to RedactingFormatter with PII_FIELDS
    formatter = RedactingFormatter(fields=PII_FIELDS)
    handler.setFormatter(formatter)

    # Add handler to logger
    logger.addHandler(handler)

    return logger


# Test the function and class
if __name__ == "__main__":
    # Test get_logger function
    logger = get_logger()

    # Test the logger with a sample message containing PII
    test_message = ("""name=John Doe;email=john.doe@example.com;phone=123-456-7890;
                   ssn=123-45-6789;password=secret123;age=30;city=New York""")

    logger.info(test_message)

    # Test annotations as required by the main.py example
    print("Logger class:", get_logger.__annotations__.get('return'))
    print("PII_FIELDS: {}".format(len(PII_FIELDS)))
