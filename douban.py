import urllib.request
import http.cookiejar
import urllib.parse
from lxml import etree

def login():
    url='https://www.douban.com/accounts/login'
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.7 Safari/537.36'}
    # headers={'User-Agent':'Mozilla/5.0'}
    req=urllib.request.Request(url,headers=headers)
    filename = 'cookie.txt'
    cookie = http.cookiejar.MozillaCookieJar(filename)
    handler = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(handler)
    params={}
    params['form_email']='2404700087@qq.com'
    params['form_password']='tarena2018'
    params['source']='http://www.douban.com/accounts/login'
    res=opener.open(req,urllib.parse.urlencode(params).encode('utf-8'))
    html=res.read().decode('utf-8')
    obj=etree.HTML(html)
    img_url=obj.xpath('//img[@id="captcha_image"]/@src')[0]
    res=urllib.request.urlretrieve(img_url,'v.jpg')
    cap=obj.xpath("//input[@name='captcha-id']/@value")[0]
    if res:
        n=input('输入验证码：')
        params['captcha-solution']=n
        params['captcha-id']=cap
        params['login']='登录'
        res = opener.open(url, urllib.parse.urlencode(params).encode('utf-8'))
        if res.geturl() == "https://www.douban.com/":
            print('login success')
            cookie.save(ignore_discard=True, ignore_expires=True)


