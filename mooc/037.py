#encode.py
#ASCII
print(ord('A'))
print(ord('a'))
print(chr(65))
#UTF-8
s = "世界，你好！"
bs = s.encode("utf-8")
print(bs)
print(bs.decode("utf-8"))
print(bs.encode("gbk"))