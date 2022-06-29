import unittest
import sys
sys.path.append('../')
    
from toyrobot.position import Position
from toyrobot.robot import Robot


class RobotTest(unittest.TestCase):
    def test_place(self):
        actual_robot = Robot(Position(0, 0), 'north', 4)
        self.assertEqual((0, 0, 'north'), (actual_robot.position.x, actual_robot.position.y, actual_robot.direction))

    def test_move(self):
        actual_robot = Robot(Position(0, 1), 'north', 4)
        actual_robot.move()
        self.assertEqual((0, 2, 'north'), (actual_robot.position.x, actual_robot.position.y, actual_robot.direction))

    def test_left(self):
        actual_robot = Robot(Position(2, 1), 'south', 4)
        actual_robot.left()
        self.assertEqual((2, 1, 'east'), (actual_robot.position.x, actual_robot.position.y, actual_robot.direction))

    def test_right(self):
        actual_robot = Robot(Position(2, 1), 'north', 4)
        actual_robot.right()
        self.assertEqual((2, 1, 'east'), (actual_robot.position.x, actual_robot.position.y, actual_robot.direction))

    def test_report(self):
        actual_robot = Robot(Position(4, 1), 'south', 4)
        actual_robot.report()
        self.assertEqual((4, 1, 'south'), (actual_robot.position.x, actual_robot.position.y, actual_robot.direction))
                         
    def test_place_outside(self):
        actual_robot = Robot(Position(5, 1), 'south', 4)
        self.assertEqual((5, 1, 'south'), (actual_robot.position.x, actual_robot.position.y, actual_robot.direction))
    
    def test_move_outside(self):
        actual_robot = Robot(Position(4, 5), 'west', 4)
        actual_robot.move()
        self.assertEqual((4, 5, 'west'), (actual_robot.position.x, actual_robot.position.y, actual_robot.direction))
    
    def test_move_outside_table(self):
        actual_robot = Robot(Position(4, 4), 'north', 4)
        actual_robot.move()
        self.assertEqual((4, 4, 'north'), (actual_robot.position.x, actual_robot.position.y, actual_robot.direction))
    
    def test_integrated(self):
        actual_robot = Robot(Position(2, 2), 'east', 4)
        actual_robot.move()
        actual_robot.right()
        actual_robot.right()
        actual_robot.move()
        actual_robot.left()
        self.assertEqual((2, 2, 'south'), (actual_robot.position.x, actual_robot.position.y, actual_robot.direction))

if __name__ == '__main__':
    unittest.main()
