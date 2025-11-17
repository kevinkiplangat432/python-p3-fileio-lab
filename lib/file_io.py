def write_file(file_name, file_content):
    new_file_name = f"{file_name}.txt"
    with open(new_file_name, mode="w") as file:
        file.write(file_content)

def append_file(file_name, append_content):
    new_file_name = f"{file_name}.txt"
    with open(new_file_name, mode= "a") as file:
        file.write("\n" + append_content) #\n for a new line in the file

def read_file(file_name):
    new_file_name =f"{file_name}.txt"
    with open(new_file_name, modec ="r"):
        file.open()
