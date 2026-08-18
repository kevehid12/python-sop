# Python Password Utility App with Breach Detection

A secure, dual-purpose Python command-line application built for the Sophia Learning Python Touchstone project.

## Features
1. **Password Strength Evaluation:** Checks length, uppercase/lowercase letters, numbers, and special symbols.
2. **Live Breach Detection:** Queries the Have I Been Pwned (HIBP) API using secure $k$-anonymity SHA-1 hashing to check if a password has been compromised in public data leaks.
3. **Secure Password Generator:** Generates cryptographically random, strong passwords of custom lengths.

## Requirements
* Python 3.x
* `requests` library (`pip install requests`)
