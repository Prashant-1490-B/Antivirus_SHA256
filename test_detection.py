from engine.detection_engine import run_scan

if __name__ == "__main__":
    scan_results = run_scan(scan_path=".",signature_db_path="signatures/malware_signatures.txt")

    for file_path, file_hash, status in scan_results:
        print(f"[{status}] {file_path}")
        # print(scan_results[0])
    