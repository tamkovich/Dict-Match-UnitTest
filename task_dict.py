class CheckDicts:

    def __init__(self, initial_dict: dict):
        """Initialize <class '__main__.CheckDicts'> object with dict"""
        self.initial_dict = initial_dict

    def diff_between_dicts(self, new_dict: dict) -> dict:
        """
        Find the difference between initial dict and received (the new one)
        :param new_dict: <dict> Just the new dict
        :return: <dict> Dict which contains only unequal values
        """
        return self.__recursion_checker(self.initial_dict, new_dict)

    #
    # End Public Methods
    #

    def __recursion_checker(self, initial, new):
        """

        :param initial:
            If dict <dict> then try to find deeper difference
            else return as value from the `new`
        :param new: Compare value with `initial`
        :return: unequal values from the `new`
        """
        res = {}
        if type(initial) is not dict or type(new) is not dict:
            return new

        # check every similar keys
        for key in set(initial.keys()) & set(new.keys()):
            if initial[key] != new[key]:
                res[key] = self.__recursion_checker(initial[key], new[key])

        # check every different keys
        for key in set(initial.keys()) ^ set(new.keys()):
            if initial.get(key) != new.get(key):
                res[key] = self.__recursion_checker(initial.get(key), new.get(key))
        return res
