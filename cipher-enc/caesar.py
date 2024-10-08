import json
from collections import Counter
import string

# Load the dictionary of English words from the JSON file
with open('words_dictionary.json', 'r') as f:
    english_words = json.load(f)

# Define common two-letter and three-letter words in English
common_twos = ['an', 'as', 'at', 'be', 'by', 'do', 'go', 'he', 'if', 'in', 'is', 'it', 'me', 'my', 'no', 'of', 'on', 'or', 'so', 'to', 'up', 'us', 'we']
common_threes = ['the', 'and', 'for', 'are', 'but', 'not', 'you', 'all', 'any', 'can', 'had', 'her', 'his', 'out', 'one', 'our', 'say', 'see', 'she', 'too', 'use']

# Function to perform a monoalphabetic substitution
def substitute_letters(text, substitution_map):
    return ''.join([substitution_map.get(c, c) for c in text])

# Function to check if the word exists in the dictionary
def is_valid_word(word):
    return word.lower() in english_words

def decipher(text):

    # Split the text into words
    words = text.split()
    print(words)

    # Find minimum and maximum word length
    min_length = min([len(word) for word in words])
    max_length = max([len(word) for word in words])

    
    
def decipher_common_twos(words, length):
    local_map_list = []

    # Fetch only words of the specified length
    words = [word for word in words if len(word) == length]
    if len(words) == 0:
        return

    # Iterate through the common two-letter words
    for word in words:
        for common in common_twos:
            # Check if the word can be deciphered
            if len(word) == len(common):
                # Create a substitution map
                sub_map = {}
                for i in range(len(word)):
                    sub_map[word[i]] = common[i]

                # Append the substitution map to the list
                local_map_list.append(sub_map)
    return local_map_list

def decipher_common_threes(words, length):
    local_map_list = []

    # Fetch only words of the specified length
    words = [word for word in words if len(word) == length]
    if len(words) == 0:
        return
    
    # Iterate through the common three-letter words
    for word in words:
        for common in common_threes:
            # Check if the word can be deciphered
            if len(word) == len(common):
                # Create a substitution map
                sub_map = {}
                for i in range(len(word)):
                    sub_map[word[i]] = common[i]
                
                # Append the substitution map to the list
                local_map_list.append(sub_map)
    return local_map_list

def decipher_words(words, length):
    # Fetch only words of the specified length
    words = [word for word in words if len(word) == length]
    if len(words) == 0:
        return
    
    print(words)
    
# Decipher text
ciphertext = "PRCSOFQX FP QDR AFOPQ CZSPR LA JFPALOQSKR. QDFP FP ZK LIU BROJZK MOLTROE."
print("Ciphertext: \n", ciphertext)
print("\nDeciphered Text: \n")
print(decipher(ciphertext))
