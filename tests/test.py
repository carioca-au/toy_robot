import unittest

from project.command import Command

BOUNDARY = '*********************************************************************************************************'


class Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('Global variables')
        cls.command = Command()

    def setUp(self):
        print('\n')
        print(BOUNDARY)
        print(self._testMethodName)
        print(BOUNDARY)

    @staticmethod
    def generate_entries():
        return ['PLACE 0,0, NORTH \n MOVE \n REPORT',
                'PLACE 0,0,NORTH \n LEFT \n REPORT',
                'PLACE 3,2,EAST \n MOVE \n MOVE \n LEFT \n MOVE \n REPORT',  # Invalid one
                'PLACE 1,2,EAST \n MOVE \n MOVE \n LEFT \n MOVE \n REPORT']

    def test_from_code(self):
        for commands in self.generate_entries():
            results = self.command.command_list(commands)
            if results:
                for result in results:
                    print(result)

    def test_from_file(self):
        # Add your path here
        path = self.command.open_file("C:\\Users\\Rodrigo\Documents\\toy_test.txt")
        results = self.command.command_list(path)
        if results:
            for result in results:
                print(result)


if __name__ == '__main__':
    unittest.main()
