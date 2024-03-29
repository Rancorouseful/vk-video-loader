import vk_api
import scripts.config as config

session = vk_api.VkApi(token=config.TOKEN)
vk = session.get_api()

groups = config.groups

def get_group_videos_links(groups):

    fl = open('used_links.txt', 'r+')
    fl_owner_if_video_id = fl.read().split(', ')
    groups_id = {}
    groups_info = session.method('groups.getById', {'group_ids': str(', '.join(groups))})

    # get ids by goups' names
    for i in range(len(groups_info)):
        groups_id[groups_info[i]['id']] = groups[i]

        # get videoposts from groups' wall by gpoups'`ids
        groups_videos_ids = []
        for group_id in groups_id:
            wall = session.method('wall.get', {'owner_id': int('-' + str(group_id)),'offset': 0, 'count': 30, 'filter': 'owner','extended': 1}) # get posts from goup's wall
            
            for i in range(len(wall['items'])):
                if len(wall['items'][i]['attachments']) != 0:
                    if wall['items'][i]['attachments'][0]['type']=='video':
                        owner_id = str(wall['items'][i]['attachments'][0]['video']['owner_id'])
                        video_id = str(wall['items'][i]['attachments'][0]['video']['id'])
                        access_key = str(wall['items'][i]['attachments'][0]['video'])
                        if owner_id + '_' + video_id not in fl_owner_if_video_id:
                            fl.write(owner_id + '_' + video_id + ', ')
                            groups_videos_ids.append(owner_id + '_' + video_id + '_' + access_key)
                            print(owner_id + '_' + video_id + '_' + access_key + ' added.')
                        else:
                            print(owner_id + '_' + video_id + '_' + access_key + ' already in used_links.')

        videos = session.method('video.get', {'videos': ','.join(groups_videos_ids)})
        player_links = []

        for i in range(len(videos['items'])):
            player_links.append(videos['items'][i]['player'])
            print(videos['items'][i]['player'])

        fl.close()
        return(player_links)


links = get_group_videos_links(groups)
