import hashlib

# md5 = hashlib.md5() # 应用MD5算法
#
# data = input("请输入加密内容：")
#
# md5.update(data.encode('utf-8'))
#
# print(md5.hexdigest())

from hashlib import md5
from string import ascii_letters,digits
from itertools import permutations
from time import time
all_letters=ascii_letters+digits+'.,;'
def decrypt_md5(md5_value):
  if len(md5_value)!=32:
     print('error')
     return
  md5_value=md5_value.lower()
  for k in range(5,10):
    for item in permutations(all_letters,k):
      item=''.join(item)
      print('.',end='')
      if md5(item.encode()).hexdigest()==md5_value:
         return item
  md5_value = input()
  start=time()
  result=decrypt_md5(md5_value)
  if result:
   print('\n Success: '+md5_value+'==>'+result)
  print('Time used:',time()-start)




decrypt_md5('a3dcb4d229de6fde0db5686dee47145d')
