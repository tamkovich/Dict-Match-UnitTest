# Разрешенные встроенные библиотеки в python
import copy
import unittest

# Внутренние модули
import task_dict


class TestDict(unittest.TestCase):

    def test_find_difference_blank_dict(self):
        data = {}
        checker = task_dict.CheckDicts(data)
        data = copy.deepcopy(data)
        data['x'] = 'y'
        self.assertEqual(
            checker.diff_between_dicts(copy.deepcopy(data)),
            {'x': 'y'}
        )

    def test_find_difference_any_keys(self):
        data = {'a': 2}
        checker = task_dict.CheckDicts(data)
        data = copy.deepcopy(data)
        data['x'] = 'y'
        data['b'] = 1
        self.assertEqual(
            checker.diff_between_dicts(copy.deepcopy(data)),
            {'x': 'y', 'b': 1}
        )

    def test_find_difference_no_changes(self):
        data = {'a': 5}
        checker = task_dict.CheckDicts(data)
        self.assertEqual(
            checker.diff_between_dicts(copy.deepcopy(data)),
            {}
        )

    def test_find_difference_multiple_types(self):
        data = {
            'a': 5,
            'b': ['a', 'b', 'c']
        }
        checker = task_dict.CheckDicts(data)
        data = copy.deepcopy(data)
        data['b'].append(80.08)
        self.assertEqual(
            checker.diff_between_dicts(data),
            {'b': ['a', 'b', 'c', 80.08]}
        )

    def test_find_difference_any_level(self):
        data = {
            'a': {
                'a1': 1,
                'a2': 2,
            },
            'b': {
                'b1': {
                    'b11': 1,
                    'b12': 2,
                },
            }
        }
        checker = task_dict.CheckDicts(data)
        data = copy.deepcopy(data)
        data['a']['a1'] = 3
        data['b']['b1']['b11'] = 5
        self.assertEqual(
            checker.diff_between_dicts(data),
            {'a': {'a1': 3}, 'b': {'b1': {'b11': 5}}}
        )


if __name__ == '__main__':
    unittest.main()
