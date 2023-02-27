from os import listdir, remove
from pathlib import Path
from moviepy.editor import VideoFileClip, concatenate_videoclips

files = listdir()
videos = []

for file in files:
    if file.endswith('.mp4'):
        videos.append(file)

clips = []

for video in videos:
    clips.append(VideoFileClip(video))

final_clip = concatenate_videoclips(clips, method="compose")
final_clip.write_videofile("final_video.mp4")

for video in videos:
    remove(video)