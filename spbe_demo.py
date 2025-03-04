# Simplified SPBE-Honeypot Basic Encryption Demo (GitHub Safe)
import sympy
import random

# Generate simplified primes (for demonstration, not actual SPBE prime structure)
def generate_prime(bits=256):
    return sympy.randprime(2**(bits-1), 2**bits)

# Key generation (Basic RSA-style simplified)
def generate_keys():
    p = generate_prime()
    q = generate_prime()
    n = p * q
    phi_n = (p-1)*(q-1)
    e = 65537  # commonly used public exponent
    d = sympy.mod_inverse(e, phi_n)
    return ((e, n), (d, n))

# Encrypt message
def encrypt(msg, pub_key):
    e, n = pub_key
    cipher = pow(msg, e, n)
    return cipher

# Decrypt message
def decrypt(cipher, priv_key):
    d, n = priv_key
    msg = pow(cipher, d, n)
    return msg

# Demonstration of encryption/decryption flow
def demo():
    pub_key, priv_key = generate_keys()
    message = 1234567890

    print(f"Original Message: {message}")

    encrypted_message = encrypt(message, pub_key)
    print(f"Encrypted Message: {encrypted_message}")

    decrypted_message = decrypt(encrypted_message, priv_key)
    print(f"Decrypted Message: {decrypted_message}")

    if decrypted_message == message:
        print("Demo Successful: Message decrypted correctly!")
    else:
        print("Demo Failed: Incorrect decryption!")

if __name__ == '__main__':
    demo()
