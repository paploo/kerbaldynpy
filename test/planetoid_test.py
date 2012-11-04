import testhelper

import kerbaldynpy

class TestPlanetoid(testhelper.KerbalDynTestCase):

    def setUp(self):
        self.earth = kerbaldynpy.Planetoid('Earth', 398600.4418e9, radius=6378.1e3, angular_velocity=7.2921150e-5)

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

    def test_gravitational_acceleration(self):
        self.assertWithinError(9.7984, self.earth.gravitational_acceleration(6378.1e3))

    def test_surface_gravity(self):
        self.assertWithinError(9.7984, self.earth.surface_gravity())

    def test_equitorial_velocity(self):
        self.assertWithinError(465.0984, self.earth.equitorial_velocity())

    def test_escape_velocity(self):
        self.assertWithinError(11179.908, self.earth.escape_velocity())


import kerbaldynpy.planetoid

class TestPlanetoidLibrary(testhelper.KerbalDynTestCase):

    def test_kerbin_name(self):
        self.assertEqual('Kerbin', kerbaldynpy.planetoid.KERBIN.name)

    def test_kerbin_gravitational_parameter(self):
        self.assertWithinError(3531600000000.0, kerbaldynpy.planetoid.KERBIN.gravitational_parameter)

    def test_kerbin_radius(self):
        self.assertWithinError(600000.0, kerbaldynpy.planetoid.KERBIN.radius)

    def test_kerbin_radius(self):
        self.assertWithinError(21600.0, kerbaldynpy.planetoid.KERBIN.rotational_period)
