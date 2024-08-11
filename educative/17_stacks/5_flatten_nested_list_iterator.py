class NestedIntegers:
    # Constructor initializes a single integer if a value has been passed
    # else it initializes an empty list
    def __init__(self, integer=None):
        if integer:
            self.integer = integer
        else:
            self.n_list = []
            self.integer = 0

    # If this NestedIntegers holds a single integer rather
    # than a nested list, returns TRUE, else, returns FALSE
    def is_integer(self):
        if self.integer:
            return True
        return False

    # Returns the single integer, if this NestedIntegers holds a single integer
    # Returns null if this NestedIntegers holds a nested list
    def get_integer(self):
        return self.integer

    #  Sets this NestedIntegers to hold a single integer.
    def set_integer(self, value):
        self.n_list = None
        self.integer = value

    # Sets this NestedIntegers to hold a nested list and adds a nested
    # integer to it.
    def add(self, ni):
        if self.integer:
            self.n_list = []
            self.n_list.append(NestedIntegers(self.integer))
            self.integer = None
        self.n_list.append(ni)

    # Returns the nested list, if this NestedIntegers holds a nested list
    # Returns null if this NestedIntegers holds a single integer
    def get_list(self):
        return self.n_list


class NestedIterator:
    # Initializes the NestedIterator with nested_list
    def __init__(self, nested_list):
        # Write your code here
        pass

    # checks if there are still some integers in nested_list
    def has_next(self):
        # Write your code here
        pass

    # returns the next element from nested_list
    def next(self):
        # Write your code here
        pass


# ------ Please don't change the following function ----------
# flatten_list function is used for testing porpuses.
# Your code will be tested using this function
def flatten_list(nested_iterator_object):
    result = []
    while nested_iterator_object.has_next():
        result.append(nested_iterator_object.next())
    return result