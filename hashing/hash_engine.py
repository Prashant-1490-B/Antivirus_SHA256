import hashlib

def calculate_sha256(file_path):
    """
    Calculates the SHA-256 hash of a file.

    Args:
        file_path (str): Path to the file

    Returns:
        str or None: SHA-256 hash as hex string, or None if error
    """
    sha256_hash = hashlib.sha256()

    try:
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                sha256_hash.update(chunk)

        return sha256_hash.hexdigest()

    except (IOError, PermissionError):
        return None
