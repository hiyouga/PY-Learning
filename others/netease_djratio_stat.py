import urllib.request, urllib.parse, urllib.error
import http.cookiejar
import re
ex = input()
if ex == '1':
	output = open('data.txt', 'w')
	url = "https://music.163.com/djradio?id=339285055&order=1&_hash=programlist&limit=400"
	request = urllib.request.Request(url)
	cookie = http.cookiejar.CookieJar()
	handler = urllib.request.HTTPCookieProcessor(cookie)
	opener = urllib.request.build_opener(handler)
	opener.handle_open["http"][0].set_http_debuglevel(1)
	user_agent = "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.43 BIDUBrowser/6.x Safari/537.31"
	request.add_header("User-Agent", user_agent)
	cookie = "__csrf=9e36d06ccfc03d1a35fe6d65be525f7c" # remember to modify
	request.add_header("Cookie", cookie)
	feeddata = opener.open(request)
	html = feeddata.read().decode().encode('gbk', 'ignore').decode('gbk', 'ignore')
	output.write(html)
	output.close()
elif ex == '2':
	data = open('data.txt', 'r').read()
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
elif ex == '3':
    data = open('list.txt', 'r').readlines()
    output = open('score.txt', 'w')
    num = int(len(data) / 4)
    mlist = []
    bias = [0, 100, 300, 500, 700, 900, 1300, 1700, 2300, 2900, 4000, 6000, 9000]
    tot_play = 0
    tot_good = 0
    for i in range(num):
        name = re.sub(r'[\'\|\n]|\(x\)', '', data[i * 4])
        play = int(data[i * 4 + 1])
        good = int(data[i * 4 + 2])
        time = data[i * 4 + 3].strip()
        if time[0:4] == '2017':
            break
        score = play + good * 40 + bias[int(time[4:6])]
        mlist.append((score, name, play, good, time))
        tot_play += play
        tot_good += good
    mlist.sort(reverse = True)
    for i in range(len(mlist)):
        output.write(str(i+1)+":\t"+mlist[i][1]+"\nPlay:"+str(mlist[i][2])+"\tGood:"+str(mlist[i][3])+"\tDate:"+mlist[i][4]+"\tScore:"+str(mlist[i][0])+"\n\n")
    output.close()
    print('Total', tot_play, 'plays', tot_good, 'goods')
else:
    print('Undefined')
print('Completed')