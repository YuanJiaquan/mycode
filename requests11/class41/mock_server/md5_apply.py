import hashlib
import datetime



def findmd5(args):
    md=args.hashvalue
    starttime=datetime.datetime.now()
    for i in open(args.file):
        md5=hashlib.md5()   #获取一个md5加密算法对象
        rs=i.strip()    #去掉行尾的换行符
        md5.update(rs.encode('utf-8'))  #指定需要加密的字符串
        newmd5=md5.hexdigest()  #获取加密后的16进制字符串
        #print newmd5
        if newmd5==md:
            print('明文是：'+rs )    #打印出明文字符串
            break
        else:
            pass

    endtime=datetime.datetime.now()
    print(endtime-starttime)	#计算用时，非必须

# def hashmd5(string):
#
#     return hashlib.md5(str(string).encode('utf-8')).hexdigest()

