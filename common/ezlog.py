import logging


def get_logger():
    logger = logging.getLogger()
    logger.setLevel(level=logging.INFO)
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    formatter = logging.Formatter('[%(levelname)s][%(name)s][%(asctime)s]: %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger
