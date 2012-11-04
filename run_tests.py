import unittest


loader = unittest.TestLoader()

suite = unittest.TestSuite()

import test.planetoid_test
suite.addTests(loader.loadTestsFromModule(test.planetoid_test))

runner = unittest.TextTestRunner(verbosity=1)
result = runner.run(suite)
