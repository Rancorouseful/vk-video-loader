import os
from moviepy.editor import VideoFileClip, concatenate_videoclips
import download
from glob import glob

if download.load_videos() == 1:
    videos = glob('*.mp4')
    def glue_videos():
        global videos
        
        print('\nConnecting videos into one...\n')

        clips = []

        for video in videos:
            clips.append(VideoFileClip(video))

        final_clip = concatenate_videoclips(clips, method="compose", )
        final_clip.write_videofile("final_video.mp4", threads=6)

        return 1