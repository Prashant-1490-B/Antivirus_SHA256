from engine.detection_engine import run_scan

if __name__ == "__main__":
    results = run_scan(
        scan_path=".",
        signature_db_path="signatures/malware_signatures.txt",
        enable_quarantine=True
    )

    for result in results:
        file_path, file_hash, status, quarantined_path = result

        if status == "MALICIOUS":
            print(f"[QUARANTINED] {file_path} -> {quarantined_path}")
        else:
            print(f"[CLEAN] {file_path}")
