import os
from datetime import datetime


def log_event(message, log_file="logs/scan.log"):
    """
    Writes a log entry with timestamp.

    Args:
        message (str): Log message
        log_file (str): Path to log file
    """
    try:
        log_dir = os.path.dirname(log_file)
        if log_dir and not os.path.exists(log_dir):
            os.makedirs(log_dir)

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(log_file, "a") as f:
            f.write(f"[{timestamp}] {message}\n")

    except IOError:
        pass
