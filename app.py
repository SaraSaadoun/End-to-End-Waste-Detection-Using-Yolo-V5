from wasteDetection.logger import logging
from wasteDetection.exception import AppException
import sys 

logging.info('hello world from logger')

try:
    a = 3 / 'a'
except Exception as e:
    raise AppException(e, sys)