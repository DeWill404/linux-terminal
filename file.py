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
            return name + " already exit...."
        else:
            f = open(name, "w+")  # Create new file
            f.close()
            return "Success"

    # To delete file
    def delete(self, name):
        name = self.current + os.sep + name   # Appending to current
        if os.path.isfile(name):        # If file exit
            os.remove(name)             # Delete
            return "Success"
        return "Invalid"

    # List content of file
    def list_file(self, name):
        name = self.current + os.sep + name       # Appending to current
        if os.path.isfile(name):            # If file exit
            file = open(name, "r+")         # open file
            print(file.read(), end="")      # read file
            file.close()
            return "Success"
        return "Invalid file"

    # To run python file
    def run(self):
        self.nano("temp")                   # Create temporary file
        file = open(self.root + '/temp', "r")  # Open it
        try:
            exec(file.read())               # Execute file
            self.delete("temp")             # Delete it
            return "Success"
        except :
            self.delete("temp")
            return "Error"

    # To write content in file
    def nano(self, name):
        self.create(name)       # Create file if does not exit
        os.system("clear")      # Clear Screen
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
        os.system("clear")
        file.close()
        return f"{name.replace(self.root,os.sep)} is edited successfully"

    def manual(self):
        name = "manual.txt"
        try:
            os.system("clear")
            f = open(name, "r")
            return f.read()
        except FileNotFoundError:
            return "Invalid"
