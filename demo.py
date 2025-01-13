from src.logger import logging
import sys
from src.exception import USvisaException
logging.info("welcome to custom log")


try:
    a=2/0
except Exception as e:
    raise USvisaException(e,sys)
    