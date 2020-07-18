# Implements a 1-D Array Using the ctypes Module
import ctypes

class Array:
    # Creates the Array with the given size of the Array
    def __init__(self, size):
        assert size > 0, 'Array Must be greater than 0'
        self.size = size

        ArrayTypes = ctypes.py_object * size
        self.slots = ArrayTypes()

        self.clear(None)

    # Returns the size of the Array
    def __len__(self):
        return self.size

    # Returns the item in the given index
    def __getitem__(self, index):
        assert index >= 0 and index < len(self.slots), "Index out of range"
        return self.slots[index]

    # Sets a value to the index
    def __setitem__(self, index, value):
        assert index >= 0 and index < len(self.slots), "Index out of range"
        self.slots[index] = value

    # Sets the Value to the Array
    def clear(self, value):
        for i in range(self.size):
            self.slots[i] = value

    # Returns Iteratable list
    def __iter__(self):
        return Arrayiterator(self.slots)



class Arrayiterator:
    idx = 0

    # Creates the iteratable List
    def __init__(self, thelist):
        self.list = thelist
        self.idx = 0

    # Returns Iteratable Array
    def __iter__(self):
        return self.list

    # Returns next occuring Value
    def __next__(self):
        if self.idx  < len(self.list):
           let = self.list[self.idx ]
           self.idx  += 1
           return let
        else:
            raise StopIteration

