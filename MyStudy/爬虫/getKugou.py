import requests as re
from bs4 import BeautifulSoup
r=re.get("https://kugou.com")

t=BeautifulSoup(r.text).get_text()
print(t)
input()
