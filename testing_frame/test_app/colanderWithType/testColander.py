from django.test.simple import DjangoTestSuiteRunner
from django.test.utils import setup_test_environment
from django.utils import unittest
import schema 
import os
import json

class ConditionManagerTests(unittest.TestCase):
    def testSocialHistrory(self):
        schema.testColanderSchema()
        schema.testUpdateColanderSchema()
        print 'here'
        
if __name__ == "__main__":
    setup_test_environment()
    suite = unittest.TestLoader().loadTestsFromTestCase(
        ConditionManagerTests)
    runner = DjangoTestSuiteRunner(verbosity=2)
    runner.setup_databases()
    runner.run_suite(suite)
