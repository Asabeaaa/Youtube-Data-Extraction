# Youtube Data Extractor
## Project Overview
This script extracts YouTube data in relation to the #endsars# trend that rocked the entire world in Nigeria in 2020. When this python script is run it makes a call to the Youtube Api and returns a list of videos with the hashtag #EndSars in it's title or description,  converts the information we need which is stored in json objects into a dataframe and then stores the output in a csv file.

###### Libraries to import
- from googleapiclient.discovery import build
- from googleapiclient.errors import HttpError
- from oauth2client.tools import argparser
- import pandas as pd
- import datetime

###### Project was divided into 3 parts:
1. Using Google Developers Console to get api Key 
2. Filter youtube for the type of data(video, channels, playlists) you want and other specifics like duration, year posted, how many videos you want returned, etc
3. Get statistics asscociated with those videos, eg; number of likes, dislikes, views, etc

## Code and Resources used 
###### Resources 
1. YouTube API source: https://developers.google.com/youtube/v3/getting-started 
2. Understanding how to use Youtube API: https://www.analyticsvidhya.com/blog/2014/09/mining-youtube-python-social-media-analysis/

## Activities done 
1. Using Google Developers Console

- Steps to follow to get Youtube api key;
1. Launch Google Developers Console (url= https://console.developers.google.com)
2. Click on ENABLE APIS AND SERVICES ( this can be found at the top of the site)
3. Next you search for youtube and select Youtube Data Api v3 (this is an API that provides access to YouTube data, such as videos, playlists, channels)
4. Then you select enable this api (you are redirected to an overview page of the youtube api)
5. Next select the credentials tab( this is found on the left hand side of the page)
6. Select create credential ( found on the top part of the site), 
7. After select create api key,key is created and you can copy it.

After the following steps your key is ready for use to make api calls.

######  Passing credentials into python script

###### ![Capture6](https://user-images.githubusercontent.com/65185008/120343032-350b5d00-c2ad-11eb-803f-f055463706f2.PNG)
###### ![Capture2](https://user-images.githubusercontent.com/65185008/120339166-ba8d0e00-c2a9-11eb-83bf-4c30913c007e.PNG)

2. Filter youtube for the type of data you want, year data was uploaded and the number of videos you want to return

![Capture9](https://user-images.githubusercontent.com/65185008/120348009-9fbe9780-c2b1-11eb-84b4-4566c9b7190c.PNG)
- passing requirements needed for filtering data as an argument
###### Arguments
- -q, --query : Specify the search query. The default value is '#endsars'.
- --video-duration, --video_duration : Specify the length of video you want.
- --published-after, --published_after : Specify a date to filter the search results from. The default value is 01-01-2021.
- --max-results, --max_results : Specify how many items to include the search results. The allowed input should be an integer from 0 to 50. The default value is 50.

###### Options (inputs for video duration) :
1. any: Any video length.
2. short: Videos length between 0 and 4 minutes.
3. medium: Video length between 4 and 20 minutes (inclusive).
4. long: Video length greater than 20 minutes.

###### Passing arguments into youtube search method
![Capture4](https://user-images.githubusercontent.com/65185008/120342027-4142ea80-c2ac-11eb-879d-7731f8e2eb55.PNG)
   - result is a json file that contains different objects that describe the video you have extracted, such as, video id, date uploaded,title of the video, etc. You can retrieve objects needed for your task

3. Get statistics asscociated with those video
###### ![Capture7](https://user-images.githubusercontent.com/65185008/120343751-d397be00-c2ad-11eb-9881-5f6dc157ca94.PNG)
By taking the ids of the videos extracted from youtube , you can generate the statistics associated with these videos by passing the ids into the youtube api videos method and specifying you want the statistics. Some stats you can generate are; the view count, likes count, number of dislikes, number of favourites, etc.


## Output
###### Final dataframe is stored into a csv with the filename having the following format: current_timestamp_youtube_data.
the current time stamp is generated automatically using datetime.datetime.now().strftime(time_format), where time_format is the specified format you want the date to be in ("%d-%m-%Y_%H-%M-%S") 












