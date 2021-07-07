import logging


def my_log():
    fmt = '%(asctime)s %(filename)s %(levelname)s  %(funcName)s  %(message)s'
    logging.basicConfig(level=logging.DEBUG, format=fmt, filename='log.log')
    return logging
