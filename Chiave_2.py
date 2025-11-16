#Alberto Gibellato 5BI

import hashlib
import sys

key_input2 = input("Write the key to view the message: ")

hash_hex2 = hashlib.sha256(key_input2.encode('utf-8')).hexdigest()

reading_file = open("key.txt", "r")
line_key = reading_file.readline().strip()
line_messagge = reading_file.read()

#print("key: " + line_key)
reading_file.close()

if hash_hex2 == line_key:
    print("Key accepted")
    print("Messagge: ", line_messagge)
else:
    print("Key not accepted")
