import unittest
from SimpleClass import simpleClass

class TestSimpleClass(unittest.TestCase):
    def test_myFunc_1(self):
        sc1 = simpleClass()
        ans = sc1.myFunc_1("Hello","World")
        self.assertEqual(ans,"Hello World")
    def test_myFunc_1_2(self):
        sc1 = simpleClass()
        ans = sc1.myFunc_1("Good","Bye")
        self.assertEqual(ans,"Good Bye")
    def test_myFunc_1_3(self):
        sc1 = simpleClass()
        ans = sc1.myFunc_1("Good","Bye")
        self.assertNotEqual(ans,"GoodBye")
    def test_myFunc_2_1(self):
        sc1 = simpleClass()
        ans = sc1.myFunc_2("1","2")
        self.assertEqual(ans,3)
    def test_myFunc_2_2(self):
        sc1 = simpleClass()
        ans = sc1.myFunc_2(1,2)
        self.assertEqual(ans,3)
    def test_myFunc_2_3(self):
        sc1 = simpleClass()
        ans = sc1.myFunc_2(1,2)
        self.assertNotEqual(ans,"3")
    def test_myFunc_2_2(self):
        sc1 = simpleClass()
        self.assertRaises(Exception,sc1.myFunc_2,"a",3)

    def test_myFunc_3_1(self):
        sc1 = simpleClass()
        ans = sc1.myFunc_3("2",1,2)
        self.assertEqual(ans,"22")
    def test_myFunc_3_2(self):
        sc1 = simpleClass()
        ans = sc1.myFunc_3("1","1",2)
        self.assertEqual(ans,"12")
    def test_myFunc_3_3(self):
        sc1 = simpleClass()
        self.assertRaises(Exception,sc1.myFunc_3,"a",3,"b")
    

    

unittest.main()