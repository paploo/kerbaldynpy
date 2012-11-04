import unittest
import importlib

test_modules = [
    'test.planetoid_test'
]

loader = unittest.TestLoader()
suite = unittest.TestSuite()

for test_module in test_modules:
    mod = importlib.import_module(test_module)
    suite.addTests(loader.loadTestsFromModule(mod))

runner = unittest.TextTestRunner(verbosity=1)
result = runner.run(suite)
