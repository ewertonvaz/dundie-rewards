import os
import logging
from logging import handlers

LOG_LEVEL = os.getenv("LOG_LEVEL", "WARNING").upper()
log = logging.Logger("dundie", LOG_LEVEL)
fmt = logging.Formatter(
    '%(asctime)s %(name)s %(levelname)s'
    'l:%(lineno)d f:%(filename)s: %(message)s'
)

def get_logger(logfile="dundie.log"):
    log = logging.getLogger("log")
    """ Returns configured log"""
    fh = handlers.RotatingFileHandler(
        logfile,
        maxBytes=300,
        backupCount=10
    )
    fh.setLevel(LOG_LEVEL)
    fh.setFormatter(fmt)
    log.addHandler(fh)
    return log