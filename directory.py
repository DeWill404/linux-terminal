import os
import shutil
import time


class File:
    def __init__(self):
        self.root = os.getcwd() + "/" + "asset"     # Location of root folder
        self.current = self.root                    # Pointer to current folder
        if not os.path.exists(self.root):           # If root does not exit
            os.mkdir(self.root)                     # Create asset as root

    # Trimming current path name & returning it
    def curr(self):
        return self.current.replace(self.root, "/")

    # Making directory
    def make_dir(self, name):
        dir_path = self.current + "/" + name
        if os.path.exists(dir_path):
            return name + " Directory already exit..."
        else:
            try:
                os.mkdir(dir_path)
                return "Success"
            except:
                return "Invalid"

    # Removing directory
    def remove_dir(self, name):
        dir_path = self.current + "/" + name
        # If directory with name exit
        if os.path.exists(dir_path) and os.path.isdir(dir_path):
            if (name != "..") and (name != "."):
                shutil.rmtree(dir_path)
                return "Success"
        else:
            return "Invalid"

    # Changing current directory
    def change_dir(self, name):
        temp = self.current     # Making a temporary copy
        if os.path.exists(self.current + "/" + name) and os.path.isdir(self.current + "/" + name):
            if '/' in name:     # If path contain multilevel of directories
                name = name.split("/")  # Getting individual folder name
                if "" in name:          # Remove "" after last / in present
                    name.remove("")
                for i in name:          # Moving in and out of directory
                    if (i != "..") and (i != "."):
                        temp += '/' + i
                    elif i == "..":
                        temp = temp[:temp.rfind("/")]
            else:
                if name == "..":    # exiting current directory
                    temp = temp[:temp.rfind("/")]
                elif name != ".":   # . is same as current level
                    temp += '/' + name
            if self.root in temp:   # If you are inside root directory
                self.current = temp
                return "Success"
        return "Invalid"

    # List content of current directory
    def list_content(self, show):
        # for showing hidden file
        if show == 0:
            lis = [i for i in os.listdir(self.current) if i[0] != '.']
            return lis
        # For showing details
        elif show == 2:
            lis = os.listdir(self.current)
            for i in range(len(lis)):
                lis[i] = self.current + '/' + lis[i]
                t = time.ctime(os.path.getctime(lis[i]))[4:]
                s = os.path.getsize(lis[i])
                lis[i] = str(s) + "   " + t + "   " + lis[i].replace(self.root, "/")
            return lis
        # for not showing hidden file
        else:
            return os.listdir(self.current)

    # Moving directory or file to other
    def move(self, orignal, target):
        temp = orignal     # making copy of orignal
        orignal = self.current + "/" + orignal
        target = self.current + "/" + target
        # Can't make change with current or parent file
        if temp != "./" and temp != "../":
            if os.path.exists(orignal) or os.path.isfile(orignal):
                if os.path.exists(target):
                    # Can't go outside root directory
                    if (self.root in orignal) and (self.root in target):
                        # if you want to move file, append filename in target
                        if os.path.isfile(orignal):
                            target += orignal[orignal.rfind("/")+1:]
                        target = r'{}'.format(target)       # Encoding
                        orignal = r'{}'.format(orignal)     # Encoding
                        shutil.move(orignal, target)
                        return "Success"
        return "Invalid"

    # To copy one directory to other
    def copy(self, orignal, target):
        temp = orignal     # making copy of orignal
        orignal = self.current + "/" + orignal
        target = self.current + "/" + target
        # Can't make change with current or parent file
        if temp != "./" and temp != "../":
            if os.path.exists(orignal) or os.path.isfile(orignal):
                if os.path.exists(target):
                    # Can't go outside root directory
                    if (self.root in orignal) and (self.root in target):
                        target = r'{}'.format(target)       # Encoding
                        orignal = r'{}'.format(orignal)     # Encoding
                        shutil.copy(orignal, target)
                        return "Success"
        else:
            return "Invalid"

    # Renaming file and directory
    def rename(self, original, target):
        if '/' not in target:
            original = self.current + "/" + original
            target = self.current + "/" + target
            if os.path.exists(original) or os.path.isfile(original):
                if self.root in original:
                    os.rename(original, target)
                    return "Success"
        return "Invalid"
















