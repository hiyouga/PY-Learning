import json
import jieba
import pickle
from gensim.models import LdaModel, TfidfModel
from gensim.corpora import Dictionary
from wordcloud import WordCloud

with open('pagerank.json', 'r') as f:
    pages = json.loads(f.read())
    f.close()

pagelist = list(pages.keys())
contents = []
word_stats = {}

def std_fn(s):
    return s.replace(':', '').replace('/', '-')

for page in pagelist:
    with open('./corpus/'+std_fn(page)+'.txt', 'r') as f:
        contents.append(f.read())

print('Starting jieba module')
jieba.load_userdict("userdict.txt")
train = []
skiplist = ['', '\n', '，', '。', '：', '；', '！', '？', '《', '》', '“', '”', '、', '（', '）', '&', '|', '▲', '·', '↓']
stopwords = [line.strip() for line in open('stopwords.txt', 'r', encoding='utf-8').readlines()]
for content in contents:
    seg_list = jieba.lcut(content, cut_all = False)
    result = []
    for seg in seg_list:
        seg = ''.join(seg.split())
        if len(seg) > 1 and seg not in skiplist and seg not in stopwords:
            result.append(seg)
    train.append(result)

print('Starting gensim module')
dictionary = Dictionary(train)
corpus = [dictionary.doc2bow(text) for text in train]
tfidf = TfidfModel(corpus)
corpus_tfidf = tfidf[corpus]
lda_model = LdaModel(corpus=corpus_tfidf, id2word=dictionary, num_topics=50)
corpus_lda = lda_model[corpus_tfidf]
topic_list = []
for i in range(lda_model.num_topics):
    topic_list.append(lda_model.show_topic(i))
word_index = {}
for i in range(len(pagelist)):
    theme, dist = sorted(corpus_lda[i], key=lambda x:x[1], reverse=True)[0]
    #print(lda_model.print_topic(theme))
    weight = pages[pagelist[i]]*1e5
    for topic_word, likelihood in topic_list[theme]:
        if topic_word in word_stats.keys():
            word_stats[topic_word] += likelihood * weight
            word_index[topic_word].append((dist * likelihood, pagelist[i]))
        else:
            word_stats[topic_word] = likelihood * weight
            word_index[topic_word] = [(dist * likelihood, pagelist[i])]

cloud = WordCloud(
    font_path = 'simhei.ttf',
    width = 400,
    height = 100,
    background_color = 'white',
    mode = "RGBA",
    scale = 2,
    max_words = 50,
    max_font_size = 40
)
wcloud = cloud.generate_from_frequencies(word_stats)
wcloud.to_file('wordcloud.gif')

for k, v in word_index.items():
    v.sort(reverse = True)

pickle.dump(word_index, open('word_index.dic', 'wb'))
print('Completed!')