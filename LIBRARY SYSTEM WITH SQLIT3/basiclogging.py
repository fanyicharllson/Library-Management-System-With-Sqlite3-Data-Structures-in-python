import logging

def create_basic_logging():
    file_handdlers = logging.FileHandler("Application.log")
    logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(asctime)s: %(name)s %(message)s', handlers=[file_handdlers])
    
    return logging 
