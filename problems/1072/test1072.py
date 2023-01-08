import p1072
import unittest


class Test1072(unittest.TestCase):
    def test_1(self):
        self.assertEqual(p1072.solve(10, 8), 1)

    def test_2(self):
        self.assertEqual(p1072.solve(100, 80), 6)

    def test_3(self):
        self.assertEqual(p1072.solve(47, 47), -1)

    def test_4(self):
        self.assertEqual(p1072.solve(99000, 0), 1000)

    def test_5(self):
        self.assertEqual(p1072.solve(1000000000, 470000000), 19230770)

    def test_6(self):
        self.assertEqual(p1072.solve(1000000000, 999999999), -1)

    def test_7(self):
        self.assertEqual(p1072.solve(100, 99), -1)

    def test_8(self):
        self.assertEqual(p1072.solve(100, 98), 100)

    def test_9(self):
        self.assertEqual(p1072.solve(100, 97), 50)


if __name__ == "__main__":
    unittest.main()
