import urllib.request as req
url = 'https://www.ptt.cc/bbs/movie/index.html'
request = req.Request (url, 
  headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'})
  
response = req.urlopen(request)
web = response.read().decode('utf-8')
print(web)

# with req.urlopen(request) as response:
#     data = response.read().decode('utf-8')
#     print(data)

import bs4
root = bs4.BeautifulSoup(web,'html.parser')
titles = root.find_all("div",class_='title')
for title in titles:
    if title.a != None:
        print(title.a.string)


# import urllib.request as ur #網路爬蟲
# url='https://www.ptt.cc/bbs/Lifeismoney/index.html'
# request=ur.Request(url,
#   headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'})
# with ur.urlopen(request) as respone:
#   data=respone.read().decode('utf-8')
# print(data)
