import hashlib
import random
import string
import time

personal_code = "50209090815"
M = int(personal_code[-2:])

def sha1_hash(message):
    """Compute the SHA-1 hash of a given message."""
    return hashlib.sha1(message.encode()).hexdigest()

def extract_bits(sha1_hex, start_bit, length=20):
    """Extract 20 bits from the SHA-1 hash starting from bit start_bit"""
    sha1_bin = bin(int(sha1_hex, 16))[2:].zfill(160)
    return sha1_bin[start_bit:start_bit + length]

def prsha1_hash(message, M):
    """Compute the PRSHA-1 hash of a given message."""
    sha1_hex = sha1_hash(message)
    start_bit = M + 1
    return extract_bits(sha1_hex, start_bit)

def find_collision(M):
    """Find a collision by generating random messages and comparing their PRSHA-1 hashes."""
    seen_hashes = {}
    attempts = 0
    start_time = time.time()

    while True:
        attempts += 1
        message = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        prsha1 = prsha1_hash(message, M)

        if prsha1 in seen_hashes:
            end_time = time.time()
            return seen_hashes[prsha1], message, prsha1, attempts, end_time - start_time

        seen_hashes[prsha1] = message

"""Print the two messages and their PRSHA-1 hash in hexadecimal format"""
S1, S2, prsha1, attempts, duration = find_collision(M)
print(f"Message 1: {S1}")
print(f"Message 2: {S2}")
print(f"PRSHA-1 Hash: 0x{int(prsha1, 2):05X}")
print(f"Attempts: {attempts}")
print(f"Duration: {duration:.3f} seconds")