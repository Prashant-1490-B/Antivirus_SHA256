import os
from engine.detection_engine import run_scan
from config.settings import DEFAULT_SCAN_PATH, SIGNATURE_DB_PATH


def main():
    print("=== Basic Antivirus Scanner (Production Mode) ===")

    scan_path = input(
        f"Enter directory path to scan (default: {DEFAULT_SCAN_PATH}): "
    ).strip()

    if not scan_path:
        scan_path = DEFAULT_SCAN_PATH

    if not os.path.exists(scan_path):
        print("Invalid path. Exiting.")
        return

    results = run_scan(
        scan_path=scan_path,
        signature_db_path=SIGNATURE_DB_PATH
    )

    print("\n=== Scan Results ===")
    for file_path, file_hash, status in results:
        print(f"[{status}] {file_path}")

    print("\nScan completed.")
    print("Logs saved to logs/scan.log")


if __name__ == "__main__":
    main()
