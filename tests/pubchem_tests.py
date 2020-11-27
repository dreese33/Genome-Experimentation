import unittest

# appends global project path to sys path
import sys, os
data_path = os.path.dirname(os.getcwd())
sys.path.insert(1, data_path)

from test import Test
from data import pubchem

class PubchemTests(Test):
    def test_find_compound_cid(self):
        print("Testing compound cid...")
        self.glucose = pubchem.find_compound_cid('glucose')
        assert self.glucose != -1
        print("Glucose cid: " + str(self.glucose))
        bad_compound = pubchem.find_compound_cid('not a real compound')
        assert bad_compound == -1
        print("Bad Compound cid: " + str(bad_compound) + "\n")

    def test_compound_information_cid(self):
        print("Test compound information cid...")
        info = pubchem.compound_information_cid(self.glucose)
        print("Glucose info extracted successfully\n")

    def run_all(self):
        self.test_find_compound_cid()
        self.test_compound_information_cid()

