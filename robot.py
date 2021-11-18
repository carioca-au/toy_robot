class RobotException(Exception):
    pass


class Robot:

    def __init__(self):
        self.robot_position = self.reset_position()
        self.last_position = self.robot_position

        self.face_positions = {'NORTH': 0, 'SOUTH': 2, 'EAST': 1, 'WEST': 3}
        self.rotation_directions = ['LEFT', 'RIGHT']

    @staticmethod
    def reset_position() -> dict:
        """
        Restart on position 0
        """
        # First Position
        return {'x': 0, 'y': 0, 'f': 0}

    def place_robot(self, x: int, y: int, face: str) -> None:
        """
        Place the robot in the right place or skip if out of the board
        :param x:(int)
        :param y:(int)
        :param face:(str)
        :return:(None)
        """
        try:
            # ensure that face is always uppercase
            face = face.upper()

            # Validates if the position is in the grid and if it's a valid face
            if face in self.face_positions.keys() and 4 > x >= 0 and 4 > y >= 0:
                self.robot_position = {'x': x, 'y': y, 'f': self.face_positions[face]}
            else:
                # There is no instructions to print any value in case of invalid command,
                # it should just skip in case of out of the board
                # print('Invalid move, therefore ignored!')
                pass

        except Exception as e:
            raise RobotException(f"There was an exception trying to place the robot: {e}")

    def move_robot(self) -> None:
        """
        Move Robot
        """
        new_position = self.robot_position.copy()
        move_direction = new_position['f']

        # North
        if move_direction == 0:
            new_position['y'] += 1

        # South
        elif move_direction == 2:
            new_position['y'] -= 1

        # East
        elif move_direction == 1:
            new_position['x'] += 1

        # West
        elif move_direction == 3:
            new_position['x'] -= 1

        # Set new position
        face_position = self.get_name_face_position(new_position['f'])
        self.place_robot(new_position['x'], new_position['y'], face_position)

    def change_facing_position(self, direction: str) -> None:
        """
        Rotates the robot accordingly to the direction informed
        :param direction:(str) LEFT/RIGHT
        :return:
        """
        if direction.upper() in self.rotation_directions:
            if direction.upper() == 'LEFT':
                self.robot_position['f'] = self.robot_position['f'] - 1 if 0 < self.robot_position['f'] else 3
            else:
                self.robot_position['f'] = self.robot_position['f'] + 1 if 3 > self.robot_position['f'] else 0

    def get_name_face_position(self, position=None) -> str:
        """
        Retrieve string with the Robot's face direction
        :param position:
        :return:(str) Robot's face direction
        """
        return [
            k
            for k, v in self.face_positions.items()
            if v == (position or self.robot_position['f'])
        ][0]

    def report_position(self) -> str:
        """
        Report robot position
        :return: (str)
        """
        return f'{self.robot_position["x"]}, {self.robot_position["y"]}, {self.get_name_face_position()}'
