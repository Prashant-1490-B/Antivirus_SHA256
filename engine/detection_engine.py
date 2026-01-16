from scanner.file_scanner import scan_directory
from hashing.hash_engine import calculate_sha256
from signatures.signature_checker import load_signatures, is_malicious


def run_scan(scan_path, signature_db_path):
    """
    Runs a full antivirus scan on a directory.

    Args:
        scan_path (str): Directory to scan
        signature_db_path (str): Path to malware signatures file

    Returns:
        list: List of tuples (file_path, file_hash, status)
    """
    results = []

    # Load malware signatures once
    signature_set = load_signatures(signature_db_path)

    # Scan files
    files = scan_directory(scan_path)

    for file_path in files:
        file_hash = calculate_sha256(file_path)

        if is_malicious(file_hash, signature_set):
            status = "MALICIOUS"
        else:
            status = "CLEAN"

        results.append((file_path, file_hash, status))

    return results
