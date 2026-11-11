'''
This file implements several different ways of generating the Fibonacci sequence.
'''


def fib(n):
    '''
    Returns the nth Fibonacci number, with fib(0)=0, fib(1)=1, fib(2)=1, ...
    '''
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


def fibs(n):
    '''
    Returns a list of the first n Fibonacci numbers starting from 0: [0, 1, 1, 2, ...].
    '''
    result = []
    a, b = 0, 1
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result


class FibIter:
    '''
    Iterator yielding the Fibonacci sequence starting from 1, 1, 2, 3, 5, ...
    FibIter(n) yields exactly n values; FibIter(None) is infinite.
    '''

    def __init__(self, n):
        self.n = n
        self.i = 0
        self.a = 1
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.n is not None and self.i >= self.n:
            raise StopIteration
        value = self.a
        self.a, self.b = self.b, self.a + self.b
        self.i += 1
        return value


class Fib:
    '''
    Iterable representing the Fibonacci sequence starting from 1, 1, 2, 3, ...
    Fib(n) yields n values, Fib() yields infinitely.
    '''

    def __init__(self, n=None):
        self.n = n

    def __iter__(self):
        a, b = 0, 1
        if self.n is None:
            while True:
                yield a
                a, b = b, a + b
        else:
            for _ in range(self.n):
                yield a
                a, b = b, a + b

    def __repr__(self):
        if self.n is None:
            return 'Fib()'
        return 'Fib(' + str(self.n) + ')'

    def __str__(self):
        return repr(self)


def fib_yield(n=None):
    '''
    Generator function for the Fibonacci sequence starting from 1, 1, 2, ...
    '''
    a, b = 0, 1
    if n is None:
        while True:
            yield a
            a, b = b, a + b
    else:
        for _ in range(n):
            yield a
            a, b = b, a + b
