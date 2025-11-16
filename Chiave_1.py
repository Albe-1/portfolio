#Alberto Gibellato 5BI

import hashlib
import sys

messagge = input("Write a message: ")

while True:
    chiave_input = input("Write the key: ")
    if len(chiave_input) < 10:
        break
    print("Error: the key must be less than 10 characters.", file=sys.stderr)

hash_hex = hashlib.sha256(chiave_input.encode('utf-8')).hexdigest()

#print("Key:", chiave_input)
#print("SHA256:", hash_hex)

file_chiave = open("key.txt", "w")
file_chiave.write(hash_hex + "\n")
file_chiave.write(messagge)
file_chiave.close()
