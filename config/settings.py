# config/settings.py

# Default scan path (used if user does not provide one)
DEFAULT_SCAN_PATH = "."

# Malware signature database
SIGNATURE_DB_PATH = "signatures/malware_signatures.txt"

# Logging
LOG_FILE_PATH = "logs/scan.log"

# Directories to exclude from scanning (VERY IMPORTANT)
EXCLUDED_DIRECTORIES = {
    "__pycache__",
    ".git",
    "tests",
    "logs",
}

# File extensions to exclude (optional hardening)
EXCLUDED_EXTENSIONS = {
    ".pyc",
    ".log",
}

# Max file size to hash (bytes) – prevents scanning huge files
MAX_FILE_SIZE = 50 * 1024 * 1024  # 50 MB
