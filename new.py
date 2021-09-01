from mechanize import Browser
from os import read, write
import os
import sys
import io
import random
import http.cookiejar as cookielib
import mechanize
from bs4 import BeautifulSoup
from colorama import init, Fore, Back, Style
init(convert=True)
######################################################################
os.system('cls')
print(Fore.MAGENTA+"""
      .---.        .-----------
     /     \  __  /    ------
    / /     \(  )/    -----
   //////   ' \/ `   ---        .----------------------------------.
  //// / // :    : ---          | Tiktok User Checker By RedShadow |
 // /   /  /`    '--            '----------------------------------'
//          //..\\
       ====UU====UU====
           '//||\\`
             ''``
""")
######################################################################
brows = Browser()
brows.set_handle_robots(False)
brows._factory.is_html = True
brows.set_cookiejar(cookielib.LWPCookieJar())
useragents = [
           'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.19) Gecko/20081202 Firefox (Debian-2.0.0.19-0etch1)',
           'Opera/9.80 (J2ME/MIDP; Opera Mini/9.80 (S60; SymbOS; Opera Mobi/23.348; U; en) Presto/2.5.25 Version/10.54',
           'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11',
           'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.6 (KHTML, like Gecko) Chrome/16.0.897.0 Safari/535.6']
brows.addheaders = [('User-agent',random.choice(useragents))]
brows.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)

def tiktok():
    file = open("user.txt", "r")
    input("[+] Press Enter To Start ..")
    while True:
        
        user = file.readline().split("\n")[0]
        if user == "":
            print(Fore.MAGENTA +"[+] finish ....")
            sys.exit()
        try:
            try_login = 0
            url = f"https://www.tiktok.com/@{user}?lang=en"
            try:
                brows.open(url)
                brows.select_form(nr=0)
                brows.method = "POST"
                submit = brows.submit()
                ############## using BeautifulSoup ##############
                soup = BeautifulSoup(submit.get_data(), 'html.parser')
                text = soup.find_all(text=True)

                output = ''
                whitelist = [
                    'title',

                ]

                for t in text:
                    if t.parent.name in whitelist:
                        output += '{} '.format(t)
                ############## using BeautifulSoup ##############
                
                print(Fore.WHITE+"[+]"+Fore.RED +" not available "+Fore.WHITE+user)
            except:
                print(Fore.WHITE+"[+]"+Fore.GREEN +" available "+Fore.WHITE+user)
                Save = io.open("usertiktok.txt","a").write(f"Account:{user}\n")
        except:print(" try agin")

tiktok()

