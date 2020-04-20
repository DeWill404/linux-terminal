from datetime import datetime

import rain
import file

F = file.File()

while True:
    print(f"{F.curr()} $", end=" ")
    cmd = input()
    cmd_split = cmd.split()

    try:
        if cmd_split[0].lower() == "pwd":
            print(F.curr())

        elif cmd_split[0].lower() == "mkdir":
            print(F.make_dir(cmd_split[1]))

        elif cmd_split[0].lower() == "rmdir":
            print(F.remove_dir(cmd_split[1]))

        elif cmd_split[0].lower() == "cd":
            print(F.change_dir(cmd_split[1]))

        elif cmd_split[0].lower() == "cp":
            print(F.copy(cmd_split[1], cmd_split[2]))

        elif cmd_split[0].lower() == "mv":
            print(F.move(cmd_split[1], cmd_split[2]))

        elif cmd_split[0].lower() == "ren":
            print(F.rename(cmd_split[1], cmd_split[2]))

        elif cmd_split[0].lower() == "ls":
            if len(cmd_split) == 1:
                print(*F.list_folder(0), sep="  ")
            elif cmd_split[1].lower() == "-a":
                print(*F.list_folder(1), sep="  ")
            elif cmd_split[1].lower() == "-l":
                print(*F.list_folder(2), sep="\n")

        elif cmd_split[0].lower() == "date":
            date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            if len(cmd_split) == 1:
                print(date)
            else:
                if cmd_split[1].lower() == "-d":
                    print(date[:11])
                elif cmd_split[1].lower() == "-t":
                    print(date[11:])

        elif cmd_split[0].lower() == "touch":
            print(F.create(cmd_split[1]))

        elif cmd_split[0].lower() == "rm":
            print(F.delete(cmd_split[1]))

        elif cmd_split[0].lower() == "cat":
            print(F.list_file(cmd_split[1]))

        elif cmd_split[0].lower() == "nano":
            print(F.nano(cmd_split[1]))

        elif cmd_split[0].lower() == "python":
            print(F.run())

        elif cmd_split[0] == "man":
            print(F.manual())

        elif cmd_split[0] == "cmatrix":
            rain.Cmatrix()

        elif cmd_split[0] == "clear":
            F.clear()

        elif cmd.lower() == "exit":
            break

    except IndexError:
        print("-> Incomplete command <-")
