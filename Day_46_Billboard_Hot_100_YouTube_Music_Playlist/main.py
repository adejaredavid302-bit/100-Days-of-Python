import requests
from bs4 import BeautifulSoup
from ytmusicapi import YTMusic
from ytmusicapi.auth.browser import setup_browser

from header import raw

raw_headers=raw

setup_browser(filepath="browser.json", headers_raw=raw)
print("SUCCESS: browser.json file built successfully!")

date = input("Which year do you want to? Type the date in the format YYYY-MM-DD: \n")
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36"}

URL = f"https://appbrewery.github.io/bakeboard-hot-100/{date}/"
response = requests.get(URL, headers=header)
webpage = response.text
soup = BeautifulSoup(webpage, "html.parser")
webpage_title = soup.select("h3.chart-entry__title")
music_list= [music.getText().strip() for music in webpage_title]


yt = YTMusic("browser.json")
playlists = yt.get_library_playlists(limit=100)
#print(f"{len(playlists)} playlists found")
playlists_name=f"{date} Billboard Hot 100 Music"
playlist_id=None
for playlist in playlists:
    if playlist["title"] == playlists_name:
        playlist_id=playlist["playlistId"]
        break
if playlist_id:
    print("playlist already exists!")

else:
    playlist_id=yt.create_playlist(
        title=playlists_name,
        description="Automated archival compilation scraped from Billboard",
        privacy_status="PRIVATE"
    )
    print(f"Created playlist: {playlist_id}!")

for song in music_list:
    try:
        search_results = yt.search(song, filter="songs", limit=1)
        yt.add_playlist_items(playlist_id, [search_results[0]["videoId"]])
        print(f"Added: {song}")
    except Exception as exception:
        print(f"Skipped: {song} | Reason: {exception}")