import unittest
import math

class KerbalDynTestCase(unittest.TestCase):

    def assertWithinError(self, expected, actual, error=1e-6, delta=1e-9):
        if abs(expected) <= delta:
            return self.assertAlmostEqual(expected, actual, delta=delta)
        else:
            err = (actual - expected) / expected
            #return self.assertTrue(math.fabs(err) <= error)
            if math.fabs(err) <= error:
                pass
            else:
                raise AssertionError, "Expected " + str(actual) + " to be within an error pf " + str(error) + " of " + str(expected)
