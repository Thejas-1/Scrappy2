import requests
from bs4 import BeautifulSoup

url = "https://www.researchgate.net/institution/PES_Institute_of_Technology/members"

r = requests.get(url)

soup = BeautifulSoup(r.content,'lxml')

links = soup.find_all("div")

print links
