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
* intitle:Index.of intext:keystore.jks

Usage
-----
```
Usage: keystorebrute.py [options] arg1 arg2

Options:
  -h, --help            show this help message and exit
  -v, --verbose         Show password being tested [default: False]
  -k FILE, --keystore=FILE
                        Keystore to crack
  -D, --dump-store      If specified, the keystore information will be dumped
                        in the terminal
  -K FILE, --keystore-list=FILE
                        A file with a list of keystores to crack
  -d DICTIONARY, --dictionary=DICTIONARY
                        Dictionary to use in the brute force
```

Output Example
--------------

```
felipe@felipe-sensepost:~/Tools/keystorebruteforce$ ./keystorebrute.py -k tests/keystore.jks -d dictionary.txt  -D
======================================
=      Keystore Brute Force v1.1     =
= Author: Felipe Molina (@felmoltor) =
======================================

====================================================
= Brute forcing keystore file 'tests/keystore.jks' =
====================================================

 [+] Valid password found: changeit

********* BEGIN PRIVATE KEY *********
-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEAtIeMuMitLXprjG2m5qrvHibxnXCU+2bYglsUg146A7Sn2ci2
3QrNSC8K3KE/gEcCMI2MDB4JC3E1CghvXNAfVeadK52OtGlg91lPbGoTmN6RVDOz
eH1XFI9euLSAfHBSSNBzkXLCX7GKWrVKyq6k2m14gelt1uN9SK4L0gJRpSX4uFIP
lvpQ0MJIRHHD4MThKsANpHmXHQgTSXCT8qDY28z19R7Y2ucP8WOHpHSi26vdkI3W
P+D1o6aHxDU1z3wCvxviDyAwrhND9wyd+uTeTIpiRLc5V09WKRwpBRuKeNjg7BDF
cVjt5gfJkMk521WEK3IC+wKMNsf11T2tmTuqzQIDAQABAoIBAFI9Obbn/DQug5Xq
UdDc56dFuGWvZr8L/++KTFL39te/UYOdsugJRrDudTVC46mtL2ss4DKY8CfdP3s9
knWmfc/lCY5X7S10n+6uKcdKn3jRU0UXdFecSbIdCdp8p9eIV4PCKhOFQtTTDSL7
WYHxgznaCr6rtxTgdy9H0iyuT8E6QhVg4COjqPp7751+GSgulld0MZwcaef2MQbP
Lk63ScQFZX3j2y55Z4gBJhkP6YzKRZA2cQWcM+1vIwIH4MQ5vyHUCa7D1DeuhE9v
aAtwzaiEBSWoQD0B5+dAX777KA38xXqy/FAaeYLPIIPwwQmni1SCD0WO/tYq23Oz
7qBg9QUCgYEA3jSzCYwwK8QHZXvldh2Ah5YQNQshADqRWPRBYfTJx82l9Xn/kp8F
dJeuQBao/OY2L0NEYO006vBRB1+wUoM3QGtYmvAYy3MFsHCnMgzlqXLPT5w5fx0O
fnUfVMiTbmUEMBwKR6kyoVPMaJm1hmUWUivvog0Ut68uZkeuCrobKlsCgYEAz/w7
/2RsasdRY7f5uI8pBrSJoLS70z1AsJDqG3ds47wkS+KVG7wGvE7w4cT7kUU7fUjI
/14rPEZA8an+MD0PpNM1UWdwQazeS4XiVbjpaJRUSjeIO4HcKrkExPHP2JEnFx0+
7jAWGJjYoPveMdD67E1FRtKOWL4nu9zU5FH49/cCgYAlql8y3h2IPalXTYIe3G9e
DFTg+Or2I/dhUb4Hgbv2b2iTTMPCscv18IQr/utUOx2yMz/TAkJ3FJdXnaPAyNdD
xy50zQAW9H9hYiclN8RyTbDQeNXSMzWyv924vGspSlxEX2xqq0aWzCKZFH0Ns/Lt
qN7s5DS/0iUWV04sKVHTgwKBgQCZ2c0MA95LMnvbVvlL8+J2SlBQZ8FU5keXFOuI
O9R5te/njomcRX96Bq8bYxpwgJUb/R5qAN/cq19ZJNWaG2EaHP6g4/JfMqARn80o
eit2p9qeN+v3kP0rQUfs469LVTxkVcb6bOm7cj01AHuBwEQNTq+DTzfrH2bHCfkV
mCmiSwKBgB2673zzuzNF3RVyYh3ZHHQ8zB14jEFQOpQYJDqOUYn2SvHfRw4ARHHu
eZTuJ3RgEGOV0lPu2By77DFfRaGdLWF7AhhF5lGj8Ww0gAoceFKZ+vGn4Xe7fBHL
jWgF5kP8KPWHAJmcQe3PxJTIEzntQi7sQTzIEbO5fKrroMzFfR8m
-----END RSA PRIVATE KEY-----
-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEAoKOGvstNxbkZ2jn5KP5PLa550BmUOKXxR3XrpWvLUbagOrQE
7WFI+g9+3KHnPkQ4l+Vq8VdsqL8rstplnS088kwTlxDEfb7z1BPs0rZjk9OCeMbd
eeU/D09z/r+NQK0PlJFwK220FDNbqyY2tMB7HkXpHKopO2K2vb7wlLIDJBVfZH5A
Tp087L2OsAUKGF2Sy67F47BeW2Dd0q2WTihHZGTvTCQoWCdOCmaJE7nTLQr+mzJb
Y23FcuEbz80j035Jlas+CM0nj1UxkNOP8GG7XwcM2vRf1nXYjv1IyzRetKTG4BiB
I0PGbTVOA7DDgPyk+IhgDBL7SA+P0kNXVPg1NQIDAQABAoIBACGlftCxxq12ctrJ
r82NTspTtEIJSYmAAISmR2BTrreD2BXTpQCPkviFjF3sL4JUScJPFFJOrHy/5ghF
RGlik1Rw6N2Ibo+kEnBGaCFOgJbzA24GwVcJ1GaBjts6Bf0ZAp1sxSDjjod4pme3
zleXxXH21LfjUFWW/I3L05phmtTQqujKEXRf62d75YhnPgu3BAx5VhV0k4+qLm39
ZeQQnIZiB/P4pCDfChPxQvhde+tfgUIubdN6J3eF6aIBzfaATNYjWLDkIk6Ubb1q
sg/XbnMR1lx0pGGdNOYWu2rmBepaDp+UUV0AtcFOYmLE+wI+mMN6Iaao3DJO1XuR
gIG32AECgYEA8kWkPZPpGXFC/r0sibzltOeYLgKiozqOX4vvhJx5cWA7Bltddxfy
nGP81tbntauqpLDGLdUKrepLXh7mEbPSYyZ78PGGndZaTJVyKZxn4JSTBMTqbB4o
ptvCWJs+87HIMMdS++NCEbY3k478VDQYXsyEv6RLWizyqJaQ1NXB2zUCgYEAqb25
34xfI4ymM5df7L+O6/sTZNItglrh7uWQUw0vouE5Gle6cBlWYCvXxDj4c/w2P3B/
r2BSz+N+WgyE05FovMg2pvU01gXDtHpRk3yfWAMWB9tZZsNeSTrpTOs/Aw10fGea
hCAFiJcPkBmrniS1q05eR2CNjs7HyplRRT+OMgECgYEA2N8yeNTw8w+Kc1KQjfQE
hH5UoctGH2wJispPbJxNsgn8jGI5NqS/TvPKn97cqKm1JZwAq4Jr/uce9HAgb3RT
PuJyTGtIn/4D805MVadm7YjSWpCTcJlGtqc+P+co4SkiFVg4lrcGq6g78+EpS48e
ya22n37I3T4jMnslxwBaeokCgYAOjkqGNQ9jiQgnnG+JadPjwKAlITDt4MVHK0B5
HsRa/11aOPOv8TxK+veByDDmIVa1kfwhGe2ADk4jgrdRPULyDWlCX/yr7cqei267
axBvB7S378N24IIRXY/sHLBGnrzCfk/tzKEs2WdoQAtLgHJjwlCrZkg9WtYfNY6W
laCoAQKBgBU+hWt4BrYH9kjR71b6Gl7smFoTrKi3Y5wgXYx6SjFqXpyDxV1xzBJF
PPSZgx2jLuqyLt6HXa+gwDkdzud7WGOVB8cXinveZyrwbAsmquE1OpWoZTlT69Hc
CYi5RwgihSr8V8o+TxQHKvNRsWFFYbECTyblBPMBpe/nwgo6B9wF
-----END RSA PRIVATE KEY-----
********* END PRIVATE KEY *********

********* BEGIN PRIVATE KEYS CERTIFICATES *********
-----BEGIN CERTIFICATE-----
MIIDpzCCAo+gAwIBAgIEPpXEljANBgkqhkiG9w0BAQsFADCBgzELMAkGA1UEBhMC
VVMxEzARBgNVBAgTCkNhbGlmb3JuaWExFDASBgNVBAcTC1NhbnRhIENsYXJhMRsw
GQYDVQQKExJPcmFjbGUgQ29ycG9yYXRpb24xEjAQBgNVBAsTCUdsYXNzRmlzaDEY
MBYGA1UEAxMPV0lOLUk4RlNMRTdBM1Q5MB4XDTEyMDkxOTE4Mzg0MFoXDTIyMDkx
NzE4Mzg0MFowgYMxCzAJBgNVBAYTAlVTMRMwEQYDVQQIEwpDYWxpZm9ybmlhMRQw
EgYDVQQHEwtTYW50YSBDbGFyYTEbMBkGA1UEChMST3JhY2xlIENvcnBvcmF0aW9u
MRIwEAYDVQQLEwlHbGFzc0Zpc2gxGDAWBgNVBAMTD1dJTi1JOEZTTEU3QTNUOTCC
ASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAKCjhr7LTcW5Gdo5+Sj+Ty2u
edAZlDil8Ud166Vry1G2oDq0BO1hSPoPftyh5z5EOJflavFXbKi/K7LaZZ0tPPJM
E5cQxH2+89QT7NK2Y5PTgnjG3XnlPw9Pc/6/jUCtD5SRcCtttBQzW6smNrTAex5F
6RyqKTtitr2+8JSyAyQVX2R+QE6dPOy9jrAFChhdksuuxeOwXltg3dKtlk4oR2Rk
70wkKFgnTgpmiRO50y0K/psyW2NtxXLhG8/NI9N+SZWrPgjNJ49VMZDTj/Bhu18H
DNr0X9Z12I79SMs0XrSkxuAYgSNDxm01TgOww4D8pPiIYAwS+0gPj9JDV1T4NTUC
AwEAAaMhMB8wHQYDVR0OBBYEFEMXm315p7JgiUehbAFEo6NNtdQNMA0GCSqGSIb3
DQEBCwUAA4IBAQBYyapwWAriSlxGYdcU1QI6jr1gPoWKyEhT3oJjqUUuxpaLdKWl
kY3Ood6u72nMvPipA1JTFyYD2jR5iBCgWyzfl4ZYr7AQMXZ7WNUvHxoE0imG5931
ZdyBXulWn+sEHE6Pd53voHElrUUxqh4TdwzP8OAksf50WMFHmsaHzuHzdBdtD6lB
Yb2jdUOIXZ82jwe81DNRvGt2w7ZIFSpObOrrLwcU+DDPIE4KkERJBW3vUBq319CD
XVxCYwPBSB2Hbn2nv4sjtzI+hJI0ukoLJfpc7f570wL80ByCZvlL1U5Uzl2Eku5o
/OEop2mqlFE6sb0Y5p1nHKZH59fvclLZldat
-----END CERTIFICATE-----

********* END PRIVATE KEYS CERTIFICATES *********

********* BEGIN KEY STORE CERTIFICATES *********
********* END KEY STORE CERTIFICATES *********

```


