FILE_NAME = "todos.txt"

def get_todos(file_path=FILE_NAME):
    """Read a text file and return the list of
    to-do items"""
    with open(file_path, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILE_NAME ):
    """Write data into the todos.txt after edited"""
    with open(filepath, "w") as file_w:
        file_w.writelines(todos_arg)

# if __name__ == "__main__":
#     print("hello")
#     print(get_todos())