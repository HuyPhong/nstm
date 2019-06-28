import logging
import time

logging.basicConfig(level=logging.INFO)
for i in range(10):
    logging.info(i)
    time.sleep(1)
