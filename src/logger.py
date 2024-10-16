import logging
import os
from datetime import datetime

time = datetime.now()
LOG_FILE = f'{time.strftime("%m_%d_%y_%H_%M_%S")}.log'
logs_path = os.path.join(os.getcwd(),"logs",LOG_FILE) #get current working directory
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename = LOG_FILE_PATH,
    format = "[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level = logging.INFO
)
