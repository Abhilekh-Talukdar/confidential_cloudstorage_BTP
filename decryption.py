def decimal_to_binary(number):
    """Convert a decimal number to its binary string representation."""
    return format(number, 'b')

def is_repeating_string(binary_str):
    """Check if a binary string is formed by repeating the same half."""
    midpoint = len(binary_str) // 2
    return binary_str[:midpoint] == binary_str[midpoint:]

def extended_gcd(a, b):
    """
    Extended Euclidean Algorithm to find coefficients (x, y) such that ax + by = gcd(a, b).
    Returns (gcd, x, y) where gcd is the GCD of a and b.
    """
    if a == 0:
        return (b, 0, 1)
    else:
        gcd, x, y = extended_gcd(b % a, a)
        return (gcd, y - (b // a) * x, x)

def decrypt():
    """Decrypt cypher.txt using Rabin's cryptosystem and write the result to decrypt.txt."""
    # Read primes p and q from keys.txt (assumed to be 4-digit each)
    with open("keys.txt", "r") as keys_file:
        key_data = keys_file.read().strip()
        p = int(key_data[:4])
        q = int(key_data[4:8])
    n = p * q

    # Calculate Bézout coefficients using Extended Euclidean Algorithm
    gcd, a, b = extended_gcd(p, q)
    if gcd != 1:
        raise ValueError("Primes p and q must be coprime.")

    with open("cypher.txt", "r") as cypher_file, open("decrypt.txt", "w") as decrypt_file:
        while True:
            cypher_bits = cypher_file.read(32)
            if not cypher_bits:
                break

            c = int(cypher_bits, 2)

            # Compute square roots modulo p and q
            exponent_p = (p + 1) // 4
            exponent_q = (q + 1) // 4
            r = pow(c, exponent_p, p)  # Equivalent to c^((p+1)/4) mod p
            s = pow(c, exponent_q, q)  # Equivalent to c^((q+1)/4) mod q

            # Use Chinese Remainder Theorem to find possible plaintexts
            x = (a * p * s + b * q * r) % n
            y = (a * p * s - b * q * r) % n
            candidates = [x, y, n - x, n - y]

            # Check each candidate for repeating binary pattern
            found = False
            for candidate in candidates:
                binary_str = decimal_to_binary(candidate)
                if is_repeating_string(binary_str):
                    midpoint = len(binary_str) // 2
                    plain_bits = binary_str[:midpoint]
                    decrypt_file.write(chr(int(plain_bits, 2)))
                    found = True
                    break

            if not found:
                decrypt_file.write("�")  # Replacement character for errors

if __name__ == "__main__":
    decrypt()