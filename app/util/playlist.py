import get_connection
import json
from ..dao.video import Video

def populate():
    videos = Video().all_for_jwplayer()
    list = []
    for video in videos:
        video_obj = {}
        for key in video.keys():
            video_obj.update({ key: video[key] })
        levels = [
            { "file": video['file'] },
            { "file": video['file']+".webm" }
        ]
        video_obj.update( { "levels": levels } )
        video_obj.update( { "image": video['thumbnail'] } )
        video_obj.pop('file')
        print video_obj
        list.append(video_obj)
    return json.dumps(list, indent = 2)
