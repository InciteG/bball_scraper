"""Logging Module

Module sets up basic logging infrastructure for application
"""

import logging
import sys
from typing import Optional

BRIEF_FORMAT = "%(levelname)s %(asctime)s - %(name)s: %(message)s"
VERBOSE_FORMAT= (
    "%(levelname)s|%(asctime)s|%(name)s|%(filename)s|" "%(funcName)s|%(lineo)d: %(message)s"
)

FORMAT_TO_USE=VERBOSE_FORMAT

DEBUG= logging.DEBUG
INFO = logging.INFO
WARN = logging.WARN
ERROR = logging.ERROR
CRITICAL = logging.CRITICAL

def get_logger(name: Optional[str]=None, log_level: int=logging.INFO) -> logging.Logger:
    """
    
    
    """
    
    logging.basicConfig(format=FORMAT_TO_USE, stream=sys.stdout, level=log_level)
    logger=logging.getLogger(name)
    return logger
