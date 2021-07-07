import hashlib

s='你好，漂流的vv'
s1=hashlib.md5(s.encode("utf-8"))
print(s1.hexdigest())