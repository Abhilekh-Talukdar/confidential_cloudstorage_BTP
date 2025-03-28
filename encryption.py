import random

def generate_primes(min_prime=1000, max_prime=10000):
    """Generate primes between min_prime and max_prime where prime ≡ 3 mod 4."""
    sieve = [True] * (max_prime + 1)
    sieve[0], sieve[1] = False, False
    for current in range(2, int(max_prime ** 0.5) + 1):
        if sieve[current]:
            sieve[current*current : max_prime+1 : current] = [False] * len(sieve[current*current : max_prime+1 : current])
    # Filter primes ≡ 3 mod 4 and within range
    return [num for num, is_prime in enumerate(sieve) if is_prime and num >= min_prime and num % 4 == 3]

def decimal_to_binary(number):
    """Convert a decimal number to a binary string."""
    return format(number, 'b')

def encrypt():
    """Encrypt plaintext.txt using Rabin's cryptosystem with primes ≡ 3 mod 4."""
    primes = generate_primes()
    if not primes:
        raise ValueError("No primes of the form 4k+3 found in the specified range.")
    
    p, q = random.sample(primes, 2)  # Ensures p ≠ q
    n = p * q
    
    with open("keys.txt", "w") as keys_file:
        keys_file.write(f"{p}{q}")
    
    with open("plaintext.txt", "r") as plain_file, open("cypher.txt", "w") as cypher_file:
        while True:
            char = plain_file.read(1)
            if not char:
                break
            
            ascii_val = ord(char)
            binary_str = decimal_to_binary(ascii_val)
            extended_binary = binary_str + binary_str  # Double the bits
            
            m = int(extended_binary, 2)
            c = pow(m, 2, n)  # Efficient modular exponentiation
            
            cypher_bits = decimal_to_binary(c).zfill(32)  # Pad to 32 bits
            cypher_file.write(cypher_bits)

if __name__ == "__main__":
    encrypt()