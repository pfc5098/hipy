import unittest
import module 

class TestModule(unittest.TestCase):

    def test_foo(self):
        self.assertEqual(module.foo('hi'), 'hi')

if __name__ == '__main__':
    unittest.main()
