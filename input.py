from project.command import Command


def command_input():
    command = Command()
    asked = False
    while True:
        try:
            print("Type the command EXIT to quit anytime")
            q1 = None
            if not asked:
                q1 = input("Would you like to import a file? [Y/N]")
                asked = True
                if q1 not in ["Y", "EXIT", "N"]:
                    print("Invalid option")
                    break
                if q1 == "Y":
                    q2 = input("Could you inform the file path, please?")
                    if q2:
                        path = command.open_file(q2)
                        results = command.command_list(path)
                        if results:
                            for result in results:
                                print(result)
                        break
                    else:
                        print("Invalid path")
                        break
            if not q1 or q1 != "EXIT":
                q1 = input("Input your command, please")
                result = command.execute(q1)
                if result:
                    print(result)
                    break

            if q1 == "EXIT":
                break

        except ValueError:
            print("Error! This value is not valid. Try again.")
        except Exception as e:
            print("Error! {0}".format(e))


command_input()
