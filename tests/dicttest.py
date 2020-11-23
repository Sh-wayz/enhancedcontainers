import unittest
import enhancedcontainers as ec


class DictTest(unittest.TestCase):

    def setUp(self):
        self.edict = ec.EnhancedDict({"test": "test"})
        pass

    def test_dot_access(self):
        self.assertIsNotNone(self.edict.test)
        self.assertEqual(self.edict.test, "test")

    def test_deep_copy(self):
        edict2 = self.edict.copy()
        edict2.test = "should not happen"
        self.assertNotEqual(edict2.test, self.edict.test)


if __name__ == '__main__':
    unittest.main()
