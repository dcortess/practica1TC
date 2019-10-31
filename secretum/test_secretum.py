import unittest
import secretum as s

class MyTestCase(unittest.TestCase):

    def test_1(self):
        n = 123
        k = 3
        p = str(n) * k
        assert s.decrypt(p) == 9

    def test_2(self):
        n = 148
        k = 3
        p = str(n) * k
        assert s.decrypt(p) == 3

    def test_3(self):
        n = 593
        k = 10
        p = str(n) * k
        assert s.decrypt(p) == 8

    def test4(self):
        n = 98963
        k = 100
        p = str(n) * k
        assert s.decrypt(p) == 8

    def test_5(self):
        n = 4757362
        k = 10000
        p = str(n) * k
        assert s.decrypt(p) == 7


if __name__ == '__main__':
    unittest.main()
