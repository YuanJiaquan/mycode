import logging

def log():
    logger=logging.getLogger()
    logger.setLevel(logging.INFO)
    if not logger.handlers:
        fmt = '%(asctime)s %(filename)s %(levelname)s  %(funcName)s  %(message)s'
        format = logging.Formatter(fmt)
        sh=logging.StreamHandler()
        logger.addHandler(sh)
        sh.setFormatter(format)
        fh=logging.FileHandler('log.log',encoding='utf-8')
        logger.addHandler(fh)
        fh.setFormatter(format)

    return logger