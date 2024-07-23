### Host Discovery Scanner (IPv4) ###
# This scanner identifies hosts on a given network via ping responses.
# By default the scanner will determine your current network and scan it (if you press ENTER).
# While this scanner isn't as fast or robust as NMAP, it is stealthier! Live off the land!

import os
import ipaddress
import socket
import time
import re

print("          ________")
print("         /\       \\")
print("        /  \       \\")
print("       /    \       \\")
print("      /      \_______\ ")
print("      \      /       /")
print("    ___\    /   ____/___")
print("   /\   \  /   /\       \\")
print("  /  \   \/___/  \       \\")
print(" /    \       \   \       \\")
print("/      \_______\   \_______\\")
print("\      /       /   /       /")
print(" \    /       /   /       /")
print("  \  /       /\  /       /")
print("   \/_______/  \/_______/ ")
print("\n*** Host Discovery Scanner (IPv4) ***\n")

class_a = ipaddress.IPv4Network("10.0.0.0/8")
class_b = ipaddress.IPv4Network("172.16.0.0/12")
class_c = ipaddress.IPv4Network("192.168.0.0/16")

hostname = socket.gethostname()

current_ip = os.popen("ifconfig | \
grep -Eo 'inet (addr:)?([0-9]*\.){3}[0-9]*' | \
grep -Eo '([0-9]*\.){3}[0-9]*' | \
grep -v '127.0.0.1'").read()

default_target = str(current_ip).strip("\n")

temp = ''
count = 0

for char in default_target:
    if count < 3:
        temp += char
    if char == '.' and count < 3:
        count += 1

default_target = ipaddress.ip_network(temp + '0/24')

#print("DEFAULT TARGET 2:", default_target)

print("The current host is \""+ hostname +"\" on network", default_target, "and is using IP address", current_ip)
print("Which network would you like to scan?...\n")
print("0) Press -ENTER- to run a scan against the current network:", default_target)
print("1) Type a specific network, i.e. 1.2.3.4/24")
print("2)", class_c, " --> [65,536 Addresses]")
print("3)", class_b, "     --> [1,048,576 Addresses]")
print("4)", class_a, "  --> [16,777,216 Addresses]")

valid = False
while valid == False:
    selection = input("\nChoose a number 0-4: ")
    if selection not in ('','0','1','2','3','4'):
        print("Invalid selection.")
    else:
        valid = True
if selection == '0' or selection == '':
    target_network = default_target
if selection == '2':
    target_network = class_c
if selection == '3':
    target_network = class_b
if selection == '4':
    target_network = class_a
if selection == '1':
    valid = False
    while valid == False:
        target_network = input("Type the specific network to scan: ")
        try:
            # Try to cast the selected target to type ip_network.
            target_network = ipaddress.ip_network(target_network, False)
            valid = True
        except:
            print("Malformed network. Try again.")

os.system('clear')
print("Host discovery scan started for network", target_network)
start = time.perf_counter()

#target_network = [ipaddress.IPv4Address('192.168.0.79'), ipaddress.IPv4Address('192.168.1.255'), ipaddress.IPv4Address('192.168.1.0'), ipaddress.IPv4Address('192.168.1.79')]

trigger = False
received = False
temp = ''

for ip in target_network:
    ip = str(ip)
    # Exclusion regex for broadcast and network IP addresses.
    broadcast_pattern = re.search("^.*\.255$", ip)
    network_pattern = re.search("^.*\.0$", ip)

    if (not broadcast_pattern and not network_pattern):
        # Send a single test ping with a wait time of 0.002ms.
        test_ping = os.popen("ping -c 1 -i 0.002 " + ip).read()
        for data in test_ping:
            if (trigger == True) and (data == '1' or data == '0'):
                if data == '1':
                    received = True
                    trigger = False
                    print('\nPacket Received! Response from:', ip, end="")
                if data == '0':
                    trigger = False
            if data != ' ':
                temp += data
                # This code checks for a matching assembled string in the ping output.
                # We want to locate this string because the proceeding string (1 or 0) will tell us whether the ping was successful.
                if temp == 'transmitted,':
                    trigger = True
            else:
                temp = ''

stop = time.perf_counter()
print(f"\n\nScan finished in {stop - start:0.4f} seconds ({(stop - start)/60:0.4f} minutes.)")
