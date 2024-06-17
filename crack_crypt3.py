# This program is used to crack a Crypt(3) DES password, given a password dictionary file (Google RockYou), and a string containing user/salt/password; i.e. Sally:AAencryptedpassword
# Reference: This program is a variation of a "cracker" from the book Violent Python by TJ O'Connor (Pg. 22-23).

import crypt

def testPass(cryptPass):
    salt = cryptPass[0:2]                       # Slice out the first 2 chars (salt value).
    dictFile = open('dictionary.txt', 'r')
    for word in dictFile.readlines():
        word = word.strip('\n')                 # Remove any newline chars.
        cryptWord = crypt.crypt(word,salt)      # Create a hash using the password + salt.
        if cryptWord == cryptPass:
            print("Password found:", word)
            return
    print("Password not found.")
    return

def main():
    passFile = open('passwords.txt')
    for line in passFile.readlines():
        if ":" in line:
            user = line.split(':')[0]                               # Slice out the user (chars before ':').
            cryptPass = line.split(':')[1].strip(' ').strip('\n')   # Set the password after the ':' and remove unwanted chars.
            print("Cracking password for:", user)
            print(cryptPass)
            testPass(cryptPass)

main()
