""" Core module of dundie"""
from dundie.utils.log import get_logger

log = get_logger()

def load(file_path):
    """
    
    >>> len(load("assets/people.csv))
    2

    """
    try:
      with open(file_path) as file_:
        return file_.readlines()
    except FileNotFoundError as e:
       log.error(str(e))
       raise(e)
