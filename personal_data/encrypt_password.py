#!/usr/bin/env python3
"""
Password Encryption Module

This module provides functionality for hashing passwords using bcrypt.
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
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


if __name__ == "__main__":
    password = "MyAmazingPassw0rd"
    print(hash_password(password))
    print(hash_password(password))
