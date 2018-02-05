import requests
from bs4 import BeautifulSoup

url = "https://www.researchgate.net/institution/PES_Institute_of_Technology/members"
#url = "https://scholar.google.gr/citations?user=aFYdVoYAAAAJ&hl=el&view_op=citations_histogram"
r = requests.get(url)
#print r.content

soup = BeautifulSoup(r.content,"lxml")
#unicode_str = r.decode("utf-8")
#encoded_str = unicode_str.encode("ascii",'ignore')
#soup = BeautifulSoup(encoded_str,"html.parser")

links = soup.find_all("html")

print links
