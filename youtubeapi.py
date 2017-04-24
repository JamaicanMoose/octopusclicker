#!/usr/bin/python

from googleapiclient.discovery import build
from googleapiclient.http import HttpRequest
import httplib2
# from oauth2client.client import GoogleCredentials


DEVELOPER_KEY = 'AIzaSyCH4TfJsRocyaeigtVXW36M4J68Hg2fDnM'
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

'''
search_videos = []
youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)
'''

# credentials = GoogleCredentials.get_application_default()


def build_request():
    new_http = httplib2.Http()
    return HttpRequest(new_http)


def youtube_search(query, before, after):
    search_videos = []
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

    http = httplib2.Http()

    search_response = youtube.search().list(
        q=query,
        part="id",
        order="date",
        type="video",
        publishedAfter=after,
        publishedBefore=before,
        maxResults='50',
        ).execute(http=http)

    # Merge video ids
    for search_result in search_response.get("items", []):
        search_videos.append(search_result["id"]["videoId"])

    video_ids = ",".join(search_videos)
    video_response = youtube.videos().list(
        id=video_ids,
        part='snippet'
    ).execute()

    videos = []

    for video_result in video_response.get("items", []):
        videos.append("%s" % (video_result["snippet"]["description"]))

    return videos
