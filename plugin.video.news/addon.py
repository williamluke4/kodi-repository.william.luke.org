'''
    Youtube Live News Kodi Addon
    ~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2013 by William Luke
    :license: GPLv3, see LICENSE.txt for more details.
'''
import xbmcswift2
from xbmcswift2 import xbmc
import requests

ONE_HOUR_IN_MINUTES = 60
YOUTUBE_URL = 'plugin://plugin.video.youtube/?action=play_video&videoid=%s'
plugin = xbmcswift2.Plugin()
addon_id = plugin._addon.getAddonInfo('id')

def get_icon_path(name):
    icon_path = 'special://home/addons/%s/resources/images/%s' % (addon_id, name)
    return icon_path 


links = [
    {
    
     'title': 'Al Jazeera English',
     'thumbnail': get_icon_path('aljazeera.jpg'),
     'description': 'Al Jazeera English' 
     },
      {
    
     'title': 'CNN',
     'thumbnail': get_icon_path('cnn.jpg'),
     'description': 'CNN' 
     },
     {
    
     'title': 'KTN',
     'thumbnail': get_icon_path('ktn.jpg'),
     'description': 'KTN News is a leading 24-hour TV channel in Eastern Africa with its headquarters located along Mombasa Road, at Standard Group Centre. This is the most authoritative news channel in Kenya and beyond.' 
     },
     {
    
     'title': 'CitizenTV',
     'thumbnail': get_icon_path('citizenTV.jpg'),
     'description': 'CITIZEN TV is the No.1 TV station commanding a total reach of 90% \and over 12 years in existence as pioneer brand for RMS Footprint with largest coverage and reach (country wide) covers all socioeconomic grouping speaks to all ages all gender.' 
     },
     {
    
     'title': 'NTV',
     'thumbnail': get_icon_path('ntv.jpg'),
     'description': 'NTV Kenya is the leading television broadcasting station covering a large part of Kenya and the region.' 
     }
]

# @plugin.cached(TTL=ONE_HOUR_IN_MINUTES)
# def get_khan_data():
#     '''A wrapper method that exists to cache the results of the remote API
#     calls.
#     '''
#     return khan.load_topic_tree()


def get_playable_url(search_string):
    eventType = "live"
    itemType="video"
    payload = {
        'q': search_string, 
        'eventType': eventType,
        'type': itemType, 
        'maxResults': '1', 
        'part': 'snippet', 
        'key': 'AIzaSyACUn-ggjDQ7Pq9fPoPmVA00w-umQu3VWY'
    }
    r = requests.get('https://www.googleapis.com/youtube/v3/search', payload)
    data = r.json()
    logger(data)
    youtube_video_id = data["items"][0]["id"]["videoId"]

    return YOUTUBE_URL % youtube_video_id

def logger(message):
    xbmc.log("Kodi-News: "+ str(message))



def to_listitem(item):
    return {
        'label': item['title'],
        'path': get_playable_url(item['title']),
        'is_playable': True,
        'thumbnail': item['thumbnail'],
        'info': {
            'plot': item['description'],
        },
    }
    


@plugin.route('/')
def main_menu(topic='root'):
    '''The one and only view which displays topics hierarchically.'''
    return [to_listitem(link) for link in links]


if __name__ == '__main__':
    plugin.run()
