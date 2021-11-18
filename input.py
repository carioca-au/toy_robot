import sys
from pathlib import Path

from command import Command
from utils import open_file


def import_file(command_exec: Command):
    command = ''
    while command.upper() != 'EXIT' and command.upper() != 'N':
        command = input("Would you like to import a file? [Y/N]")

        if command.upper() not in ["Y", "EXIT", "N"]:
            print("Invalid option")
            continue
        if command.upper() == "Y":
            path = input("Could you inform the file path, please?")
            if path:
                file = open_file(Path(path))
                results = command_exec.command_list(file)
                if results:
                    [print(result) for result in results]
                    print('Game Over!')
                sys.exit(0)
            else:
                print("Invalid path")
                continue


def command_input():
    command_exec = Command()
    command = ''
    print("Type the command EXIT to quit anytime")
    import_file(command_exec)

    while command.upper() != 'EXIT':
        try:
            command = input("Type a valid command, please (default REPORT)") or 'REPORT'
            result = command_exec.execute(command)
            if result:
                print(result)
                continue

        except ValueError:
            print("Error! This value is not valid. Try again.")
        except Exception as e:
            print("Error! {0}".format(e))

    print('Exited')
    print('Game Over!')


command_input()
