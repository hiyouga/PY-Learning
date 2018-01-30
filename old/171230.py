import urllib.request, urllib.parse, urllib.error
import http.cookiejar
import re
x = str(input())
if x == '1':
	output = open('data.txt', 'w')
	request = urllib.request.Request("http://music.163.com/djradio?id=339285055&order=1&_hash=programlist&limit=400#programlist")
	cookie = http.cookiejar.CookieJar()
	handler = urllib.request.HTTPCookieProcessor(cookie)
	opener = urllib.request.build_opener(handler)
	opener.handle_open["http"][0].set_http_debuglevel(1)
	user_agent ="Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.43 BIDUBrowser/6.x Safari/537.31"
	request.add_header("User-Agent", user_agent)
	cookie ="__csrf=200c0517639dc79c7d12fcb1bc84f9d1"
	request.add_header("Cookie", cookie)
	feeddata = opener.open(request)
	html = feeddata.read().decode().encode('gbk', 'ignore').decode('gbk', 'ignore')
	output.write(html)
	output.close()
else:
	data = open('data.txt').read()
	output = open('list.txt', 'w')
	pattern = re.compile('<div.*?class="tt f-thide">.*?</div>')
	pattern2 = re.compile('<td class="col3"><span class="s-fc3">.*?</span></td>\n<td class="col4"><span class="s-fc3">.*?</span></td>\n<td class="col5"><span class="s-fc4">.*?</span></td>')
	items = re.findall(pattern, str(data))
	items2 = re.findall(pattern2, str(data))
	for i in range(0, len(items)):
		name = re.sub('<div class="tt f-thide"><a href=".*?" title=".*?">|</a></div>', "", str(items[i]))
		info = re.sub('<td class=".*?"><span class=".*?">|</span></td>|播放|赞|-', "", str(items2[i]))
		output.write(name+"\n"+info+"\n")
	output.close()