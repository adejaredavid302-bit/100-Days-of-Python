import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(URL)
web_page=response.text
soup=BeautifulSoup(web_page,"html.parser")
links=soup.find_all(name="h3",class_="title")
movies=[link.getText() for link in links]
movies=movies[::-1]

content="\n".join(movies)
print(content)
with open("movies.txt","w", encoding="utf-8") as file:
    file.write(content)
