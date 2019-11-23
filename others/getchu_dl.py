import urllib.request, urllib.parse, urllib.error
import http.cookiejar
import re
import os
request = urllib.request.Request("http://trial.getchu.com/D090/983160/983160_opdemo.mp4")
cookie = http.cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
user_agent ="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"
request.add_header("User-Agent", user_agent)
request.add_header("Accept", "*/*")
request.add_header('Referer', "http://www.getchu.com/soft.phtml?id=983160&gc=gc")
cookie =""
request.add_header("Cookie", cookie)
feeddata = opener.open(request)
output = open('temp.mp4', 'wb')
output.write(feeddata.read())
output.close()