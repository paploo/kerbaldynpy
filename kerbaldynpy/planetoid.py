import math

class Planetoid(object):

    def __init__(self, name, gravitational_parameter, radius=0.0, angular_velocity=0.0):
        self.name = name
        self.gravitational_parameter = gravitational_parameter
        self.radius = radius
        self.angular_velocity = angular_velocity

    @property
    def rotational_period(self):
        return 2.0 * math.pi / self.angular_velocity

    @rotational_period.setter
    def rotational_period(self, rotational_period):
        self.angular_velocity = 2.0 * math.pi / rotational_period

if __name__ == '__main__':
    p = Planetoid('jeff', 1024, radius=3.0)
    print p
    print p.orbital_parameters
