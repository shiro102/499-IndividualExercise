import unittest


def search(string, key):
    return string.count(key)


class TestSearchMethod(unittest.TestCase):

    def test_search(self):
        s = "abbccc"
        self.assertEqual(search(s, 'b'), 2)


if __name__ == '__main__':
    unittest.main()
