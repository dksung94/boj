import p1039
import unittest


class Test1072(unittest.TestCase):
    def test_1(self):
        self.assertEqual(p1039.solve(16375, 1), 76315)

    def test_2(self):
        self.assertEqual(p1039.solve(132, 3), 312)

    def test_3(self):
        self.assertEqual(p1039.solve(932133, 9), 933321)


if __name__ == "__main__":
    unittest.main()
