# --- Shadow Extractor ---
# This script retrieves encrypted passwords from the /etc/shadow file on a Linux system.
# Note: Elevated privileges are required to run the script, i.e. 'sudo python3 shadow_extractor.py'

import os
path = '/etc'
os.chdir(path)

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

read_shadow = open('shadow', 'r')
lines = read_shadow.readlines()
shadow_parse(lines)
read_shadow.close()
