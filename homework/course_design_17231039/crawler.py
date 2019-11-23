from urllib.request import Request, urlopen
from urllib.parse import urlparse
from html.parser import HTMLParser
from queue import Queue
import json

init_url = urlparse('https://news.sina.com.cn/')
base_url = urlparse('')
skiplist = ['jpg', 'jpeg', 'gif', 'bmp', 'flv', 'mp4', 'wmv', 'swf', 'css', 'rar', 'jsp', 'pdf', 'exe']
docs = {}
queue = Queue()
queue.put(init_url.geturl())

class MyParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
    
    def handle_starttag(self, tag, attrList):
        if tag == 'a':
            try:
                attrs = {}
                for k, v in attrList:
                    attrs[k] = v
                if 'href' in attrs.keys():
                    link = attrs['href']
                else:
                    return
                if '#' in link:
                    return
                link = link.strip()
                link = link.replace('http://', 'https://')
                pr = urlparse(link)
                u = pr.path.rfind('.')
                if u > 0 and pr.path[u+1:] in skiplist:
                    return
                if pr.scheme == '' and pr.netloc == '':
                    if pr.path and pr.path[0] == '/':
                        link = base_url.scheme + base_url.netloc + link
                    else:
                        link = base_url.geturl()[0: base_url.geturl().rfind('/') + 1] + link
                elif pr.scheme not in ['http', 'https'] or pr.netloc != base_url.netloc:
                    return
                p = link.split('/')
                while '..' in p:
                    v = p.index('..')
                    p.pop(v-1)
                    p.pop(v-1)
                link = '/'.join(p)
                if link not in docs[base_url.geturl()]:
                    docs[base_url.geturl()][link] = 1
                    queue.put(link)
                else:
                    docs[base_url.geturl()][link] += 1
            except Exception as e:
                print('Error', e)
                return

parser = MyParser()
depth = 2
seq = 0

while not queue.empty() and depth > 0:
    for i in range(queue.qsize()):
        cururl = queue.get()
        if cururl in docs:
            continue
        base_url = urlparse(cururl)
        docs[base_url.geturl()] = {}
        try:
            parser.feed(str(urlopen(Request(base_url.geturl(), headers={'User-agent': 'Mozilla 5.10'})).read(), encoding = 'utf8'))
            print(base_url.geturl(), 'indexed.')
            seq += 1
        except UnicodeDecodeError:
            parser.feed(str(urlopen(Request(base_url.geturl(), headers={'User-agent': 'Mozilla 5.10'})).read(), encoding = 'gbk'))
            print(base_url.geturl(), 'indexed.')
            seq += 1
        except Exception as e:
            print('Failed to index', base_url.geturl(), '. The error is', e)
    depth -= 1

with open('docs.json', 'w') as f:
    f.write(json.dumps(docs, sort_keys=True, indent=4))
    f.close()

print('Completed! Indexed', seq, 'links!')
