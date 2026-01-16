def load_signatures(signature_file):
    """
    Loads malware signatures from a file.

    Args:
        signature_file (str): Path to signature database

    Returns:
        set: Set of known malicious hashes
    """
    signatures = set()

    try:
        with open(signature_file, "r") as f:
            for line in f:
                signature = line.strip().lower()
                if signature:
                    signatures.add(signature)

    except IOError:
        pass

    return signatures


def is_malicious(file_hash, signature_set):
    """
    Checks if a hash exists in the malware signature set.

    Args:
        file_hash (str): SHA-256 hash of file
        signature_set (set): Loaded malware hashes

    Returns:
        bool: True if malicious, False otherwise
    """
    if not file_hash:
        return False

    return file_hash.lower() in signature_set
