import math

class Body(object):
    def __init__(self, mass, position, velocity):
        if mass <= 0:
            # Use the correct error type
            raise RuntimeError("mass must be positive")

        self.mass = mass
        self.position = position
        self.velocity = velocity

    # Each "tick" of the clock is 1 millisecond
    def move(self):
        self.position = (self.position[0] + self.velocity[0] / 1000, self.position[1] + self.velocity[1] / 1000)

    def accelerate(self, a):
        self.velocity = (self.velocity[0] + a[0] / 1000, self.velocity[1] + a[1] / 1000)

    def distance_between(self, other_body):
        return other_body.distance_from(self.position)

    def distance_from(self, other_position):
        x_dist = self.position[0] - other_position[0]
        y_dist = self.position[1] - other_position[1]

        return math.sqrt(x_dist * x_dist + y_dist * y_dist)

    def unit_vec_between(self, other_body):
        return tuple(-num for num in other_body.unit_vec_towards(self.position))

    def unit_vec_towards(self, other_position):
        v = (other_position[0] - self.position[0], other_position[1] - self.position[1])
        magnitude = math.sqrt(v[0] * v[0] + v[1] * v[1]) # pop pop

        return (v[0] / magnitude, v[1] / magnitude)

    def midpoint_between(self, other_body):
        half_dist = self.distance_between(other_body) / 2
        unit_vec = self.unit_vec_between(other_body)

        x_pos = self.position[0]
        y_pos = self.position[1]

        return (x_pos + half_dist * unit_vec[0], y_pos + half_dist * unit_vec[1])

    def overlaps_with(self, other_body):
        midpoint = self.midpoint_between(other_body)
        # check if this body or the other contains the midpoint_between
        # TODO: does this make sense?
        return self.contains(midpoint) or other_body.contains(midpoint)

class RoundBody(Body):
    def __init__(self, mass, position, velocity, radius):
        if radius <= 0:
            raise RuntimeError("radius must be positive")
        super().__init__(mass, position, velocity)
        self.radius = radius

    def contains(self, point):
        return self.distance_from(point) <= self.radius

class SquareBody(Body):
    def __init__(self, mass, position, velocity, side_length):
        if side_length <= 0:
            raise RuntimeError("side length must be positive")

        super().__init__(mass, position, velocity)
        self.side_length = side_length

    def contains(self, point):
        x = self.position[0]
        y = self.position[1]
        right = x + self.side_length / 2
        left = x - self.side_length / 2
        top = y + self.side_length / 2
        bot = y - self.side_length / 2

        px = point[0]
        py = point[1]

        return px <= right and px >= left and py <= top and py >= bot
