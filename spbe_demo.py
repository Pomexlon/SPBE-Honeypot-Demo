import sympy

# Function to generate random primes
def generate_prime(bits=512):
    return sympy.randprime(2**(bits-1), 2**bits)

# Generate RSA-style keys
def generate_keys():
    p = generate_prime()
    q = generate_prime()
    n = p * q
    phi_n = (p - 1) * (q - 1)
    e = 65537
    d = pow(e, -1, phi_n)
    return (e, n), (d, n)

# Encryption function
def encrypt(msg, public_key):
    e, n = public_key
    return pow(msg, e, n)

# Decryption function
def decrypt(cipher, private_key):
    d, n = private_key
    return pow(cipher, d, n)

# Main script execution
if __name__ == "__main__":
    import sympy

    # Your custom numeric message here:
    message = 987654321  # <-- Define your message clearly here

    print("Original Message:", message)

    public_key, private_key = generate_keys()

    cipher = encrypt(message, public_key)
    print("Encrypted Message:", cipher)

    decrypted_message = decrypt(cipher, private_key)
    print("Decrypted Message:", decrypted_message)

    if decrypted_message == message:
        print("Demo Successful: Message decrypted correctly!")
    else:
        print("Demo Failed: Decryption mismatch.")

