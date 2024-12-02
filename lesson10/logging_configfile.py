import logging
import logging.config


logging.config.fileConfig('logging_config.ini')

logger = logging.getLogger('root')

logger.debug('This is DEBUG message')
logger.info('This is INFO message')
