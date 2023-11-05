def secure_file_operation():
    file_path = "/etc/passwd"
    try:
        with open(file_path, "r") as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")

secure_file_operation()
