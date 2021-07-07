# 导入md5加密的库
import hashlib


# arg = '守护世界上最好的虚竹'
# print(arg)
# # md5加密的实现形式
# se = hashlib.md5(arg.encode('utf-8'))
# # 获取变量的内存地址
# print(se)
# # 获取值
# print(se.hexdigest())

# md5加密的封装函数
def hashmd5(string):
    return hashlib.md5(str(string).encode('utf-8')).hexdigest()
