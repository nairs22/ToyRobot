import sys

from toyrobot.robot import Robot
from toyrobot.position import Position
from toyrobot.direction import Direction

class RobotRunner:
    """ This class is runner class of robot.py. """

    command_list = ['move','left','right','report','place']
    direction_list = [d.name for d in Direction]    

    @staticmethod
    def check_valid_place_cmd(cmd):
        instruction = cmd[0].lower()
        if instruction == 'place':
            params = cmd[1].split(',')
            if len(params) == 3 and params[0].isdigit() and params[1].isdigit() and params[2].lower() in RobotRunner.direction_list:
                return [int(params[0]), int(params[1]), params[2]]
        return False

    def run(inputFile, outputFile):
        
        try:
            with open(inputFile) as in_file, open(outputFile, 'w') as out_file:
                #Checks whether the first line is a valid PLACE command
                first_line = next(in_file)
                first_cmd = first_line.split()
                is_valid_cmd = RobotRunner.check_valid_place_cmd(first_cmd)
                if is_valid_cmd:
                    robot=Robot(Position(is_valid_cmd[0], is_valid_cmd[1]), is_valid_cmd[2].lower())

                    for line in in_file:
                        cmd = line.split()
                        params = cmd[0].lower()
                        if params in RobotRunner.command_list:
                            if params == 'place':
                                is_valid_cmd = RobotRunner.check_valid_place_cmd(cmd)

                                if is_valid_cmd:
                                    robot.place(Position(is_valid_cmd[0], is_valid_cmd[1]), is_valid_cmd[2].lower())
                                else:
                                    print('ERROR: InvalidParameters')

                            elif params == 'report':
                                out_file.write(robot.report())

                            else:
                                robot = getattr(robot, params)() 
                        else:
                            print('ERROR: InvalidCommand ' + params)

                else:
                    print('ERROR: First Command has to be PLACE')
        except IOError as e:
            print ("I/O error({0}): {1}".format(e.errno, e.strerror))
        except: 
            print ("Unexpected error:", sys.exc_info()[0])