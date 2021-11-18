from robot import Robot


class CommandException(Exception):
    pass


class ExecuteCommandException(CommandException):
    pass


class Command:

    def __init__(self):
        # print('Command Class')
        # PLACE is a valid command, however it is also a composite command which will be validate in another way
        self.valid_commands = ['LEFT', 'RIGHT', 'MOVE', 'REPORT']
        self.robot = Robot()

    def execute(self, cmd: str) -> str:
        """
        Execute each valid command
        :param cmd:(str) command
        :return:(str)
        """
        try:
            if cmd.upper().startswith('PLACE'):

                cmd = cmd.replace('PLACE', '').replace(' ', '').upper()
                values = cmd.split(',')
                x = int(values[0])
                y = int(values[1])
                f = values[2]
                self.robot.place_robot(x, y, f)
            else:
                cmd = cmd.replace(' ', '').upper()
                if cmd in self.valid_commands:
                    if cmd == 'LEFT' or cmd == 'RIGHT':
                        self.robot.change_facing_position(cmd)

                    elif cmd == 'MOVE':
                        self.robot.move_robot()

                    elif cmd == 'REPORT':
                        return self.robot.report_position()
        except ValueError as v:
            raise ExecuteCommandException(f'Value provided not valid: {v}')
        except Exception as e:
            raise ExecuteCommandException(f'There was an issue while executing {cmd} : {e}')

    def command_list(self, command_lines: str) -> list:
        """
        Run over list of commands and execute them
        :param command_lines:(str) big string within all commands
        :return:(list)
        """
        try:
            results = []

            for cmd in command_lines.splitlines():
                result = self.execute(cmd)
                if result:
                    results.append(result)
            return results
        except ExecuteCommandException as ee:
            raise ee
        except Exception as e:
            raise CommandException(f"There was an issue when reading the commands: {e}")
