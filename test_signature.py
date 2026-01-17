from signatures.signature_checker import load_signatures, is_malicious

if __name__ == "__main__":
    sig_db = load_signatures("signatures/malware_signatures.txt")

    test_hash = "0b45700be478106a3d1612179856f5f29681e7903030b9647aa7f50b39655a4b" #this is for unit test. 

    # if is_malicious(sig_db):
    if is_malicious(test_hash, sig_db):
        print("Malware detected")
    else:
        print("File is clean")

