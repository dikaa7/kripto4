import random
from util import is_prime, gcd, lcm, modinv

def generate_keypair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal')

    n = p * q
    phi = lcm((p-1),(q-1))

    g = random.randrange(1, n**2)
    Lx = (g**phi)%(n**2)
    L = (Lx-1)//n
    u = modinv(L, n)

    return ((g, n), (phi, u))

def pailer_encrypt(pk, plaintext):
    key, n = pk
    r = random.randrange(0, n)
    g = gcd(r, n)
    while g != 1:
        r = random.randrange(0, n)
        g = gcd(r, n)

    cipher = [((key ** ord(char)) * (r ** n)) % (n**2) for char in plaintext]
    return cipher

def pailer_decrypt(pk, n, ciphertext):
    key, u = pk
    plain = [(((((char ** key) % (n**2)) - 1) // n) * u) % n for char in ciphertext]
    return ''.join([chr(x) for x in plain])


# pub, pri = generate_keypair(11,13)
# text = "hello"
# cipher = pailer_encrypt(pub, text)
# plain = pailer_decrypt(pri, cipher)

# print(pub, pri)
# print(cipher)
# print(plain)