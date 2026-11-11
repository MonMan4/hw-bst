'''
Reimplementation of Python's builtin range function as a generator.
'''


def range(*args):
    '''
    Supports range(stop), range(start, stop), range(start, stop, step).
    '''
    if len(args) == 1:
        start, stop, step = 0, args[0], 1
    elif len(args) == 2:
        start, stop, step = args[0], args[1], 1
    elif len(args) == 3:
        start, stop, step = args[0], args[1], args[2]
    else:
        raise TypeError('range expected at most 3 arguments')

    if step == 0:
        raise ValueError('range() arg 3 must not be zero')

    if step > 0:
        current = start
        while current < stop:
            yield current
            current += step
    else:
        current = start
        while current > stop:
            yield current
            current += step
