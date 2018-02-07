import requests
from bs4 import BeautifulSoup

url = "https://www.researchgate.net/profile/Chiraag"

r = requests.get(url)

soup = BeautifulSoup(r.content,"lxml")

link = soup.find_all("html")
print link
