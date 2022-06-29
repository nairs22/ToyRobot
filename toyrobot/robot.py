from toyrobot.move import Move
from toyrobot.direction import Direction


class Robot:
    def __init__(self, position, direction='NORTH', table_size=4):
        self.position = position
        self.direction = direction.upper()
        self.table_size = table_size

    def is_valid_position(f):
        def wrapper(self, position, direction):
            if 0 <= position.x <= self.table_size and 0 <= position.y <= self.table_size:
                return f(self, position, direction)
            return self

        return wrapper

    @is_valid_position
    def place(self, position, direction):
        print('place', str(position.x), str(
            position.y), direction)
        self.position = position
        self.direction = direction.upper()
        return self

    def move(self):
        print("move",  Move[self.direction.lower()].value)
        newPosition = self.position.add(Move[self.direction.lower()].value)
        return self.place(newPosition, self.direction)

    def calculate_compass_degree(f):
        def wrapper(self):
            compass_degree = Direction[self.direction.lower()].value
            return f(self, compass_degree)
        return wrapper

    @calculate_compass_degree
    def left(self, compass_degree):
        print("LEFT", compass_degree)
        new_compass_degree = compass_degree-90 if compass_degree != 0 else 270
        return self.place(self.position, Direction(new_compass_degree).name)

    @calculate_compass_degree
    def right(self, compass_degree):
        print("RIGHT")
        new_compass_degree = compass_degree + 90 if compass_degree != 270 else 0
        return self.place(self.position, Direction(new_compass_degree).name)

    def report(self):
        print('REPORT', str(self.position.x), str(
            self.position.y), self.direction)
        return ' '.join([str(self.position.x), str(self.position.y), self.direction, '\n'])
