# --- Shadow Extractor ---
# This script retrieves encrypted passwords from the /etc/shadow file on a Linux system, and identifies the hashing algorithm used.
# Note: Elevated privileges are required to run the script, i.e. 'sudo python3 shadow_extractor.py'

import os
path = '/etc'
os.chdir(path)


def hash_type(input):
    alg = ''
    count = 0
    for char in input:
        if count < 2:
            if char == '$':
                count += 1
            alg += char
    if alg == '$1$':
        print('MD5 algorithm detected:', alg)
    elif alg == '$2a$':
        print('Blowfish algorithm detected:', alg)
    elif alg == '$2y$':
        print('Blowfish algorithm detected:', alg)
    elif alg == '$5$':
        print('SHA-256 algorithm detected:', alg)
    elif alg == '$6$':
        print('SHA-512 algorithm detected:', alg)
    elif alg == '$y$':
        print('Yescrypt algorithm detected:', alg)
    else:
        print('Unknown algorithm detected.')


def shadow_parse(target_file):
    for line in target_file:
        uname, password, *fields= line.split(':')
        '''
        If the password field contains some string that is not a valid
        result of crypt(3), for instance ! or *, the user will not be able
        to use a unix password to log in (but the user may log in the
        system by other means).
        '''
        # This line excludes users with no password retrievable.
        if not password.startswith('!') and not password.startswith('*'):
            print(uname + ' ' + password)
            hash_type(password)


read_shadow = open('shadow', 'r')
lines = read_shadow.readlines()
shadow_parse(lines)
read_shadow.close()
