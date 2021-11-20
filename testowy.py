import unittest


class MyTestCase(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        print("class")
        cls.aa = 4

    def setUp(self):
        print(self.aa)
        print("setUp")

    def test_something(self):
        print("aaa")
        print(self.aa)
        self.assertEqual(True, True)

    def test_something1(self):
        print("bbb")
        self.assertEqual(True, True)

    def tearDown(self):
        print("Tear")

if __name__ == '__main__':
    unittest.main()
