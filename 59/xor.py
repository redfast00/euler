import sys
import string

english_values = set((ord(character) for character in string.ascii_letters + string.digits +' ().,;!?\'\"'))
password_length = 3

def decrypt(ciphertext):
    candidates = []
    for decryption_key in (ord(character) for character in string.ascii_lowercase):
        for plaintext in (cipherbyte ^ decryption_key for cipherbyte in ciphertext):
            if plaintext not in english_values:
                break
        else:
            return decryption_key

total = 0
with open(sys.argv[1]) as infile:
    values = [int(value) for value in infile.read().strip().split(',')]
    for i in range(password_length):
        candidate = decrypt(values[i::password_length])
        print(chr(candidate)) # god
    for idx, cipherbyte in enumerate(values):
        cleartext = ord('god'[idx % password_length]) ^ cipherbyte
        print(chr(cleartext), end='')
        total += cleartext
    print(f'\ntotal = {total}')
