import os
from moviepy.editor import VideoFileClip, concatenate_videoclips
import download

if download.load_videos() == 1:

    print('\nConnecting videos into one...\n')

    videos = []

    files = os.listdir()
    
    for file in files:
        if file.endswith('.mp4'):
            videos.append(file)

    clips = []

    for video in videos:
        clips.append(VideoFileClip(video))

    final_clip = concatenate_videoclips(clips, method="compose")
    final_clip.write_videofile("final_video.mp4")

    # print('\nDeleting single videos...\n')
    # for video in videos:
    #     os.remove(video)
    #     print(video + ' deleted')