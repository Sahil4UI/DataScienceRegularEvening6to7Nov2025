# library
import urllib.request as url
import bs4
name = input("Enter product name : ").replace(" ","%20")
path ="https://www.flipkart.com/search?q="+name
res = url.urlopen(path)
# data fetch
data = bs4.BeautifulSoup(res,features="html.parser")
path = "https://www.flipkart.com"+data.find("a",class_="k7wcnx")["href"]
res = url.urlopen(path)
data = bs4.BeautifulSoup(res,features="html.parser")
product=data.find("span",class_="LMizgS")
print("Product Name : ",product.text)
rating = data.find("div",class_="MKiFS6")
print("rating : ",rating.text)
path = "https://www.flipkart.com"+data.find("div",class_="col MDzIYy").find_all("a")[-1]["href"]
res = url.urlopen(path)
data = bs4.BeautifulSoup(res,features="html.parser")
reviewList = data.find_all("p",class_="qW2QI1")
reviewDescList = data.find_all("div",class_="G4PxIA")

for i in zip(reviewList,reviewDescList):
    print("=> ",i[0].text,"\n\n",i[1].text,end="\n\n\n")
    print("********************************")
