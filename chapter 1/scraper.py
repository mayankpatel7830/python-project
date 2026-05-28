import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"
response = requests.get(url)

soup = BeautifulSoup(response.text,"html.parser")

quotes = soup.find_all("div" , class_="quote")

data = []

for q in quotes:
    text = q.find("span",class_="text").text
    author = q.find("small",class_="author").text

    data.append({"text": text, "author": author})

for item in data:
    print(f"{item['author']} said: {item['text']}")


import csv

with open("quotes.cvs", "w" , 
          newline="" , encoding="utf-8") as file: 
          writer = csv.DictWriter(file,fieldnames=["text","author"])

          writer.writeheader()
          writer.writerows(data)