from bs4 import BeautifulSoup
import requests

url = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

movie_tags = soup.find_all(name="h3")

with open("top_100_movies.txt", mode="w", encoding="utf-8") as file:
    file.write("Empire's 100 Best Movies of All Time:\n\n")
    for i, tag in enumerate(reversed(movie_tags), start=1):
        file.write(f"{tag.text}\n")

print("Done!")
