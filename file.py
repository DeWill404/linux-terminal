import os
import directory


class File(directory.Folder):
    # Constructor to call and set parent attributes
    def __init__(self):
        super().__init__()

    # To create new file
    def create(self, name):
        name = self.current + os.sep + name  # Appending to current
        if os.path.isfile(name):  # If file already exit
            return name.replace(self.root, os.sep) + " already exist...."
        else:
            f = open(name, "w+")  # Create new file
            f.close()
            return "File successfully created..."

    # To delete file
    def delete(self, name):
        name = self.current + os.sep + name   # Appending to current
        if os.path.isfile(name):        # If file exit
            os.remove(name)             # Delete
            return "File successfully removed......"
        return "Invalid file location........"

    # List content of file
    def list_file(self, name):
        name = self.current + os.sep + name       # Appending to current
        if os.path.isfile(name):            # If file exit
            file = open(name, "r+")         # open file
            print(end="\n")                 # SEPARATOR
            print(file.read(), end="")      # read file
            file.close()
            print(end="\n")                 # SEPARATOR
            return "Success"
        return "Invalid"

    # To run python file
    def run(self):
        self.nano("temp.py")                   # Create temporary file
        file = open(self.root + os.sep + "temp.py", "r")  # Open it
        try:
            exec(file.read())                  # Execute file
            self.delete("temp.py")             # Delete it
        except :
            self.delete("temp.py")

    # To write content in file
    def nano(self, name):
        self.create(name)       # Create file if does not exit
        self.clear()      # Clear Screen
        # Open text editor
        print(f"{name.replace(self.root,os.sep)} is opened, Ctrl-D to save it.")
        name = self.current + os.sep + name
        if os.path.getsize(name) != 0:      # If file is not empty
            file = open(name, "r+")
            print(file.read(), end="")
            file.close()
            file = open(name, "a+")
        else:                               # If file is empty
            file = open(name, "w+")
        while True:
            try:
                file.write(input()+"\n")
            except EOFError:
                break
        self.clear()
        file.close()
        return f"{name.replace(self.root,os.sep)} is edited successfully"

    def manual(self):
        name = "manual.txt"
        try:
            self.clear()
            f = open(name, "r")
            return f.read()
        except FileNotFoundError:
            return "Sorry, Manual is missing..."

