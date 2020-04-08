class Create:
    # Create directory with name, next, back
    # child is for moving in directory
    # parent is for moving out of directory
    # length is for no. of files in directory
    def __init__(self, name):
        self.name = name
        self.next = None
        self.back = None
        self.child = File()
        self.parent = None
        self.length = 0


class File:
    def __init__(self):
        self.head = None    # Initializing Empty folder
        self.root = "Root"

    # Setting up root folder
    def setup(self):
        self.add_node(self.root)   # Add root directory
        self.movedown()            # Move in root folder

    # Selecting a particular folder
    def select(self, name):
        if self.head.parent is None:    # if head is root, so there won't be any adjacent file
            return -1
        else:
            temp = self.head        # Selecting head
            for i in range(self.head.parent.length):    # Iteration
                if temp.name == name:                   # If found
                    self.head = temp
                    return 1
                temp = temp.next
            return 0

    # getting name of current folder
    def getname(self):
        return self.head.name

    # getting name of parent folder
    def get_parentname(self):
        return self.head.parent.name

    # Moving to parent directory
    def moveup(self):
        if self.head.parent is None:        # If reached on root node
            return -1
        self.head = self.head.parent

    # Moving to child directory
    def movedown(self):
        if self.head.child.head is None:    # If reached on leaf node
            return -1
        self.head = self.head.child.head

    # Adding files on same level
    def add_node(self, name):
        if self.head is None:           # If directory is empty
            self.head = Create(name)    # x
            self.head.next = self.head  # x-x
            self.head.back = self.head  # x-x-x
            self.add_child(".")         # Create '.' file for newnode
            self.add_child("..")        # Create '..' file for newnode
        elif self.head.parent is None:  # If current node is root then exit
            return -1
        else:
            temp = self.head            # Selecting head
            parent = self.head.parent   # Selecting parent

            # Check if already exit
            for i in range(parent.length):
                if temp.name == name:
                    return -1
                temp = temp.next

            # New Node creating
            newnode = Create(name)          # N
            newnode.parent = parent         # Connecting to parent
            newnode.next = self.head        # N-A
            newnode.back = self.head.back   # B-N-A
            self.head.back.next = newnode   # B=N-A
            self.head.back = newnode        # B=N=A
            parent.length += 1              # length++

    # delete files on same level
    def delete_node(self, name):
        if self.head.parent is None:   # Current directory is root then exit
            return -1
        elif (name == ".") or (name == ".."):   # if user want to delete "." or ".." folder
            return -1
        else:
            temp = self.head            # Selecting Head
            parent = self.head.parent   # Selecting Parent

            for i in range(parent.length):   # Iterating to each object
                if temp.name == name:               # If found
                    temp.next.back = temp.back      # break back link
                    temp.back.next = temp.next      # break next link
                    temp = None              # delete file
                    parent.length -= 1       # Decrease length
                    return 1
                temp = temp.next

        return 0

    # List all file on same level
    def list_file(self, reverse):
        if self.head.parent is None:
            return -1
        else:
            lis = []            # Empty list
            temp = self.head    # Selecting head

            for i in range(self.head.parent.length):    # Iteration
                lis.append(temp.name)                   # Append
                temp = temp.next

            if reverse == 0:
                return lis
            else:
                return sorted(lis, reverse=True)

    # Adding files on same level
    def add_child(self, name):
        if self.head.child.head is None:
            self.head.child.head = Create(name)     # X
            temp = self.head.child.head             # Shortcut
            temp.parent = self.head                 # Connecting to parent
            temp.next = temp                        # X-x
            temp.back = temp                        # x-X-x
        else:
            temp = self.head.child.head     # Select Child head

            # Check if already exit
            for i in range(self.head.length):
                if temp.name == name:
                    return -1
                temp = temp.next

            # New Node creating
            temp = self.head.child.head     # Shortcut
            newnode = Create(name)          # N
            newnode.parent = self.head      # Connecting t parent
            newnode.next = temp             # N-A
            newnode.back = temp.back        # B-N-A
            temp.back.next = newnode        # B=N-A
            temp.back = newnode             # B=N=A
        self.head.length += 1   # length++

    # delete files on base level
    def delete_child(self, name):
        if (name == ".") or (name == ".."):   # if list is empty
            return -1
        else:
            temp = self.head.child.head      # Selecting child head
            parent = self.head               # Selecting Parent

            for i in range(parent.length):   # Iterating to each object
                if temp.name == name:           # If found
                    temp.next.back = temp.back
                    temp.back.next = temp.next
                    temp = None
                    parent.length -= 1
                    return 1
                temp = temp.next

            return 0

    # List all file on same level
    def list_child(self, reverse):
        if (self.head is None) or (self.head.child.head is None):   # if list empty
            return -1
        else:
            lis = []                        # Empty list
            temp = self.head.child.head     # Selecting child head
            parent = self.head              # Selecting head

            for i in range(parent.length):
                lis.append(temp.name)
                temp = temp.next

            if reverse == 0:
                return lis
            else:
                return sorted(lis, reverse=True)
