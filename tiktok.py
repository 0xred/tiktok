import requests
from bs4 import BeautifulSoup
import re
headers = requests.utils.default_headers()
headers.update({
    'User-Agent': 'Mozilla/5.0 (X22; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
})

usr =input(" add user with @ :")
url = 'https://www.tiktok.com/%s'% usr+'?lang=en'
res = requests.get(url ,headers=headers)
html_page = res.content
soup = BeautifulSoup(html_page, 'html.parser')
text = soup.find_all(text=True)

output = ''
whitelist = [
    'title',

    # there may be more elements you don't want, such as "style", etc.
]

for t in text:
    if t.parent.name in whitelist:
        output += '{} '.format(t)

print(output)
if usr in output:
    print(" yessssssssssssss i found user")
else: print(" NOOOOOOOOOOOOOOOOOO i dont found user")