import urllib.request as req
url = 'https://www.ptt.cc/bbs/Badminton/index.html'
request = req.Request(url,headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'})
with req.urlopen(request) as response:
    data = response.read()
#    print(data)

import bs4

root = bs4.BeautifulSoup(data,'html.parser')

titles = root.find_all('div',class_='title')
for title in titles:
    if title != None:
        print(title.a.string)
        

