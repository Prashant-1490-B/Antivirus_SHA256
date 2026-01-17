from scanner.file_scanner import scan_directory

if __name__ == "__main__":
    files = scan_directory(".")

    print("Files found:\n")
    for f in files:
        print(f)
