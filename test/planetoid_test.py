import testhelper

import kerbaldynpy.planetoid

class TestPlanetoid(testhelper.KerbalDynTestCase):

    def setUp(self):
        self.earth = kerbaldynpy.planetoid.Planetoid('Earth', 398600.4418e9, radius=6378.1e3, angular_velocity=7.2921150e-5)

    def test_get_name(self):
        self.assertEqual('Earth', self.earth.name)

    def test_get_gravitational_parameter(self):
        self.assertWithinError(398600.4418e9, self.earth.gravitational_parameter)

    def test_get_radius(self):
        self.assertWithinError(6378.1e3, self.earth.radius)

    def test_get_rotational_period(self):
        self.assertWithinError(86164.091, self.earth.rotational_period)

    def test_set_rotational_period(self):
        period = 62.83185307179586
        self.earth.rotational_period = period
        self.assertWithinError(period, self.earth.rotational_period)
        self.assertWithinError(0.10, self.earth.angular_velocity)
