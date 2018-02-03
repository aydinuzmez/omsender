import os
import logging
import time


log_path = os.path.join(current_folder, "log", time.strftime("%d_%m_%Y")+".log")

logging.basicConfig(
    filename=log_path,
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt="%I:%M:%S %p"
                    )