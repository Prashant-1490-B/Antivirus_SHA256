import os
import shutil
import time


def quarantine_file(file_path, quarantine_dir="quarantine"):
    """
    Moves a malicious file to quarantine directory.

    Args:
        file_path (str): Path to malicious file
        quarantine_dir (str): Quarantine directory

    Returns:
        str or None: New quarantined file path, or None if failed
    """
    try:
        if not os.path.exists(quarantine_dir):
            os.makedirs(quarantine_dir)

        filename = os.path.basename(file_path)
        timestamp = int(time.time())

        quarantined_name = f"{filename}.{timestamp}.quarantine"
        quarantined_path = os.path.join(quarantine_dir, quarantined_name)

        shutil.move(file_path, quarantined_path)

        return quarantined_path

    except (IOError, PermissionError, shutil.Error):
        return None
