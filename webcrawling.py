# library
import urllib.request as url
import bs4
name = input("Enter product name : ").replace(" ","%20")
path ="https://www.flipkart.com/search?q="+name
res = url.urlopen(path)
# data fetch
data = bs4.BeautifulSoup(res,features="html.parser")
product = data.find("div",class_="RG5Slk")
price = data.find("div",class_="hZ3P6w DeU9vF")
print(product.text)
print(price.text)
features = data.find("ul",class_="HwRTzP")
features_list=features.find_all("li")
# print(features_list)
print("Features : ")
for item in features_list:
    print("=>",item.text,"\n")
