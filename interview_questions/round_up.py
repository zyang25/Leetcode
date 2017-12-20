import unittest

# input (20, 3) -> 7 (6.66)


def divide_number(x, y):

    pass


def round_up(x):
    '''
    No % allow
    '''
    base_x = floor(x)
    diff = abs(y - base_x)
    if diff > 0.5:
        return base_x + 1
    else:
        return base_x

class TestDivideNumber(unittest.TestCase):
    """docstring for TestRoundUp"""
    def test_round_up(self):
        self.assertEqual(round_up(3.2), 1)


if __name__ == 'main':
    unittest.main()
