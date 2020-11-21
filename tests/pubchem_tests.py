import unittest
from test import Test

class PubchemTests(Test):
    def test_find_compound_cid(self):
        print("Test compound cid")

    def test_compound_information_cid(self):
        print("Test compound information cid")

    def test_compound_information(self):
        print("Test compound information")

    def run_all(self):
        self.test_find_compound_cid()
        self.test_compound_information_cid()
        self.test_compound_information()
