import sys

from toyrobot.robot import Robot
from toyrobot.position import Position
from toyrobot.direction import Direction


class RobotRunner:
    @staticmethod
    def check_valid_place_cmd(cmd, direction_list):
        instruction = cmd[0]
        if instruction == 'PLACE':
            params = cmd[1].split(',')
            if len(params) == 3 and params[0].isdigit() and params[1].isdigit() and params[2] in direction_list:
                return [int(params[0]), int(params[1]), params[2]]
        return False

    def main(inputFile, outputFile):
        robot = Robot(Position(0, 0), 'NORTH', 4)
        direction_list = [d.name.upper() for d in Direction]

        with open(inputFile) as in_file, open(outputFile, 'w') as out_file:
            first_line = next(in_file)
            first_cmd = first_line.split()
            is_valid_cmd = RobotRunner.check_valid_place_cmd(
                first_cmd, direction_list)
            print(is_valid_cmd)
            if is_valid_cmd:
                robot.place(
                    Position(is_valid_cmd[0], is_valid_cmd[1]), is_valid_cmd[2])

                for line in in_file:
                    cmd = line.split()
                    params = cmd[0]
                    print("COMMAND----", params)
                    if params in {'MOVE', 'LEFT', 'RIGHT', 'REPORT', 'PLACE'}:
                        if params == 'PLACE':
                            is_valid_cmd = RobotRunner.check_valid_place_cmd(
                                cmd, direction_list)
                            if is_valid_cmd:
                                print(is_valid_cmd[0], is_valid_cmd[1])
                                robot.place(
                                    Position(is_valid_cmd[0], is_valid_cmd[1]), is_valid_cmd[2])
                            else:
                                print('ERROR: InvalidParameters')
                        elif params == 'REPORT':
                            out_file.write(robot.report())
                        else:
                            robot = getattr(robot, params.lower())()
                    else:
                        print('ERROR: InvalidCommand' + params)
            else:
                print('ERROR: First Command has to be PLACE')
