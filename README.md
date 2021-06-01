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
- Using Google Developers Console
###### Steps to follow to get Youtube api key;
1. Launch Google Developers Console (url= https://console.developers.google.com)
2. Click on ENABLE APIS AND SERVICES ( this can be found at the top of the site)
3. Next you search for youtube and select Youtube Data Api v3 (this is an API that provides access to YouTube data, such as videos, playlists, channels)
4. Then you select enable this api (you are redirected to an overview page of the youtube api)
5. Next select the credentials tab( this is found on the left hand side of the page)
6. Select create credential ( found on the top part of the site), 
7. After select create api key,key is created and you can copy it.

After the following steps your key is ready for use to make api calls.

###### Passing credentials into python script
![Capture1](https://user-images.githubusercontent.com/65185008/120339033-9d583f80-c2a9-11eb-9582-21432d106fb6.PNG)
![Capture2](https://user-images.githubusercontent.com/65185008/120339166-ba8d0e00-c2a9-11eb-83bf-4c30913c007e.PNG)

- Filter youtube for the type of data you want, year data was uploaded and the number of videos you want to return

![Capture3](https://user-images.githubusercontent.com/65185008/120339744-3a1add00-c2aa-11eb-977a-aafc4775c1b9.PNG)
passing requirements needed for filtering data as an argument
###### Arguments
-q, --query : Specify the search query. The default value is '#endsars'.














