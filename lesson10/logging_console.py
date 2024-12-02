import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

logger.debug('This is DEBUG message')
logger.info('This is INFO message')
logger.warning('This is WARNING message')
logger.error('This is ERROR message')
logger.critical('This is CRITICAL message')

console_handler.close()
