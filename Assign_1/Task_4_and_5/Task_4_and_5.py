import sys
import os
import random
from string import ascii_lowercase

# system receive the key for encryption_substi
def receive_key():
    substi_key = int(input ("Please enter a number (1-25) as your key: "))
    while substi_key < 1 or substi_key > 25:
        substi_key = int(input ("Invalid key! Please enter a number as your key (1-25): "))
    return substi_key

# Substitution cipher, user should remember this key
def encryption_substi(plaintext):
    # Polyalphabetic cipher
    subst_key = receive_key()
    print("************************************************************")
    print(f"Your decryption key is: {subst_key}, please remember!")
    print("************************************************************")
    result = ""
    # encrypt the plaintext
    for i in range(len(plaintext)):
        char = plaintext[i]
        # if the character is not alphabet, it will not be processed
        if not char.isalpha():
            result += char
        # encrypt uppercase characters in plaintext     
        if char.isupper() and char.isalpha():
            result += chr((ord(char) + subst_key - 65) % 26 + 65)
        # encrypt lowercase characters in plain text
        if char.islower() and char.isalpha():
            result += chr((ord(char) + subst_key - 97) % 26 + 97)
    return result
    

# Transposition ciphers based on previous polyalphabetic cipher,
# trans_key for transposition encryption
def encryption_trans(plaintext,trans_key):
    result =[]
    length = len(trans_key)
    temp =[plaintext[i:i+length] for i in range(0,len(plaintext),length)]
    for item in temp[:-1]:
        new_item=''
        for i in trans_key:
            new_item = new_item + item[i-1]
        result.append(new_item)
    return''.join(result) + temp[-1]

# Decrypt transposition ciphers 
def decryption_trans (encrypt_text,trans_key):
    return encryption_trans(encrypt_text,trans_key)
    
# Decrypt substitution cipher
def decryption_substi(decrypt_trans):
    subst_key = int(input("Please enter your key: "))
    result = ""
    for i in range(len(decrypt_trans)):
        char = decrypt_trans[i]
        if not char.isalpha():
            result += char
        # Encrypt uppercase characters in plain text     
        if char.isupper() and char.isalpha():
            result += chr((ord(char) - subst_key - 65) % 26 + 65)
        # Encrypt lowercase characters in plain text
        if char.islower() and char.isalpha():
            result += chr((ord(char) - subst_key - 97) % 26 + 97)
    return result

# Output file
def write_file( message, file_path ):
    with open ( file_path, "w" ,encoding = "utf-8" ) as file:
        file.write ( message )

# Read file
def read_file(file_name_encryp):
    print( "\nReading from: ", file_name_encryp )
    with open ( file_name_encryp, "r", encoding = "utf-8") as file:
        full_text = ""
        for lines in file:
            full_text += lines
            print( lines.strip() ) # add this to instantly show result
    return full_text

# program start
# ****READ_ME****:
# Selection 1 and 2 are designed for Task 4 on report
# All the files will generate to the same path as this program
# Selection 3 and 4 are designed for Task 5 on report
# To decrypt the uploaded cipher please copy it to the same path as this program
while True:
    print(">>>Please make a selection!<<<")
    selection = int (input("'1' message encryption, '2' messsage decryption, '3' file encryption, '4' file decryption ('0'Exit): "))
    # message encryption
    if selection == 1:
        message = input ("Please enter a message, use space to divide words: ")
        # step 1, substitution cipher
        message_subst = encryption_substi(message)
        # step 2, transposition ciphers
        message_encryt = encryption_trans(message_subst,(1,4,3,2))
        try:
            print( os.getcwd() )
            write_file (message_encryt, "message_encryption.txt" )
            print(">>>The file's content has been successfully written to the encryption file 'message_encryption.txt'")
        except FileNotFoundError as e:
            print (e)
    # message decryption
    elif selection == 2:
        try:
            lines = read_file ("message_encryption.txt")
            decrypt_text = decryption_trans (lines,(1,4,3,2))
            plaintext = decryption_substi(decrypt_text)
            write_file(plaintext, "message_plaintext.txt")
            print(">>>The file's content has been successfully written to the new file 'message_plaintext.txt'")
        except FileNotFoundError as e:
            print (e)
    # file encryption
    elif selection == 3:
        try:
            lines = read_file ("plaintext.txt")
            file_subst = encryption_substi(lines)
            file_encryt = encryption_trans(file_subst,(1,4,3,2))
            write_file (file_encryt, "encryption.txt" )
            print(">>>The file's content has been successfully written to the new file 'encryption.txt'")
        except FileNotFoundError as e:
            print (e)
    # file decryption
    elif selection == 4:
        try:
            lines = read_file ( "encryption.txt" )
            decrypt_trans = decryption_trans (lines,(1,4,3,2))
            plaintext = decryption_substi(decrypt_trans)
            write_file (plaintext, "generate_plaintext.txt" )
            print(">>>The file's content has been successfully written to the new file 'generate_plaintext.txt'")
        except FileNotFoundError as e:
            print (e)
    elif selection == 0:
        sys.exit(">>>Exit!<<<")
    else:
        sys.exit(">>>Please enter a vaild selection!<<<")  
