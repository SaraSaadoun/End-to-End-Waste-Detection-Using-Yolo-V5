import os
import logging
from datetime import datetime

LOG_DIR = os.path.join(os.getcwd(), 'log')
LOG_FILE_NAME = f'{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.log'
LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE_NAME)

os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.INFO,
    format='%(asctime)s - %(name)s %(levelname)s - %(message)s'
)

