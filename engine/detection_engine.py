from scanner.file_scanner import scan_directory
from hashing.hash_engine import calculate_sha256
from signatures.signature_checker import load_signatures, is_malicious
from quarantine.quarantine_manager import quarantine_file


def run_scan(scan_path, signature_db_path, enable_quarantine=False):
    results = []

    signature_set = load_signatures(signature_db_path)
    files = scan_directory(scan_path)

    for file_path in files:
        file_hash = calculate_sha256(file_path)

        if is_malicious(file_hash, signature_set):
            status = "MALICIOUS"

            quarantined_path = None
            if enable_quarantine:
                quarantined_path = quarantine_file(file_path)

            results.append((file_path, file_hash, status, quarantined_path))

        else:
            status = "CLEAN"
            results.append((file_path, file_hash, status, None))

    return results
