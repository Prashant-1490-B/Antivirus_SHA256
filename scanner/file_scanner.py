import os

def scan_directory(root_path):
    """
    Recursively scans a directory and returns a list of file paths.

    Args:
        root_path (str): Directory to scan

    Returns:
        list: List of absolute file paths
    """
    collected_files = []

    for root, dirs, files in os.walk(root_path):
        for file_name in files:
            full_path = os.path.join(root, file_name)
            collected_files.append(full_path)

    return collected_files  
