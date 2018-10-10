import http.cookiejar
import urllib.request
import requests
from douban import *

filename='cookie.txt'
login()
url='https://book.douban.com/people/185136907/collect'
cookie=http.cookiejar.MozillaCookieJar()
cookie.load(filename,ignore_discard=True, ignore_expires=True)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.7 Safari/537.36'
    }
handler = urllib.request.HTTPCookieProcessor(cookie)
req=urllib.request.Request(url,headers=headers)
opener = urllib.request.build_opener(handler)
res=opener.open(req)
html=res.read().decode('utf-8')
print(html)