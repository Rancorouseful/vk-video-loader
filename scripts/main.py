import json
import os
import glue

with open('video_data.json', encoding='utf-8') as json_file:
    if glue.glue_videos() == 1:
        data = json.load(json_file)
        os.system(f'''
        cd scripts & python upload_video.py 
        --file="{0}" 
        --title={1}  
        --description={2} 
        --keywords={3} 
        --category={4} 
        --privacyStatus={5}'''.format(
            data['file'],
            data['title']+str(data["part"]),
            data['description'],
            data['keywords'],
            data['category'],
            data['privacyStatus']
        ))
        
        data["part"] = data["part"]+1
        json.dump(json_file, data)

        print('\nDeleting single videos...\n')
        for video in glue.videos:
            os.remove(video)
            print(video + ' deleted')
        
