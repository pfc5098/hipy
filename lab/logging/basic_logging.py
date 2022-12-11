import os
import logging

log_file_name = 'log_file.log'
if os.path.exists(log_file_name):
    os.remove(log_file_name)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s', datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[logging.FileHandler(log_file_name), logging.StreamHandler()]
)

import time

logging.info('Preparing data.')
time.sleep(1)
logging.info('Fitting model.')
time.sleep(1)
logging.info('Making prediction.')
time.sleep(1)