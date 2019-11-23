import pickle
import tkinter as tk
import tkinter.font as tkFont

word_index = pickle.load(open('word_index.dic', 'rb'))

def std_fn(s):
    return s.replace(':', '').replace('/', '-')

def search():
    for widget in searchResult.winfo_children():
        widget.destroy()
    word = wordEntry.get().strip()
    if word in word_index.keys():
        searchStatus.config(text = '搜索到{:d}条结果'.format(len(word_index[word])))
        for w, l in word_index[word][0:3]:
            with open('./corpus/'+std_fn(l)+'.txt', 'r') as f:
                textLabel = tk.Label(searchResult, text=f.read()[0:120]+'...', font=font, justify='left', wraplength=800)
                textLabel.pack()
    else:
        searchStatus.config(text = '无搜索结果')
    

if __name__ == '__main__':
    root = tk.Tk()
    font = tkFont.Font(family = 'SimHei', size = 14)
    topFrame = tk.LabelFrame(root, text = '新闻词云')
    wordcloud = tk.PhotoImage(file = 'wordcloud.gif')
    imgLabel = tk.Label(topFrame, image = wordcloud, width = 800, height = 200)
    imgLabel.pack()
    topFrame.pack()
    # center
    centerFrame = tk.LabelFrame(root, text = '关键词搜索')
    centerFrame.configure(width = 800)
    wordEntry = tk.Entry(centerFrame, show = None, font = ('SimHei', 14), width = 75)
    wordEntry.pack(side = tk.LEFT)
    searchButton = tk.Button(centerFrame, text = '搜索', command = search)
    searchButton.pack(side = tk.RIGHT)
    centerFrame.pack()
    # bottom
    bottomFrame = tk.LabelFrame(root, text = '搜索结果')
    searchStatus = tk.Label(bottomFrame, text = '请输入搜索内容', font = font)
    searchStatus.pack()
    searchResult = tk.Frame(bottomFrame)
    searchResult.configure(width = 800, height = 400)
    searchResult.pack()
    bottomFrame.pack()
    root.title('新浪热搜')
    root.geometry('820x600')
    tk.mainloop()