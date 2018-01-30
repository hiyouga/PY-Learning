import urllib.request, urllib.parse, urllib.error
import http.cookiejar
output = open('data1.txt', 'w')
def handle(x):
	request = urllib.request.Request(x)
	cookie = http.cookiejar.CookieJar()
	handler = urllib.request.HTTPCookieProcessor(cookie)
	opener = urllib.request.build_opener(handler)
	opener.handle_open["http"][0].set_http_debuglevel(1)
	user_agent ="Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.43 BIDUBrowser/6.x Safari/537.31"
	request.add_header("User-Agent", user_agent)
	cookie ="appunion=1;ounion=58335%3Da0e2a65b7baa5cdaa09f9114047ab99;__guid=49464096.30226535217400.1513961159115.1233"
	request.add_header("Cookie", cookie)
	feeddata = opener.open(request)
	html = feeddata.read().decode()
	posa = html.find("question-main")
	posb = html.find("wz-answer")
	posc = html.find("正确答案：")
	out = html[posa+47:posb-153]
	out += "\n"
	out += html[posc:posc+50]
	out += "\n"
	output.writelines(out)
for i in range(80):
	handle("http://weixin.buaa.edu.cn/activity/wap/answer/index.html?id=43&page="+str(i+1))
output.close()