class Robot:

    def __init__(self):
        # print('Ini ROBOT')

        self.robot_position = self.reset_position()
        self.last_position = self.robot_position

        self.face_positions = {'NORTH': 0, 'SOUTH': 2, 'EAST': 1, 'WEST': 3}
        self.rotation_directions = ['LEFT', 'RIGHT']

    @staticmethod
    def reset_position():
        # First Position
        return {'x': 0, 'y': 0, 'f': 0}

    def place_robot(self, x, y, f):
        try:
            if not isinstance(x, int):
                x = int(x)
            if not isinstance(y, int):
                y = int(y)

            if self.validate_place_position(x, y, f):
                self.robot_position = {'x': x, 'y': y, 'f': self.face_positions[f]}
                return True

            # print('Invalid move, therefore ignored!')
            return False
        except Exception as e:
            # print(e)
            pass

    def validate_place_position(self, x, y, f):
        valid = True

        if f not in self.face_positions.keys():
            # print('Face position invalid! Please select among {0}'.format(self.face_positions))
            valid = False

        elif x > 4 or x < 0:
            # print('Horizontal move invalid!')
            valid = False

        elif y > 4 or y < 0:
            # print('Vertical move invalid!')
            valid = False
        return valid

    def move_robot(self):
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

        face_position = self.get_name_face_position(new_position['f'])
        if self.place_robot(new_position['x'], new_position['y'], face_position):
            # print('Move successfully done!')
            pass

    def change_facing_position(self, direction):

        if self.validate_rotation_directions(direction):

            if direction == 'LEFT':
                if 0 < self.robot_position['f']:
                    self.robot_position['f'] -= 1
                elif self.robot_position['f'] == 0:
                    self.robot_position['f'] = 3

            else:
                if 3 > self.robot_position['f']:
                    self.robot_position['f'] += 1
                elif self.robot_position['f'] == 3:
                    self.robot_position['f'] = 0

    def validate_rotation_directions(self, directions):
        if directions not in self.rotation_directions:
            # print('Rotation Command Invalid!')
            return False
        return True

    def get_name_face_position(self, position=None):
        if position is None:
            position = self.robot_position['f']

        for k, v in self.face_positions.items():
            if v == self.robot_position['f']:
                return k

    def report_position(self):
        return '{0}, {1}, {2}'.format(self.robot_position['x'], self.robot_position['y'], self.get_name_face_position())
