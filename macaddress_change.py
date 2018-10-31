#!/usr/bin/python3

import sys
import os


def error():
    print(
        'Usage : macaddress_change.py dev macaddress \n' +
        'Exemple: macaddress_change.py enp5s0 fa:ca:da:01:02:03'
    )
    exit(1)


try:
    interface = sys.argv[1]
    new_mac = sys.argv[2]
    if len(sys.argv) > 3:
        hostname = sys.argv[3]
    else:
        hostname = None
except IndexError:
    error()

if len(new_mac) == 17:
    cmd = os.system('ip link set dev {} address {}'.format(interface, new_mac))
    if cmd == 256:
        print('Invalid mac address!')
    elif cmd == 512:
        print('Operation no permitted!')
        exit(1)
else:
    error()

if hostname:
    cmd = os.system('hostname {}'.format(hostname))
    if cmd:
        print('Invalid hostname')
