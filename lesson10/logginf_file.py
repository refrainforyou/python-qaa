import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler('logfile.txt')
file_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

logger.debug('This is DEBUG message')
logger.info('This is INFO message')
logger.warning('This is WARNING message')
logger.error('This is ERROR message')
logger.critical('This is CRITICAL message')

file_handler.close()
