#!/usr/bin/env python

from __future__ import print_function
import sys
import argparse
import codecs
import getpass
import hashlib

def wdc(password):
    password = "WDC." + password
    password = password.encode("utf-16")[2:]
    for _ in range(1000):
        password = hashlib.sha256(password).digest()
    return password

def hdparm(password):
    if password == 'NULL':
        password = ''
    return password.ljust(32, '\0').encode('ascii')

def generate_password(password, cook_method, cmd):
    password = cook_method(password)

    if cmd == 'unlock':
        field = b'00'
    else:
        password = password + password
        if cmd == 'unset':
            field = b'10'
        if cmd == 'set':
            field = b'01'

    header = b'450000' + field + b'00000020'
    header = codecs.decode(header, 'hex')

    return header + password

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("passwd", type=str, nargs='?')
    parser.add_argument("--hdparm", action="store_true")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--unset", action="store_true")
    group.add_argument("--set", action="store_true")

    args = parser.parse_args()

    if args.hdparm:
        if len(args.passwd) > 32:
            sys.exit('Password length cannot be larger than 32!')
        method = hdparm
    else:
        method = wdc
        passwd = args.passwd or getpass.getpass('My Book password: ')

    if args.unset:
        cmd = 'unset'
    elif args.set:
        cmd = 'set'
    else:
        cmd = 'unlock'

    password = generate_password(passwd, method, cmd)

    out = getattr(sys.stdout, 'buffer', sys.stdout)
    out.write(password)

if __name__ == '__main__':
    main()
