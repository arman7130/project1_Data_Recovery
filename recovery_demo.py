def search_file(file_path, keyword):
    try:
        with open(file_path, "rb") as f:
            data = f.read()

        if keyword.encode() in data:
            print(f"[+] Found '{keyword}'")
        else:
            print("[-] Not found")

    except:
        print("Error reading file")

file_path = input("Enter file path: ")
keyword = input("Enter keyword: ")

search_file(file_path, keyword)
