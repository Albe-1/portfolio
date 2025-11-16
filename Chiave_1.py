#Alberto Gibellato 5BI

import hashlib
import sys

messagge = input("Write a message: ")

while True:
    key_input = input("Write the key: ")
    if len(key_input) < 10:
        break
    print("Error: the key must be less than 10 characters.", file=sys.stderr)

hash_hex = hashlib.sha256(key_input.encode('utf-8')).hexdigest()

#print("Key:", key_input)
#print("SHA256:", hash_hex)

file_key = open("key.txt", "w")
file_key.write(hash_hex + "\n")
file_key.write(messagge)
file_key.close()
