
# Read rainbow table from file
rainbow_table = {}
with open("rainbow_table.txt", "r") as file:
    for line in file:
        hash, word = line.strip().split(" ")
        rainbow_table[hash] = word

# Input hash
hash = input("Enter hash: ")

# Find password
if hash in rainbow_table:
    print(f"Password: {rainbow_table[hash]}")
else:
    print("Password not found")
