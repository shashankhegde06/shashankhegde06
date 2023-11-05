import os

def insecure_file_operation():
    file_path = "/etc/passwd"
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            content = file.read()
            print(content)

insecure_file_operation()
