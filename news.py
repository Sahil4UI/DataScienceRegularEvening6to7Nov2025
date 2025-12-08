import urllib.request as url
import bs4

path = "https://indianexpress.com/"
print("***************************HEADLINES******************************")
res = url.urlopen(path)
data=bs4.BeautifulSoup(res,features="html.parser")
topNews=data.find_all("div",class_="top-news")[1]
newsList = topNews.find_all("h3")
line=1
for i in newsList:
    print(line,". ",i.text,end="\n\n")
    line+=1
