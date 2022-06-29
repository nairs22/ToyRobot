import os
import sys
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))
    
from toyrobot.position import Position
from toyrobot.direction import Direction
from toyrobot.move import Move
from toyrobot.robot import Robot
import unittest

class RobotTest(unittest.TestCase):
    def test_place(self):
        actual_robot = Robot(Position(0, 0), 'NORTH', 4)
        self.assertEqual((0, 0, 'NORTH'), (actual_robot.position.x,
                         actual_robot.position.y, actual_robot.direction))

    def test_move(self):
        actual_robot = Robot(Position(0, 1), 'NORTH', 4)
        actual_robot.move()
        self.assertEqual((0, 2, 'NORTH'), (actual_robot.position.x,
                         actual_robot.position.y, actual_robot.direction))

    def test_left(self):
        actual_robot = Robot(Position(2, 1), 'EAST', 4)
        actual_robot.left()
        self.assertEqual((2, 1, 'NORTH'), (actual_robot.position.x,
                         actual_robot.position.y, actual_robot.direction))

    def test_right(self):
        actual_robot = Robot(Position(2, 1), 'NORTH', 4)
        actual_robot.right()
        self.assertEqual((2, 1, 'EAST'), (actual_robot.position.x,
                         actual_robot.position.y, actual_robot.direction))

    def test_report(self):
        actual_robot = Robot(Position(4, 1), 'SOUTH', 4)
        actual_robot.report()
        self.assertEqual((4, 1, 'SOUTH'), (actual_robot.position.x,
                         actual_robot.position.y, actual_robot.direction))
                         
    def test_place_outside(self):
        actual_robot = Robot(Position(5, 1), 'SOUTH', 4)
  
        self.assertEqual((4, 1, 'SOUTH'), (actual_robot.position.x,
                         actual_robot.position.y, actual_robot.direction))

if __name__ == '__main__':
    unittest.main()
