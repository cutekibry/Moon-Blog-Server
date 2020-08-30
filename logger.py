import logging
import sys

try:
    import coloredlogs
    coloredlogs.install(level='DEBUG')
except ModuleNotFoundError:
    pass

logger_name = 'Moon-Blog-Server'
logger = logging.getLogger(logger_name)
logger.setLevel(logging.DEBUG)
logging.StreamHandler(sys.stdout)
