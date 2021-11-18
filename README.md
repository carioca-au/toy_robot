<h1 align="center">
  Toy Robot
</h1>

## 💻 Technologies and Requirements

- [PYTHON 3.9](https://www.python.org/downloads/release/python-390/)

## 📝 Description
The application is a simulation of a toy robot moving on a square tabletop, of dimensions 5 units x 5
units. There are no other obstructions on the table surface. The robot is free to roam around the
surface of the table, but must be prevented from falling to destruction. Any movement that would
result in the robot falling from the table must be prevented, however further valid movement
commands must still be allowed.


## 📝 Task
Create an application that can read in commands of the following form –

- PLACE X,Y,F
- MOVE
- LEFT
- RIGHT
- REPORT

PLACE will put the toy robot on the table in position X,Y and facing NORTH, SOUTH, EAST or WEST.
The origin (0,0) can be considered to be the SOUTH WEST most corner. The first valid command to
the robot is a PLACE command, after that, any sequence of commands may be issued, in any order,
including another PLACE command. The application should discard all commands in the sequence
until a valid PLACE command has been executed. MOVE will move the toy robot one unit forward in
the direction it is currently facing.
LEFT and RIGHT will rotate the robot 90 degrees in the specified direction without changing the
position of the robot.
REPORT will announce the X,Y and F of the robot. This can be in any form, but standard output is
sufficient.
A robot that is not on the table can choose the ignore the MOVE, LEFT, RIGHT and REPORT
commands. Input can be from a file, or from standard input, as the developer chooses. . Provide test
data to exercise the application.
Constraints: The toy robot must not fall off the table during movement. This also includes the initial
placement of the toy robot. Any move that would cause the robot to fall must be ignored.


## ⚙️ Setup & Run

### Clone the project
```sh
# git clone https://github.com/carioca-au/toy_robot.git
# cd toy_robot
``` 
### Install requirements
**project root**
```sh
# pip install -r requirements.txt
```
<br>
- There are 2 ways to see Toy Robot working:
  
- Python Unit Test, which there are 2 ways to provide new commands to the robot
    - 1st: Edit file that is under **tests -> data -> toy_test.txt** with different commands, always respecting one command per line.
    - 2nd: Go to the test.py file that is under **tests -> test.py** and change the values returned by the function **generate_entries**
- Run as Python script
  - Run the **input.py** script
    
### Running tests
**project root**
```sh
# python -m pytest
```

### Running the script
**project root**
```sh
# python input.py
```


Developed by **Rodrigo de Azevedo Carvalho** - [Linkedin](www.linkedin.com/in/rodrigo-de-azevedo-carvalho) - [GitHub](https://github.com/carioca-au)
