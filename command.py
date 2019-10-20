from project.robot import Robot


class Command:

    def __init__(self):
        # print('Command Class')
        # PLACE is a valid command, however it is also a composite command which will be validate in another way
        self.valid_commands = ['LEFT', 'RIGHT', 'MOVE', 'REPORT']
        self.robot = Robot()

    def execute(self, cmd):
        try:
            if cmd.startswith('PLACE'):

                cmd = cmd.replace('PLACE', '').replace(' ', '')
                values = cmd.split(',')
                x = values[0]
                y = values[1]
                f = values[2]
                self.robot.place_robot(x, y, f)
            else:
                cmd = cmd.replace(' ', '')
                if cmd in self.valid_commands:
                    if cmd == 'LEFT' or cmd == 'RIGHT':
                        self.robot.change_facing_position(cmd)

                    elif cmd == 'MOVE':
                        self.robot.move_robot()

                    elif cmd == 'REPORT':
                        return self.robot.report_position()
        except Exception as e:
            # print(e)
            pass

    def command_list(self, command_lines):
        try:
            results = []

            for cmd in command_lines.splitlines():
                result = self.execute(cmd)
                if result:
                    results.append(result)
            return results
        except Exception as e:
            pass

    def open_file(self, file_path):
        try:
            f = open(file_path, "r")
            contents = f.read()
            return contents
        except Exception as e:
            pass
