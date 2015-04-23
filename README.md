# Keystore Bruteforce Tool 

Summary
-------
Script to brute force and dictionary attack a Java keystore file.

Required Libraries
------------------

* termcolor (sudo pip install termcolor)
* pyjks     (sudo pip install pyjks)

Google Dorks
------------

To find some .keystores you can use Google Dorks like this:
* intext:"Index of" intext:".keystore"

Usage
-----
```
$ ./keystorebrute.py -h
Usage: keystorebrute.py [options] arg1 arg2

Options:
  -h, --help            show this help message and exit
  -v, --verbose         Show password being tested [default: False]
  -k FILE, --keystore=FILE
                        Keystore to crack
  -K FILE, --keystore-list=FILE
                        A file with a list of keystores to crack
  -d DICTIONARY, --dictionary=DICTIONARY
                        Dictionary to use in the brute force
```

Output Example
--------------

```
$ ./keystorebrute.py -K ks.list -d dictionary.txt
=======================================
Brute forcing keystore file 'keystore1'
=======================================
 + Valid password found! 'changeme'
 Private key: testingbruteforce
 -----BEGIN RSA PRIVATE KEY-----
 AhRhpe/kYnCnCS7qwQGkVWmeJzUxow==
 -----END RSA PRIVATE KEY-----
 -----BEGIN CERTIFICATE-----
 MIIDUjCCAxCgAwIBAgIEfVrbuzALBgcqhkjOOAQDBQAwezELMAkGA1UEBhMCRVMx
 EDAOBgNVBAgTB1Vua25vd24xDzANBgNVBAcMBkph4oCabjETMBEGA1UECgwKQGZl
 bG1vbHRvcjEcMBoGA1UECxMTUGF0YXRhcyBGcml0YXMgUy5hLjEWMBQGA1UEAxMN
 RmVsaXBlIE1vbGluYTAeFw0xNTA0MjMxMTA4NDJaFw0xNTA3MjIxMTA4NDJaMHsx
 CzAJBgNVBAYTAkVTMRAwDgYDVQQIEwdVbmtub3duMQ8wDQYDVQQHDAZKYeKAmm4x
 EzARBgNVBAoMCkBmZWxtb2x0b3IxHDAaBgNVBAsTE1BhdGF0YXMgRnJpdGFzIFMu
 YS4xFjAUBgNVBAMTDUZlbGlwZSBNb2xpbmEwggG3MIIBLAYHKoZIzjgEATCCAR8C
 gYEA/X9TgR11EilS30qcLuzk5/YRt1I870QAwx4/gLZRJmlFXUAiUftZPY1Y+r/F
 9bow9subVWzXgTuAHTRv8mZgt2uZUKWkn5/oBHsQIsJPu6nX/rfGG/g7V+fGqKYV
 DwT7g/bTxR7DAjVUE1oWkTL2dfOuK2HXKu/yIgMZndFIAccCFQCXYFCPFSMLzLKS
 uYKi64QL8Fgc9QKBgQD34aCF1ps93su8q1w2uFe5eZSvu/o66oL5V0wLPQeCZ1FZ
 V4661FlP5nEHEIGAtEkWcSPoTCgWE7fPCTKMyKbhPBZ6i1R8jSjgo64eK7OmdZFu
 o38L+iE1YvH7YnoBJDvMpPG+qFGQiaiD3+Fa5Z8GkotmXoB7VSVkAUw7/s9JKgOB
 hAACgYBGwXz4U3PK2WWjepSKxEUCrnywkwE/s3M/nfO6mVOxVTlU/yTxpx9ZbH52
 lsJE7lLj2Ra6+vudW5OajZEK1SR50DhNqIftQIAY9/jPQ9T1kf9bJBR4uap4oZde
 yg7PdTM2cSpDoQWo5ovchDWetJnXyr0EuaVDtM+m4z9ikeaN/aMhMB8wHQYDVR0O
 BBYEFAymjaLgT35el+noW6y79B9V2roAMAsGByqGSM44BAMFAAMvADAsAhQ/3ghZ
 V/aa8IFRoTi7rZD7YJ2QDQIUTjrJDrBd4n2TmYPeX4KSsdgqHTg=
 -----END CERTIFICATE-----


 =======================================
 Brute forcing keystore file 'keystore2'
 =======================================
  + Valid password found! '1q2w3e'
  Private key: keystore2
  -----BEGIN RSA PRIVATE KEY-----
  AhRQqDK3wBOU/nEQhX6G6oVdM50jVw==
  -----END RSA PRIVATE KEY-----
  -----BEGIN CERTIFICATE-----
  MIIDYjCCAyCgAwIBAgIEFTDItjALBgcqhkjOOAQDBQAwgYIxCzAJBgNVBAYTAkVT
  MRAwDgYDVQQIEwdVbmtub3duMRYwFAYDVQQHDA1KYeKAmm4vTWFkcmlkMRMwEQYD
  VQQKDApAZmVsbW9sdG9yMRwwGgYDVQQLExNQYXRhdGFzIEZyaXRhcyBTLkEuMRYw
  FAYDVQQDEw1GZWxpcGUgTW9saW5hMB4XDTE1MDQyMzExMTYwMFoXDTE1MDcyMjEx
  MTYwMFowgYIxCzAJBgNVBAYTAkVTMRAwDgYDVQQIEwdVbmtub3duMRYwFAYDVQQH
  DA1KYeKAmm4vTWFkcmlkMRMwEQYDVQQKDApAZmVsbW9sdG9yMRwwGgYDVQQLExNQ
  YXRhdGFzIEZyaXRhcyBTLkEuMRYwFAYDVQQDEw1GZWxpcGUgTW9saW5hMIIBtzCC
  ASwGByqGSM44BAEwggEfAoGBAP1/U4EddRIpUt9KnC7s5Of2EbdSPO9EAMMeP4C2
  USZpRV1AIlH7WT2NWPq/xfW6MPbLm1Vs14E7gB00b/JmYLdrmVClpJ+f6AR7ECLC
  T7up1/63xhv4O1fnxqimFQ8E+4P208UewwI1VBNaFpEy9nXzrith1yrv8iIDGZ3R
  SAHHAhUAl2BQjxUjC8yykrmCouuEC/BYHPUCgYEA9+GghdabPd7LvKtcNrhXuXmU
  r7v6OuqC+VdMCz0HgmdRWVeOutRZT+ZxBxCBgLRJFnEj6EwoFhO3zwkyjMim4TwW
  eotUfI0o4KOuHiuzpnWRbqN/C/ohNWLx+2J6ASQ7zKTxvqhRkImog9/hWuWfBpKL
  Zl6Ae1UlZAFMO/7PSSoDgYQAAoGAIv/DxXWLbbRbTzov8Z7gtHrXZwTUnEXrDzdF
  1kccPZD0xv3GuaaPYOTKz0btmPtrpbL8z7vC03T/GsvcciEEQrCyRonZAw/hK9F8
  rVNTLwqQh6xkily0BYYruma9yp/nArj6RZf6ctzAqI4l2sltTvMeSmrp+0OHUXhT
  arlJ+fqjITAfMB0GA1UdDgQWBBSr5+z5+OWIxOY69ODgnRkaGz3fyjALBgcqhkjO
  OAQDBQADLwAwLAIUXCu6ktSNioOmUCvUXH9tprGCQawCFCKmFt9/IIvm+vLhq16T
  rjSQCEDi
  -----END CERTIFICATE-----

```

