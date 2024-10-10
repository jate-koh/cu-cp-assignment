import hashlib
import os
import time

# Start timer
start_time = time.time()

# Import words from txt file
total_words = 0
with open("10k-most-common.txt") as f:
    words = f.read().splitlines()

# Sample specified number of words
n = 10000
sample = words[:n]
# print(sample)

# Create every possible combination
combinations = []
max_length = 5
for word in sample:
    # Get word length
    word_length = len(word)

    # Save maximum length
    if word_length > max_length:
        max_length = word_length

    for i in range(word_length + 1):
        for j in range(i, word_length + 1):
            # Create a new word
            new_word = word[:i] + word[i:j].upper() + word[j:]
            combinations.append(new_word)



# Create substitute combinations
# [‘o’ => 0 , ‘l’ => 1, ‘i’ => 1]
substitutes_table = {
    'o': ['0'],
    'l': ['1'],
    'i': ['1']
}

# Recursive function to substitute letters
def substitute_rec(letters, current_combination=""):
    if len(letters) == 0:
        return [current_combination]
    
    current_letter = letters[0]
    remaining_letters = letters[1:]

    # List to collect all combinations
    combinations = []

    # Add the original letter without substitution
    combinations += substitute_rec(remaining_letters, current_combination + current_letter)

    # Add all possible substitutions if any
    if current_letter.lower() in substitutes_table:
        for substitute in substitutes_table[current_letter.lower()]:
            combinations += substitute_rec(remaining_letters, current_combination + substitute)
    
    return combinations

substitutes_combinations = []
for word in combinations:
    substitutes_combinations.extend(substitute_rec(word))

# Remove duplicates if necessary
substitutes_combinations = list(set(substitutes_combinations))

# Hash each combination
hashes = []
for combination in combinations:
    hash = hashlib.sha1(combination.encode()).hexdigest()
    hashes.append(hash)

# Hash each substitute combination
hashes_substitutes = []
for combination in substitutes_combinations:
    hash = hashlib.sha1(combination.encode()).hexdigest()
    hashes_substitutes.append(hash)

# Rainbow table
rainbow_table = {}
for i in range(len(hashes)):
    rainbow_table[hashes[i]] = combinations[i]
for i in range(len(hashes_substitutes)):
    rainbow_table[hashes_substitutes[i]] = substitutes_combinations[i]

# Remove rainbow table if it exists
try:
    os.remove("rainbow_table.txt")
except FileNotFoundError:
    pass

# Save rainbow table to a file
with open("rainbow_table.txt", "w") as f:
    for key, value in rainbow_table.items():
        f.write(f"{key} {value}\n")

# End timer
end_time = time.time()

# Print results
print("Execution time: ", end_time - start_time, "seconds")
print("Table size: ", len(rainbow_table))
print("Total number of words: ", len(words))
print("Max length: ", max_length)
print("Number of combinations: ", len(combinations))
print("Number of substitute combinations: ", len(substitutes_combinations))
print("Total number of combinations: ", len(combinations) + len(substitutes_combinations))
print("Number of hashes: ", len(hashes) + len(hashes_substitutes))