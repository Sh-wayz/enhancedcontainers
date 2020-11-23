import unittest
import enhancedcontainers as ec


class QueueTest(unittest.TestCase):

    def setUp(self):
        self.queue = ec.Queue()
        pass

    def test_everything_that_requires_a_single_queue_bc_unittest_sucks(self):
        self.assertTrue(self.queue.is_empty())
        # enqueue testing
        # self.assertEqual(self.queue.enqueue('test1'), 'test1')
        # self.assertEqual(self.queue.enqueue('test2'), 'test2')
        # self.assertEqual(self.queue.enqueue('test3'), 'test3')
        self.queue.enqueue('test1')
        self.queue.enqueue('test2')
        self.queue.enqueue('test3')
        # should be 'test1'vvv
        self.assertEqual(self.queue.peek(), self.queue.dequeue())
        self.assertEqual(self.queue.size(), 2)
        self.assertFalse(self.queue.is_empty())


if __name__ == '__main__':
    unittest.main()
