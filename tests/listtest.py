import unittest
import enhancedcontainers as ec


class ListTest(unittest.TestCase):

    def setUp(self):
        self.elist = ec.EnhancedList(['test', 'test', 'test2', 'test3'])
        pass

    def test_indices(self):
        self.assertEqual(self.elist.indices('test'), [0, 1])
        self.assertNotEqual(self.elist.indices('test2'),
                            self.elist.indices('test'))

    def test_deep_copy(self):
        elist2 = self.elist.copy()
        elist2[0] = "test4"
        self.assertNotEqual(elist2[0], self.elist[0])

        def test_append(self):
            self.assertEqual(self.elist.append('test5'), 'test5'
                             def test_deep_copy(self):
                             edict2=self.edict.copy()
                             edict2.test="should not happen"
                             self.assertNotEqual(edict2.test, self.edict.test)
