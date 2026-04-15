def search_file(file_path, keyword):
    try:
        with open(file_path, "rb") as f:
            data = f.read()

        print("\n[INFO] Scanning file for keyword...")

        if keyword.encode() in data:
            print(f"[SUCCESS] Keyword '{keyword}' found in file")
        else:
            print(f"[FAIL] Keyword '{keyword}' not found")

    except FileNotFoundError:
        print("[ERROR] File not found. Check the path.")
    except Exception as e:
        print("[ERROR] Something went wrong:", e)


print("=== Lost Data Retrieval Demo ===")

file_path = input("Enter file path: ")
keyword = input("Enter keyword to search: ")

search_file(file_path, keyword)

