import math

class Planetoid(object):

    def __init__(self, name, gravitational_parameter, radius=0.0, rotational_period=None, angular_velocity=0.0):
        self.name = name
        self.gravitational_parameter = gravitational_parameter
        self.radius = radius

        if rotational_period:
            self.rotational_period = rotational_period
        else:
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


KERBOL = Planetoid('Kerbol', 1172332794832492300.0, 261600000)

KERBIN = Planetoid('Kerbin', 3531600000000.0, 600000.0, 21600.0)
MUN = Planetoid('Mun', 65138397520.7806, 200000.0, 138984.376574476)
MINMUS = Planetoid('Minmus', 1765800026.31247, 60000.0, 40400.0)

DUNA = Planetoid('Duna', 301363211975.098, 320000.0, 65517.859375)
IKE = Planetoid('Ike', 18568368573.1441, 130000.0, 65517.8621348081)

MOHO = Planetoid('Moho', 245250003654.51, 250000.0, 2215754.21968432)

EVE = Planetoid('Eve', 8171730229210.85, 700000.0, 80500.0)
GILLY = Planetoid('Gilly', 8289449.81471635, 13000.0, 28255.0)

JOOL = Planetoid('Jool', 282528004209995.0, 6000000.0, 36000.0)
VALL = Planetoid('Vall', 207481499473.751, 300000.0, 105962.088893924)
LAYTHE = Planetoid('Laythe', 1962000029236.08, 500000.0, 52980.8790593796)
TYLO = Planetoid('Tylo', 2825280042099.95, 600000.0, 211926.35802123)
BOP = Planetoid('Bop', 2486834944.41491, 65000.0, 12950.0)


planetoids = [KERBOL, KERBIN, MUN, MINMUS, DUNA, IKE, MOHO, EVE, GILLY, JOOL, VALL, LAYTHE, TYLO, BOP]
PLANETOIDS = dict(((p.name,p) for p in planetoids))
