'''
A robot moves in a plane starting from the original point (0,0). The
robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. The
trace of robot movement is shown as the following:

UP 5
DOWN 3
LEFT 3
RIGHT 2
­
The numbers after the direction are steps. Please write a program to
compute the distance from current position after a sequence of movement
and original point. If the distance is a float, then just print the
nearest integer.

Solution should be 2

https://github.com/zhiwehu/Python-programming-exercises/blob/master/100%2B%20Python%20challenging%20programming%20exercises.txt#L570
'''


class Robot:

    def __init__(self):
        self.x = 0
        self.y = 0

    def move(self, instructions):
        direction, distance = instructions.split(' ')
        distance = int(distance)
        if direction == 'UP':
            self.y = self.y + distance
        elif direction == 'DOWN':
            self.y = self.y - distance
        elif direction == 'LEFT':
            self.x = self.x - distance
        elif direction == 'RIGHT':
            self.x = self.x + distance
        else:
            raise AssertionError('Direction not found')

    def position(self):
        return int(((self.x ** 2) + (self.y ** 2)) ** (0.5))


def test_robot():
    robot = Robot()
    robot.move('UP 5')
    robot.move('DOWN 3')
    robot.move('LEFT 3')
    robot.move('RIGHT 2')
    assert robot.position() == 2, robot.position()


if __name__ == '__main__':
    test_robot()
