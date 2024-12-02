import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
logging.getLogger('').addHandler(console_handler)

logging.debug('This is DEBUG message')
logging.info('This is INFO message')
logging.warning('This is WARNING message')
logging.error('This is ERROR message')
logging.critical('This is CRITICAL message')
