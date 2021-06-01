
try:
    import requests
    from bs4 import BeautifulSoup
    import sys
    import os
    from colorama import Fore, Back, Style
except Exception as lib:
        print(lib)
        input()
        sys.exit()


os.system('cls' if os.name == 'nt' else 'clear')
os.system("color B")
print("""
==================================
   Tiktok Chacker user
==================================
  add user list in user.txt
""")
 
try:
    file = open(f"user.txt", "r")
except:
    print("No File Named user.txt ")
    input()
    sys.exit()
 
input("[+] Press Enter To Start ..")

while True:
 
    user = file.readline().split("\n")[0]
    if user == "":
        input()
        sys.exit()
    try:
        headers = requests.utils.default_headers()
        headers.update({
            'User-Agent': 'Mozilla/5.0 (X22; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
        })

        url = 'https://www.tiktok.com/%s'% user+'?lang=en'
        res = requests.get(url ,headers=headers)
        html_page = res.content
        soup = BeautifulSoup(html_page, 'html.parser')
        text = soup.find_all(text=True)

        output = ''
        whitelist = [
            'title',

        ]

        for t in text:
            if t.parent.name in whitelist:
                output += '{} '.format(t)


        if user in output:
            print(Fore.RED+f"NOT Available --> {user}")
        else: print(Fore.GREEN+f"Available --> {user}")
    except:
        print(" have good day bro :)")
