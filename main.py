import logging

logger = logging.getLogger('test_logger')

logger.info('This will not show up.')
logger.warning('This will.')
