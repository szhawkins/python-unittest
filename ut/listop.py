#!/usr/bin/python3

class C(object):
    """A simple class"""

    def __init__(self, c):
        self.c = c

    def disp(self):
        print ("length: ", len(self.c))
        print ("data: ", self.c)

    def sum(self):
        return sum(self.c)

    def len (self):
        return len(self.c)

    def sort (self):
        self.c.sort()
        return (self.c)

    def append (self, moreItems):
        self.c.extend(moreItems)

