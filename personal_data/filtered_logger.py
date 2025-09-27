#!/usr/bin/env python3
"""
Filtered Logger Module

This module provides functionality to obfuscate personally identifiable
information (PII) in log messages using regular expressions.
"""

import os
import re
import logging
import mysql.connector
from typing import List
from mysql.connector.connection import MySQLConnection


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


def get_db() -> MySQLConnection:
    """
    Connect to the MySQL database using environment variables.

    Returns:
        MySQLConnection object to the database
    """
    # Get database credentials from environment variables with defaults
    username = os.getenv('PERSONAL_DATA_DB_USERNAME', 'root')
    password = os.getenv('PERSONAL_DATA_DB_PASSWORD', '')
    host = os.getenv('PERSONAL_DATA_DB_HOST', 'localhost')
    database = os.getenv('PERSONAL_DATA_DB_NAME')

    # Check if database name is provided
    if not database:
        raise ValueError("PERSONAL_DATA_DB_NAME environment variable is required")

    # Create and return database connection
    connection = mysql.connector.connect(
        user=username,
        password=password,
        host=host,
        database=database
    )

    return connection


def main() -> None:
    """
    Main function that retrieves and displays filtered user data from database.
    """
    # Get the logger
    logger = get_logger()

    # Get database connection
    db = get_db()
    cursor = db.cursor(dictionary=True)

    # Execute query to get all users
    cursor.execute("SELECT * FROM users;")

    # Process each row
    for row in cursor:
        # Build log message in key=value format
        message_parts = []
        for key, value in row.items():
            message_parts.append(f"{key}={value}")
  
        # Join parts with semicolon separator
        log_message = ";".join(message_parts) + ";"
  
        # Log the filtered message
        logger.info(log_message)

    # Clean up
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
