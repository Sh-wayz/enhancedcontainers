import unittest
import enhancedcontainers as ec


class StackTest(unittest.TestCase):

    def setUp(self):
        self.stack = ec.Stack(3)
        pass

    def test_everything_that_requires_a_single_stack_bc_unittest_sucks(self):
        self.assertEqual(self.stack.push('test1'), 'test1')  # push testing
        self.assertEqual(self.stack.push('test2'), 'test2')
        self.assertNotEqual(self.stack.push('test3'),
                            'This should not happen.')
        self.assertEqual(self.stack.peek(), 'test3')  # peek testing
        self.assertNotEqual(self.stack.peek(), 'test4')
        self.assertEqual(self.stack.pop(), 'test3')  # pop testing
        self.assertTrue(self.stack.__contains__('test2'))  # contains testing

    def test_other_stuff(self):
        self.assertTrue(self.stack.is_empty())
        self.assertFalse(self.stack.is_full())
        self.assertEqual(self.stack.limit, 3)


if __name__ == '__main__':
    unittest.main()
