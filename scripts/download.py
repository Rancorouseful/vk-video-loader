import get_links
import youtube_dl

ydl_opts = {}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    def load_videos():
        print('\nDownloading:\n')
        for link in get_links.links:
            ydl.download([link])
        return 1