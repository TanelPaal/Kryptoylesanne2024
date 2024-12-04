import hashlib
import random
import string
import time

personal_code = "50209090815"
P = personal_code

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

def find_collision(P, M):
    """Find a collision by generating random messages and comparing their PRSHA-1 hashes."""
    attempts = 0
    start_time = time.time()
    prsha1_P = prsha1_hash(P, M)

    while True:
        attempts += 1
        message_length = random.randint(1, 11)
        Q = ''.join(random.choices(string.ascii_letters + string.digits, k=message_length))
        prsha1_Q = prsha1_hash(Q, M)

        if prsha1_Q == prsha1_P and Q != P:
            end_time = time.time()
            return P, Q, prsha1_P, attempts, end_time - start_time

def estimate_attempts():
    """Estimate the number of attempts required for a collision attack."""
    return 524288

"""Print the original message P, the found message Q, and their PRSHA-1 hash in hexadecimal format."""
M = int(personal_code[-2:])
P, Q, prsha1, attempts, duration = find_collision(P, M)
estimated_attempts = estimate_attempts()

print(f"Original message P: {P}")
print(f"Found message Q: {Q}")
print(f"PRSHA-1 Hash: 0x{int(prsha1, 2):05X}")
print(f"Estimated Attempts: {estimated_attempts}")
print(f"Actual Attempts: {attempts}")
print(f"Duration: {duration:.3f} seconds")