import logging 
import os 
from datetime import datetime

LOG_FIILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
log_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exit_ok=True)

LOG_FILE_PATH=od,path.join(logs_path,LOG_FIILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,


)