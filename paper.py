import requests
from bs4 import BeautifulSoup
import re

url = "https://www.researchgate.net/profile/Pooja_Agarwal21"

r = requests.get(url)

soup = BeautifulSoup(r.content,"lxml")

link = soup.find_all("html")

file = open('papers.txt','w')
y = str(link)
file.write(y)
file.close()

file = open('papers.txt','r')
g = file.read()
i=0
a = []
for m in re.finditer('<span><a class="nova-e-link nova-e-link--color-inherit nova-e-link--theme-bare" href=',g):
    a.append(m.end())
str1 = []
s = []
file.seek(a[0]+1)
i = a[0]+1
#ch = file.read(65)
#print ch
ch = file.read(1)
s.append(ch)
names = []
str1 = []
for k in a:
    i = k+1
    ch = file.read(1)
    str1 = ''
    while (ch!='\"'):
        i=i+1
        file.seek(i)
        ch = file.read(1)
        if ch=='\"':
            break
        else:
            s.append(ch)
            str1 = ''.join(s)
    names.append(str1)

file.close()
print str1
print names
print len(names)



