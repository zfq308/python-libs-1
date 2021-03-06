# file:    funchelp.py
# author:  Colin Woodbury
# contact: colingw AT gmail
# about:   A library for helping with functional programming in python.

class take():
    '''Yields 'num' elements from a given iterator.'''
    def __init__(self, num, itera):
        self.num = num
        self.itera = itera

    def __iter__(self):
        gen = iter(self.itera)  # Activate the iterator.
        for x in range(self.num):
            yield next(gen)

def head(itera):
    '''Returns the first item generated by an iterator.'''
    gen = iter(itera)
    return next(gen)

def last(itera):
    '''Returns the last item generated by an iterator.'''
    curr = None
    for item in itera:
        curr = item
    return curr
        
