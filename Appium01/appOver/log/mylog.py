import logging


def test_log():
    logger = logging.getLogger()

    logger.setLevel(logging.INFO)
    if not logger.handlers:
        sh = logging.StreamHandler()
        logger.addHandler(sh)
        fmt = '%(asctime)s %(filename)s %(levelname)s %(module)s %(funcName)s %(message)s'
        formator = logging.Formatter(fmt)
        sh.setFormatter(formator)
        fh = logging.FileHandler('../logs/log1.log', encoding='utf-8')
        logger.addHandler(fh)
        fh.setFormatter(formator)
        return logger
