import logging

def fen_log():
    logger=logging.getLogger()
    logger.setLevel(logging.INFO)
    if not logger.handlers:
        fmt = '%(asctime)s %(filename)s %(levelname)s  %(funcName)s  %(message)s'
        format = logging.Formatter(fmt)
        sh=logging.StreamHandler()
        logger.addHandler(sh)
        sh.setFormatter(format)
        fh=logging.FileHandler('log2.log',encoding='utf-8')
        logger.addHandler(fh)
        fh.setFormatter(format)

    return logger



# f='%(asctime)s %(filename)s %(levelname)s  %(funcName)s  %(message)s'
# logging.basicConfig(level=logging.WARNING,format=f)
# logging.debug('debug模式')
# logging.info('info模式')
# logging.warning('warning模式')
# logging.error('error模式')
# logging.critical('critical模式')
fen_log()