from toyrobot.move import Move
from toyrobot.direction import Direction


class Robot:
    """ This class is responsible to perform all robot actions. 

    Attributes:
        position (object): Position of robot.
        direction (str): Direction of robot.
        table_size (int): Maximum size of the table. Default is 4. Table is a square.
    """

    def __init__(self, position, direction='north', table_size = 4):
        self.position = position
        self.direction = direction
        self.table_size = table_size

    def is_valid_position(f):
        def wrapper(self, position, direction):
            if 0 <= position.x <= self.table_size and 0 <= position.y <= self.table_size:
                return f(self, position, direction)
            return self

        return wrapper

    @is_valid_position
    def place(self, position, direction):
        """Updates the robot position only if its valid""" 
        self.position = position
        self.direction = direction
        return self

    def move(self):
        newPosition = self.position.add(Move[self.direction.lower()].value)
        return self.place(newPosition, self.direction)

    def calculate_compass_degree(f):
        def wrapper(self):
            compass_degree = Direction[self.direction.lower()].value
            return f(self, compass_degree)
        return wrapper

    @calculate_compass_degree
    def left(self, compass_degree):
        """Calculates the new_degree based on the direction and updates the robot position""" 
        new_compass_degree = compass_degree - 90 if compass_degree != 0 else 270
        return self.place(self.position, Direction(new_compass_degree).name)

    @calculate_compass_degree
    def right(self, compass_degree):
        """Calculates the new_degree based on the direction and updates the robot position""" 
        new_compass_degree = compass_degree + 90 if compass_degree != 270 else 0
        return self.place(self.position, Direction(new_compass_degree).name)

    def report(self):
        return ' '.join([str(self.position.x), str(self.position.y), self.direction.upper(), '\n'])
