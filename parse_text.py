# -*- coding: utf-8 -*-
"""
Created on Thu May 21 12:46:00 2020

@author: zuzan
"""
from requests import get
from bs4 import BeautifulSoup
import io

def parse_lyrics(song_link):
  response = get(song_link)
  html_soup = BeautifulSoup(response.text, 'html.parser')
  lyrics = html_soup.find_all('p')
  song = []
  for paragraph in lyrics:
    paragraph = str(paragraph).replace("<br/>", "\s").replace("</p>", "").replace("<p>", "").replace("!", "")
    song.append(paragraph)
    #song.append(paragraph.get_text())
  del song[-2:]
  song = '\n'.join(song)
  return song

print("Connect with URL...")

url = 'https://www.nickcave.com/lyrics/'
response = get(url)

html_soup = BeautifulSoup(response.text, 'html.parser')
albums = html_soup.find_all('div', class_ = 'lyric-album-list')
print(f'Number of available albums: {len(albums)}')


file  = io.open("songs.txt", "w", encoding="utf-8") 

print('Parse text...')

no_songs = 0

for album in albums:
  songs = album.find_all('a')
  for song in songs:
    song_link = song.get('href')
    file.write(parse_lyrics(song_link)+'\s')
    no_songs += 1

print(f"No. of downloaded songs: {no_songs}")

file.close()

print(f"'Songs.txt' file succesfully created!")