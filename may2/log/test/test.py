import logging

fmt='%(asctime)s %(filename)s %(levelname)s  %(funcName)s  %(message)s'
logging.basicConfig(level=logging.DEBUG,format=fmt,filename='log.log')

# logging.debug('debug模式')
# logging.info('info模式')
# logging.warning('warning模式')
# logging.error('error模式')
# logging.critical('critical模式')
print('nihao')
