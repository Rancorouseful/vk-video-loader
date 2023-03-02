import main
import youtube_dl

ydl_opts = {}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    def load_videos():
        for link in main.links:
            ydl.download([link])
        return 1