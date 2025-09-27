#!/usr/bin/env python3
"""
Filtered Logger Module

This module provides functionality to obfuscate personally identifiable information (PII)
in log messages using regular expressions.
"""

import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
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
    pattern = '|'.join(f'{field}=[^{separator}]*' for field in fields)
    return re.sub(pattern, lambda m: m.group().split('=')[0] + '=' + redaction, message)


# Test the function
if __name__ == "__main__":
    fields = ["password", "date_of_birth"]
    messages = [
        "name=egg;email=eggmin@eggsample.com;password=eggcellent;date_of_birth=12/12/1986;",
        "name=bob;email=bob@dylan.com;password=bobbycool;date_of_birth=03/04/1993;"
    ]

    for message in messages:
        print(filter_datum(fields, 'xxx', message, ';'))
