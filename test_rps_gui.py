import unittest
from rps_gui import *

class MyTestCase(unittest.TestCase):
    def test_score_keeper(self):
        self.assertEqual(score_keeper(1, 1), 2)
        self.assertRaises(ValueError, score_keeper, -1, -1)

if __name__ == '__main__':
    unittest.main()
