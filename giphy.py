import urllib.request as url
import json
name  = input("Enter Name to SEARCH : ").replace(" ","+")
path = "https://api.giphy.com/v1/gifs/search?api_key=d3vBGqDiJidgq3fFmzOyjFam6iEuHxyD&q="+name+"&limit=25&offset=0&rating=g&lang=en&bundle=messaging_non_clips"

res = url.urlopen(path)
data = json.load(res)["data"]
for index,item in enumerate(data):
    gif=item["images"]["original"]["url"]
    url.urlretrieve(gif,f"file{index}.gif")
    print(f"{index+1} files downloaded")
