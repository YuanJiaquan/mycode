# 日志：文档  文件 日记  记录系统运行的内容
# 日志的作用：能够记录在系统上面进行的操作  记录系统运行状态  出现问题也能很快定位问题

# 学习日志
# 几个组件
# 1.loggers:日志器
# 2.handler:处理器
# 3.formatter:格式器

# 日志级别  info  error  能够反映出问题的严重程度
# debug:调试的级别  1级别
# info:正常的级别  2级别
# warning:警告  程序有问题但是不影响程序正常运行  3级别 不提bug  默认的级别
# error:错误  程序有问题  4级别
# critical:严重的问题  程序崩溃了 5级别

# logging是自带的，不需要你安装
# 可以用别人已经封装好的
import logging
# import loguru

# loguru.logger.info('info')

# 设置日志的级别,日志的格式不是我们想要的，设置格式  格式的字符串
# 日志信息输出到控制台  为什么要把日志信息输出文件里面？
# 基础配置写法，1.日志信息不能在控制台和文件里面同时出现  2.会乱码

# 函数的内容：就是设置了日志的格式，日志的保存在哪
def test_log():
    fmt='%(asctime)s %(filename)s %(levelname)s  %(funcName)s  %(message)s'
    logging.basicConfig(level=logging.DEBUG,format=fmt,filename='log1.log')
    return logging
# logging.debug('debug模式')
# log.info('初始化driver{}'.format(driver))
# logging.info('info模式')
# logging.warning('warning模式')
# logging.error('error模式')
# logging.critical('critical模式')

# 日志文件 ，你想要放在目录下，就要自己创建目录，项目