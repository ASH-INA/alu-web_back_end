#!/usr/bin/env python3
"""
Password Encryption Module

This module provides functionality for hashing and verifying passwords using bcrypt.
"""

import bcrypt


def hash_password(password: str) -> bytes:
    """
    Hash a password using bcrypt with salt.

    Args:
        password: The plain text password to hash

    Returns:
        A salted, hashed password as byte string
    """
    # Convert password to bytes (bcrypt requires bytes)
    password_bytes = password.encode('utf-8')

    # Generate salt and hash the password
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password_bytes, salt)

    return hashed_password


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Verify if a password matches the hashed password.

    Args:
        hashed_password: The hashed password (bytes)
        password: The plain text password to verify

    Returns:
        True if the password matches, False otherwise
    """
    # Convert password to bytes
    password_bytes = password.encode('utf-8')

    # Use bcrypt to check if the password matches the hash
    return bcrypt.checkpw(password_bytes, hashed_password)


# Test the functions
if __name__ == "__main__":
    password = "MyAmazingPassw0rd"
    encrypted_password = hash_password(password)
    print(encrypted_password)
    print(is_valid(encrypted_password, password))

    # Test with wrong password
    print(is_valid(encrypted_password, "WrongPassword"))
