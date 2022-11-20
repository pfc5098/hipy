import logging 
logging.basicConfig(filename='basics.log', 
                    level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

logging.info('hello A')
logging.info('hello B')