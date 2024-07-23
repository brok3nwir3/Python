### Host Discovery Scanner (IPv4) ###
# This scanner identifies hosts on a given network via ping responses.
# While this scanner is not as fast or robust as NMAP, it is stealthier!

import os
import ipaddress
import socket
import time

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

priv_network1 = ipaddress.IPv4Network("192.168.0.0/16")
priv_network2 = ipaddress.IPv4Network("172.16.0.0/12")
priv_network3 = ipaddress.IPv4Network("10.0.0.0/8")
hostname = socket.gethostname()
current_ip = os.popen("ifconfig | \
grep -Eo 'inet (addr:)?([0-9]*\.){3}[0-9]*' | \
grep -Eo '([0-9]*\.){3}[0-9]*' | \
grep -v '127.0.0.1'").read()

print("The current host is \""+ hostname +"\" and is using IP address:", current_ip,)
print("Which network would you like to scan?...")
print("1)", priv_network1, " --> [65,536 Addresses]")
print("2)", priv_network3, "     --> [1,048,576 Addresses]")
print("3)", priv_network2, "  --> [16,777,216 Addresses]")
print("4) Enter a specific network, i.e. 1.2.3.4/24")

valid = False
while valid == False:
    selection = input("\nChoose a number 1-4: ")
    if selection not in ('1','2','3','4'):
        print("Invalid selection.")
    else:
        valid = True

if selection == '1':
    target_network = priv_network1
if selection == '2':
    target_network = priv_network2
if selection == '3':
    target_network = priv_network3
if selection == '4':
    valid = False
    while valid == False:
        target_network = input("Enter the specific network to scan: ")
        try:
            target_network = ipaddress.ip_network(target_network)
            valid = True
        except:
            print("Malformed network. Try again.")

os.system('clear')
print("Host discovery scan started for network", target_network)
start = time.perf_counter()

trigger = False
received = False
temp = ''

for ip in target_network:
    ip = str(ip)
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
