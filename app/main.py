from fastapi import FastAPI
import logging
from logging.handlers import RotatingFileHandler
import os

# Ensure logs directory exists
os.makedirs('logs', exist_ok=True)

# Logging setup
log_formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
log_file = 'logs/app.log'
handler = RotatingFileHandler(log_file, maxBytes=5*1024*1024, backupCount=2)
handler.setFormatter(log_formatter)
handler.setLevel(logging.INFO)

app_logger = logging.getLogger('app_logger')
app_logger.setLevel(logging.INFO)
app_logger.addHandler(handler)

app = FastAPI()

@app.get('/')
def read_root():
    app_logger.info('Root endpoint accessed')
    return {"message": "Hello, FastAPI with logging!"} 