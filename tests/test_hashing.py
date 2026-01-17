from hashing.hash_engine import calculate_sha256  #hashing is the folder and hash_engine is the file name

if __name__ == "__main__":
    test_file = "test_scanner.py"  # any file in project root; can be used for unit test 

    hash_value = calculate_sha256(test_file)

    if hash_value:
        print("SHA-256:", hash_value)
    else:
        print("Hashing failed")
