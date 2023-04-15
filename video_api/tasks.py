import requests
import pprint
from datetime import datetime, timedelta
from django_celery_beat.models import PeriodicTask
from main import celery_app, YOUTUBE_DATA_API_KEYS
from .models import Video

def send_alert_to_dev():
    pass

def fetch_videos(api_key):
    last_5_minutes = datetime.now() - timedelta(minutes = 5)
    formatted_time = datetime.strftime(last_5_minutes, '%Y-%m-%dT%H:%M:%SZ')
    search_url = 'https://www.googleapis.com/youtube/v3/search'
    search_params = {
        'part' : 'snippet',
        'q' : 'surfing',
        'key' : api_key,
        'maxResults' : 25,
        'type' : 'video',
        'order' :'date',
        'publishedAfter' : formatted_time
    }
    return requests.get(search_url, params=search_params).json()


@celery_app.task(bind=True)
def fetch_and_save_videos(*args):
    for i in YOUTUBE_DATA_API_KEYS:
        r = fetch_videos(i)
        if not r.get('error'):
            break
    else:
        task = PeriodicTask.objects.filter(name="Get Videos").first()
        if task:
            task.enabled = False
            task.save()
        send_alert_to_dev()
        raise Exception("All API Keys Exhausted")

    results = r['items']

    date_format = '%Y-%m-%dT%H:%M:%SZ'
    for result in results:
        data = {
            'video_id': result['id']['videoId'],
            'video_title': result['snippet']['title'],
            'channel_id': result['snippet']['channelId'],
            'channel_title': result['snippet']['channelTitle'],
            'description': result['snippet']['description'],
            'published_at': datetime.strptime(result['snippet']['publishedAt'], date_format),
            'thumbnail': result['snippet']['thumbnails']['medium']['url']
        }
        Video.objects.get_or_create(**data)