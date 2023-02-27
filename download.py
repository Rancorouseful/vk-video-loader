import main
import youtube_dl

ydl_opts = {}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    for link in main.links:
        ydl.download([link])