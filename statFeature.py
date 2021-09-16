import unittest


def stat(string):
    list_of_word = sorted(list(set(string)))
    result = []
    for a in list_of_word:
        result.append('The occurrence of "{:s}" is {:d}'
                      .format(a, string.count(a)))

    return result


class TestStat(unittest.TestCase):

    def test_stat(self):
        s = 'abbccc'
        self.assertEqual(stat(s), ['The occurrence of "a" is 1',
                                   'The occurrence of "b" is 2',
                                   'The occurrence of "c" is 3'])


if __name__ == '__main__':
    unittest.main()

