from re import search
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth2client.tools import argparser
import pandas as pd 
import datetime

#edit with generated api key 
API_KEY='######################################'
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

argparser.add_argument("--q", help="Search term", default="#EndSars")
argparser.add_argument("--video-duration", help="Video duration", default="medium")
argparser.add_argument("--published-after", help="Published after", default="2021-01-01T00:00:00Z")
argparser.add_argument("--max-results", help="Max results", default=50)

args = argparser.parse_args()
options = args

youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=API_KEY)

#searching youtube for videos
search_response = youtube.search().list(
 q=options.q,
 videoDuration=options.video_duration,
 publishedAfter=options.published_after,
 type="video",
 part="id,snippet",
 maxResults=options.max_results
).execute()

#print(search_response.get("items", [1])[0]['snippet']['thumbnails']['default']['url'])



#print(search_response)
allVideos=[]

#stores info needed from video in a key, value pair dictionayr
for search_result in search_response.get("items", []):
    video = {}
    if search_result["id"]["kind"] == "youtube#video":
        video['videoId'] = search_result["id"]["videoId"]
        video['videoTitle'] = search_result["snippet"]["title"]
        video['videoDescription'] = search_result['snippet']['description']
        video['videoUrl'] = "https://www.youtube.com/watch?v="+search_result["id"]["videoId"]
        
        #extracting time from date time object
        videoPublishedTime = datetime.datetime.strptime(search_result['snippet']['publishedAt'],"%Y-%m-%dT%H:%M:%SZ")
        new_format_time = "%H:%M:%S"
        video['videoPublishedTime'] = videoPublishedTime.strftime(new_format_time)

    #each dictionary is appended into the list
    allVideos.append(video)
    
 #list of dictionaries is converted into a data frame
videos_df=pd.DataFrame(allVideos)
#print(videos_df)

#keys = ','.join(videos.keys())

#getting video stats

def get_stats(row):
    videos_list_response = youtube.videos().list(
    id=row['videoId'],
    part='id,statistics'
    ).execute()

    #print(videos_list_response)
    
    #checks to see if object is present in json
    stats_keys=['viewCount','likeCount','dislikeCount','favoriteCount','commentCount']
    for item in videos_list_response.get("items", []):
        for key in stats_keys:
            if 'statistics' in item:
                if key in item['statistics']:
                    row[key]=item['statistics'][key]
                else:
                    row[key]=0

                          
    return row
#updating dataframe with video statistics
videos_df=videos_df.apply(get_stats,axis=1)

print(videos_df)
print(videos_df.columns)

# # #generating csv file
#csv file is saved with the time stamp from when the script was run
new_format_time_2 = "%d-%m-%Y_%H-%M-%S"
script_time = datetime.datetime.now().strftime(new_format_time_2)

csv_name= f"C:/Users/USER/Desktop/{str(script_time)}_youtube_data.csv"
videos_df.to_csv(path_or_buf=csv_name,header=True)












