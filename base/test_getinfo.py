import unittest
class TestGetinfo(unittest.TestCase):
    def test_01(self):
        self.assertEqual("12","1")

    def test_02(self):
        a="11"
        b="22"
        self.assertEqual(a,b)


if __name__ == '__main__':
    unittest.main()