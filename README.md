# Basic Antivirus Simulation (Signature-Based Scanner)

## Overview
This project is a **production-style antivirus simulation** built using Python that demonstrates how **signature-based malware detection** works internally.

The antivirus scans user-specified directories, generates cryptographic hashes (SHA-256) of files, compares them against a known malware signature database, and reports whether files are **CLEAN** or **MALICIOUS**.  
All scan activity is logged to provide a forensic and audit trail.

> ⚠️ **Disclaimer**  
> This project is strictly for **educational and ethical purposes only**.  
> It does not detect real malware unless real malware signatures are intentionally added.  
> Do not use this tool on systems or files without proper authorization.

---

## Key Concepts Demonstrated
- Signature-based malware detection
- Cryptographic hashing (SHA-256)
- Recursive file system scanning
- Modular antivirus architecture
- Production-style configuration management
- Logging and forensic evidence generation
- Separation of test and production code

---


Each module has **a single responsibility**, closely mirroring how real antivirus engines are designed.

---

## How the Antivirus Works (Detection Flow)

1. User provides a directory path to scan
2. The scanner recursively enumerates files
3. Each file is read in binary mode
4. A SHA-256 hash is generated for each file
5. The hash is compared against known malware signatures
6. The file is classified as **CLEAN** or **MALICIOUS**
7. All events are logged for auditing

---

## Usage (Production Mode)

### Run the Antivirus
python main.py

## Example Execution
=== Basic Antivirus Scanner (Production Mode) ===
<br>
Enter directory path to scan (default: .): C:\Users\Documents

[CLEAN] C:\Users\Documents\notes.txt
<br>
[MALICIOUS] C:\Users\Documents\test_scanner.py

Scan completed.
Logs saved to logs/scan.log
