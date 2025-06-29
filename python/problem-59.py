"""
Each character on a computer is assigned a unique code and the preferred standard 
is ASCII (American Standard Code for Information Interchange). For example, 
uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

A modern encryption method is to take a text file, convert the bytes to ASCII, 
then XOR each byte with a given value, taken from a secret key. The advantage with 
the XOR function is that using the same encryption key on the cipher text restores 
the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.

For unbreakable encryption, the key is the same length as the plain text message, 
and the key is made up of random bytes. The user would keep the encrypted message 
and the encryption key in different locations, and without both "halves", it is 
impossible to decrypt the message.

Unfortunately, this method is impractical for most users, so the modified method 
is to use a password as a key. If the password is shorter than the message, which 
is likely, the key is repeated cyclically throughout the message. The balance 
for this method is using a sufficiently long password key for security, but short 
enough to be memorable.

Your task has been made easy, as the encryption key consists of three lower case 
characters. Using 0059_cipher.txt (right click and 'Save Link/Target As...'), a 
file containing the encrypted ASCII codes, and the knowledge that the plain text 
must contain common English words, decrypt the message and find the sum of the 
ASCII values in the original text.
"""
#%%
from itertools import combinations_with_replacement, permutations
letters = range(97, 97+26)
with open("common_english_words.txt", 'r') as f:
    dictionary = f.read().split("\n")

with open("0059_cipher.txt", "r") as f:
    cipher = f.read().split(",")


current_word = ''
non_alphabetic_characters = '$!,{}|~\\|[]@?>=</&\\%`^_'
possible_key = combinations_with_replacement(letters, 3)

current_password = (97, 97, 96)
current_n_words = 0

for possible_combinations in possible_key:
    possible_passwords = permutations(possible_combinations)
    for password in possible_passwords:
        n_words = 0
        current_word = ''
        for ix in range(len(cipher)):
            code = int(cipher[ix])
            character = chr(code ^ password[ix % 3])
            if character in '{}|~\\|[]@>=/<&`':
                break
            if character == ' ' or character == ',':
                current_word = current_word.lower()
                if current_word in dictionary:
                    n_words += 1
                current_word = ''
            else:
                current_word += character
        if n_words > current_n_words:
            current_n_words = n_words
            current_password = password

actual_text = ''
res = 0
for ix in range(len(cipher)):
    code = int(cipher[ix])
    ascii_code = code ^ current_password[ix % 3]
    res += ascii_code
    character = chr(ascii_code)
    actual_text += character

print(f"The sum of the ascii codes in the decrypted text is {res}")