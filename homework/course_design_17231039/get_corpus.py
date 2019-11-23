import json
from urllib.request import Request, urlopen
from html.parser import HTMLParser

with open('pagerank.json', 'r') as f:
    pages = json.loads(f.read())
    f.close()

current_url = ''
content_dic = {}

class MyParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.capturing = False
        self.masking = False
        self.stack = 0
    
    def handle_starttag(self, tag, attrList):
        if tag == 'div':
            if self.capturing:
                self.stack += 1
            else:
                attrs = {}
                for k, v in attrList:
                    attrs[k] = v
                if 'id' in attrs.keys() and attrs['id'] == 'article':
                    self.capturing = True
        if self.capturing and tag == 'script':
            self.masking = True
    
    def handle_endtag(self, tag):
        if tag == 'div':
            if self.stack == 0:
                self.capturing = False
            else:
                self.stack -= 1
        if self.capturing and tag == 'script':
            self.masking = False
        
    def handle_data(self, data):
        if self.capturing and not self.masking:
            content_dic[current_url] += data.strip()            

parser = MyParser()

for k in pages.keys():
    current_url = k
    content_dic[current_url] = ''
    try:
        parser.feed(str(urlopen(Request(current_url, headers={'User-agent': 'Mozilla 5.10'})).read(), encoding = 'utf8'))
        print(current_url, 'archived.')
    except UnicodeDecodeError:
        parser.feed(str(urlopen(Request(current_url, headers={'User-agent': 'Mozilla 5.10'})).read(), encoding = 'gbk'))
        print(current_url, 'archived.')
    except Exception as e:
        print('Failed to archive', current_url, '. The error is', e)

def std_fn(s):
    return s.replace(':', '').replace('/', '-')

for k, v in content_dic.items():
    with open('./corpus/'+std_fn(k)+'.txt', 'w') as f:
        f.write(v.encode('gbk', 'ignore').decode('gbk'))

print('Completed!')