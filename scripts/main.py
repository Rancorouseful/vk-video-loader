import json
import os
import glue

with open('video_data.json', 'r', encoding='utf-8') as file:
    if glue.glue_videos() == 1:
        data = json.load(file)
        try:
            os.system('''cd scripts & python upload_video.py --file="{0}" --title="{1}" --description="{2}" --keywords="{3}" --category="{4}" --privacyStatus="{5}"'''.format(
                os.path.abspath(data['file']),
                data['title']+str(data["part"]),
                data['description'],
                data['keywords'],
                data['category'],
                data['privacyStatus']
            ))

            data["part"] = data["part"]+1
            
            data = json.dumps(data, indent = 7)

            file.close()

            file = open("video_data.json","w") 
            file.write(str(data))
            file.close()

            print('\nDeleting single videos...\n')
            for video in glue.videos:
                os.remove(video)
                glue.videos.remove(video)
                print(video + ' deleted')
        except:
            print('ERROR')
