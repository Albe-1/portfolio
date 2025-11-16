#Alberto Gibellato 5BI
#Leggo da file la chiave criptata e la confronto con quella inserita

import hashlib
import sys

chiave_input2 = input("Scrivere la chiave per visualizzare il messaggio: ")

hash_hex2 = hashlib.sha256(chiave_input2.encode('utf-8')).hexdigest()

lettura_file = open("chiave.txt", "r")
riga_chiave = lettura_file.readline().strip()
riga_messaggio = lettura_file.read()

#print("chiave: " + riga_chiave)
lettura_file.close()

if hash_hex2 == riga_chiave:
    print("Chiave accettata")
    print("Messaggio: ", riga_messaggio)
else:
    print("Chiave non accettata")