#!/usr/bin/python3

import unittest

from src.cf2 import *

# ===[ Simple MetaModel used by tests ]===
TOP = MetaTreeFixedDict("top", "i am top")
BAR = MetaTreeScalar("bar", "i am bar", int, parent=TOP)
BAZ = MetaTreeFixedDict("baz", "i am baz", parent=TOP)
MetaTreeScalar("name", "person's name", str, parent=BAZ)
MetaTreeScalar("age", "person's age", int, parent=BAZ)
TEAMS = MetaTreeFixedDict("teams", "sports teams", parent=TOP)
MetaTreeScalar("soccer", "soccer", str, parent=TEAMS)
MetaTreeScalar("nfl", "american football", str, parent=TEAMS)
TEST_METAMODEL = MetaModel(TOP)

# ===[ Tests ]===
class TestTypeCheck(unittest.TestCase):
    def test_good_case(self):
        good_data = {
                        "bar": 5,
                        "baz": {
                            "name": "john",
                            "age": 37,
                        },
                        "teams" : {
                            "soccer": "man utd",
                            "nfl": "tigers",
                        }
                    }
        errlist = TEST_METAMODEL.TypeCheck(good_data)
        self.assertEqual(errlist, [], "detected error in good case")

    def test_bad_case(self):
        bad_data = {
                        "bar" : False,
                        "baz" : {
                            "age" : "100",
                            "hobby" : [ "fishing" , "eating" ]
                        },
                        "teams": 619,
                        "etc" : {
                            "phone" : 123456709,
                        }
                    }
        errlist = TEST_METAMODEL.TypeCheck(bad_data)
        self.assertNotEqual(len(errlist), 0)

# ===[ Boilerplate ]===
if __name__ == '__main__':
    unittest.main()
