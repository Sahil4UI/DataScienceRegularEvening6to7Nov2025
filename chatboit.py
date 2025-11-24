import webbrowser
import urllib.request as url#request send krna and response dena
import bs4#request ka response ane k bad data fetch krna
helloIntent = ["hey","hello","hi","wasup","sup","hola"]
byeIntent = ["bye","tata","see you"]
while True:
    msg = input("Enter Msg:")
    if msg in helloIntent:
        print("hey....")
    elif msg in byeIntent:
        print("Bye.....")
        break#exit
    elif msg.startswith("open"):
        webbrowser.open("https://"+msg.split()[1]+".com")
    elif "news" in msg:
        path = "https://indianexpress.com/"
        response = url.urlopen(path)
        data = bs4.BeautifulSoup(response,features="html.parser")
        div = data.find_all("div",class_="top-news")[1]
        newsList = div.find_all("h3")
        for news in newsList:
            print("=>.  ",news.text,"\n\n")
    else:
        print("Sorry I Didn't Understand")
