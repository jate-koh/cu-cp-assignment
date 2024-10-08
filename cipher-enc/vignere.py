import time
import colorama
import argparse
import sys
import random

def vigenere_encrypt(plaintext, key):
    counter = 0
    encoded_text = ""
    for char in plaintext:
        vig_key_val = 0
        if char.islower():
            vig_key = key[counter]
            if vig_key.islower():
                vig_key_val = ord(vig_key) - ord("a")
            elif vig_key.isupper():
                vig_key_val = ord(vig_key) - ord("A")

            vig_char = chr(((ord(char) - ord("a") + vig_key_val) %26) +ord("a"))
            counter += 1

        elif char.isupper():
            vig_key = key[counter]
            if vig_key.islower():
                vig_key_val = ord(vig_key) - ord("a")
            elif vig_key.isupper():
                vig_key_val = ord(vig_key) - ord("A")

            vig_char = chr(((ord(char) - ord("A") + vig_key_val) %26) +ord("A"))
            counter += 1

        if counter == len(key):
            counter = 0

        if not char.isalpha():
            vig_char = char


        encoded_text += vig_char

    return encoded_text

def vigenere_decrypt(encodedtext, key):
    counter = 0
    decoded_text = ""
    for char in encodedtext:
        vig_key_val = 0
        if char.islower():
            vig_key = key[counter]
            if vig_key.islower():
                vig_key_val = ord(vig_key) - ord("a")
            elif vig_key.isupper():
                vig_key_val = ord(vig_key) - ord("A")

            vig_char = chr(((ord(char) - ord("a") - vig_key_val) %26) +ord("a"))
            counter += 1

        elif char.isupper():
            vig_key = key[counter]
            if vig_key.islower():
                vig_key_val = ord(vig_key) - ord("a")
            elif vig_key.isupper():
                vig_key_val = ord(vig_key) - ord("A")

            vig_char = chr(((ord(char) - ord("A") - vig_key_val) %26) +ord("A"))
            counter += 1

        if counter == len(key):
            counter = 0

        if not char.isalpha():
            vig_char = char


        decoded_text += vig_char

    return decoded_text

plaintext = "Hello, World!"
key = "luck"

print("Plaintext: ", plaintext)
print("Key: ", key)

print("Encrypted text: ")
print(vigenere_encrypt(plaintext, key))

print("Decrypted text: ")
print(vigenere_decrypt(vigenere_encrypt(plaintext, key), key))