import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        print("aaa")
        self.assertEqual(True, True)

    def test_something1(self):
        print("bbb")
        self.assertEqual(True, True)

if __name__ == '__main__':
    unittest.main()
