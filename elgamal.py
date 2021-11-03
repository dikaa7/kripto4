import random
from math import pow
from util import power, gcd

def generate_key(q):
    key = random.randint(1,q)
    while gcd(q,key) != 1:
        key = random.randint(1,q)
    return key

def generate_keypair(p, g):
    key = generate_key(p)
    h = power(g,key,p)
    return (p,g,h), key

def elgamal_encrypt(pk, plaintext):
    q,g,h = pk
    k = generate_key(q)
    s = power(h,k,q)
    p = power(g,k,q)
    cipher = [(ord(char) * s) for char in plaintext]

    return cipher,p

def elgamal_decrypt(c1, key, p, ciphertext):
    h = power(c1,key,p)
    plaintext = [chr(int(char/h)) for char in ciphertext]
    return ''.join([x for x in plaintext])

# msg = input("Enter message: ")
# q = random.randint(1,1000)
# g = random.randint(2,q)
# key = generate_keypair(q)
# h = power(g,key,q)

# print("g used=", g)
# print("g^a used=", h)

# cipher, p = elgamal_encrypt(msg, q, h, g)

# print("Original Message=",msg)
# print("Encrypted Maessage=",cipher)

# plain = elgamal_decrypt(cipher,p,key,q)
# print("Decryted Message=",plain)