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

    def gravitational_acceleration(self, r):
        return self.gravitational_parameter / r**2.0

    def surface_gravity(self, h=0.0):
        return self.gravitational_acceleration(self.radius + h)

    def equitorial_velocity(self, h=0.0):
        return self.angular_velocity * (self.radius + h)

    def escape_velocity(self):
        return math.sqrt( 2.0 * self.gravitational_parameter / self.radius )

    def geostationary_orbit(self):
        return Orbit.geostationary_orbit(self)
