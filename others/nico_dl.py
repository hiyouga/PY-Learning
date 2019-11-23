import urllib.request, urllib.parse, urllib.error
import http.cookiejar

output = open('temp.mp4', 'wb')
for i in range(1, 40):
	request = urllib.request.Request("https://pe036c18c1c.dmc.nico/hlsvod/ht2_nicovideo/nicovideo-sm35467924_a7597e2d2cf6685941472edb38be2472753cc62fc434d8fd6a72a228d7d59ac5/1/ts/" + str(i) + ".ts?ht2_nicovideo=25777085.kbanke_pwa33k_16sahf4rs5258")
	cookie = http.cookiejar.CookieJar()
	handler = urllib.request.HTTPCookieProcessor(cookie)
	opener = urllib.request.build_opener(handler)
	user_agent ="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"
	request.add_header("User-Agent", user_agent)
	request.add_header("Accept", "*/*")
	request.add_header('Referer', "https://static.parastorage.com/services/wix-vod/1.651.0/widget.html?cacheKiller=1518237527123&compId=comp-jbqvsxbn&deviceType=desktop&externalId=4c713b09-fcdb-47c6-ba5e-bbeadcca5360&height=308&instance=SuiQm6-jnLbnPtxLUldL3jt3jVWVkluuO39IcnAG9T0.eyJpbnN0YW5jZUlkIjoiOTg3OGY5MjctN2EzYy00NzcyLWFkZWItOTExM2RmMGNhOTJhIiwiYXBwRGVmSWQiOiIxNDQwOTU5NS1mMDc2LTQ3NTMtODMwMy05YTg2ZjlmNzE0NjkiLCJzaWduRGF0ZSI6IjIwMTgtMDItMTBUMDQ6Mzg6NDcuNDg2WiIsInVpZCI6bnVsbCwiaXBBbmRQb3J0IjoiMTMzLjE4LjE5NC4xOTkvMzkxOTEiLCJ2ZW5kb3JQcm9kdWN0SWQiOm51bGwsImRlbW9Nb2RlIjpmYWxzZSwiYWlkIjoiMTEwM2UzMTItNTg5Zi00MWU1LTg4NTUtNGI4YTQ3ZjgxOTFhIiwiYmlUb2tlbiI6Ijc1ODI4NGFkLTk4OGMtMDlkNS0wN2VkLWNjNjRkYjJmOTY2MiIsInNpdGVPd25lcklkIjoiYWYxZDkwMTAtMGM3NS00MjNkLTkwYjAtZWNmNWI4ZjgyZWYwIn0&locale=ja&pageId=cihbc&viewMode=site&vsi=ee781ece-ef49-4e5a-8288-eaa5f7520913&width=476")
	cookie = ""
	request.add_header("Cookie", cookie)
	feeddata = opener.open(request)
	output.write(feeddata.read())
	print(i)

output.close()