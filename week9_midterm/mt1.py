#3 Zip it
def make_zipper(f1, f2, sequence):
    """ Return a function of f1 and f2 composed based on sequence.
    >>> def increment(x):
            return x + 1
    >>> def square(x):
            return x * x
    >>> do_nothing = make_zipper(increment, square, 0)
    >>> do_nothing(2) # Don't call either f1 or f2, just return your input untouched
    2
    >>> incincsq = make_zipper(increment, square, 112)
    >>> incincsq(2) # increment(increment(square(2))), so 2 → 4 → 5 → 6
    6
    >>> sqincsqinc = make_zipper(increment, square, 2121)
    >>> sqincsqinc(2) # square(increment(square(increment(2)))), so 2 → 3 → 9 → 10 → 100 100
    """
    