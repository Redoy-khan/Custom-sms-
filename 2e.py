import requests
import os

os.system('pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requests bs4')
os.system('clear')
    
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
