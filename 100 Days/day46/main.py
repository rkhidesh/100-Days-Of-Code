from  bs4 import BeautifulSoup
import  requests
year = input("Which year do you want to travel to? Type the date in this format YYYY-MM-D: ")
url = "https://www.billboard.com/charts/hot-100/2000-08-12/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")
the_list_songs = soup.select("li h3")
billboard_song_list = [the_list_songs[num].getText().strip() for num in range(0, 100)]

print(billboard_song_list)