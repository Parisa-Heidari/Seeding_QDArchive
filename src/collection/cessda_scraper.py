import requests
from bs4 import BeautifulSoup

url = "https://datacatalogue.cessda.eu/?query=qualitative"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

print(soup.title)
