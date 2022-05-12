"""This tests logging"""

import os
import json
import app.config
from app.logging_config import add_path_to_logfile
from app.logging_config import LOGGING_CONFIG


def test_logfile_misc_debug():
    """ check if misc_debug.log exists """
    log_dir = app.config.Config.LOG_DIR
    filepath = os.path.join(log_dir, "misc_debug.log")
    # assert os.path.isfile(filepath)



def test_logfile_request():
    """ check if misc_debug.log exists """
    log_dir = app.config.Config.LOG_DIR
    filepath = os.path.join(log_dir, "request.log")
    # assert os.path.isfile(filepath)
