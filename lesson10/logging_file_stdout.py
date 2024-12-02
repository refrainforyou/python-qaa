import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
file_handler = logging.FileHandler('logfile.txt')

console_handler.setLevel(logging.DEBUG)
file_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s - %(filename)s - %(funcName)s - %(lineno)d - %(name)s', datefmt='%Y-%m-%d %H:%M:%S')

console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)


def run_logger():
    logger.debug('This is DEBUG message')
    logger.info('This is INFO message')
    logger.warning('This is WARNING message')
    logger.error('This is ERROR message')
    logger.critical('This is CRITICAL message')


run_logger()

file_handler.close()
