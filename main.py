from datetime import datetime

import directory
import rain

direc = directory.File()

while True:
    print(f"{direc.curr()} $", end=" ")
    cmd = input()
    cmd_split = cmd.split()

    if cmd_split[0].lower() == "pwd":
        print(direc.curr())

    elif cmd_split[0].lower() == "mkdir":
        print(direc.make_dir(cmd_split[1]))

    elif cmd_split[0].lower() == "rmdir":
        print(direc.remove_dir(cmd_split[1]))

    elif cmd_split[0].lower() == "cd":
        print(direc.change_dir(cmd_split[1]))

    elif cmd_split[0].lower() == "cp":
        print(direc.copy(cmd_split[1], cmd_split[2]))

    elif cmd_split[0].lower() == "mv":
        print(direc.move(cmd_split[1], cmd_split[2]))

    elif cmd_split[0].lower() == "ren":
        print(direc.rename(cmd_split[1], cmd_split[2]))

    elif cmd_split[0].lower() == "ls":
        if len(cmd_split) == 1:
            print(*direc.list_content(0), sep="  ")
        elif cmd_split[1].lower() == "-a":
            print(*direc.list_content(1), sep="  ")
        elif cmd_split[1].lower() == "-l":
            print(*direc.list_content(2), sep="\n")

    elif cmd_split[0].lower() == "date":
        date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        if len(cmd_split) == 1:
            print(date)
        else:
            if cmd_split[1].lower() == "-d":
                print(date[:11])
            elif cmd_split[1].lower() == "-t":
                print(date[11:])

    elif cmd_split[0] == "cmatrix":
        rain.Cmatrix()

    if cmd.lower() == "exit":
        break
