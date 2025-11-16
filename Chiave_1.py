#Alberto Gibellato 5BI
#Messaggio e chiave dall'utente, chiave criptata e inserita in un file assieme al messaggio

import hashlib
import sys

messaggio = input("Scrivere un messaggio: ")

while True:
    chiave_input = input("Scrivere la chiave: ")
    if len(chiave_input) < 10:
        break
    print("Errore: la chiave deve essere meno di 10 caratteri.", file=sys.stderr)

hash_hex = hashlib.sha256(chiave_input.encode('utf-8')).hexdigest()

#print("Chiave:", chiave_input)
#print("SHA256:", hash_hex)

file_chiave = open("chiave.txt", "w")
file_chiave.write(hash_hex + "\n")
file_chiave.write(messaggio)
file_chiave.close()
