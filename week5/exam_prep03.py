# Constructor
def tree(label, branches=[]):
    for branch in branches:
        assert is_tree(branch)
    return [label] + list(branches)


# Selectors
def label(tree):
    return tree[0]


def branches(tree):
    return tree[1:]


def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True


# For convenience
def is_leaf(tree):
    return not branches(tree)


# fall 2015,midterm 2,#3a
def complete(t, d, k):
    """Return whether t is d-k-complete.
    A tree is d-k-complete if every node at a depth less than d has exactly
    k branches and every node at depth d is a leaf.
    >>> complete(tree(1),0,5)
    True
    >>> u=tree(1,[tree(1),tree(1),tree(1)])
    >>> complete(tree(1,[u,u,u]),2,3)
    True
    >>> complete(u,1,3)
    True
    >>> complete(tree(1,[u,u]),2,3)
    False
    """
    if not branches(t):  # is_leaf(t)
        return d == 0
    bs = [complete(branch, d - 1, k) for branch in branches(t)]
    return len(branches(t)) == k and all(bs)


# Spring 2018,Exam-Prep 03,#1
x, y, z = 1, 2, 3
y = [x, [y, [z, []]]]
x = [y[1][0], y, [y[1][1][1]]]
z = len([])


class Tree:
    def __init__(self, root, branches=[]):
        self.root = root
        for branch in branches:
            assert isinstance(branch, Tree)
            self.branches = list(branch)
    
    def is_leaf(self):
        return not self.branches


class Tree(object):
    def __init__(self, entry, left=None, right=None):
        self.entry = entry
        self.left = left
        self.right = right


# Spring 2015,Midterm 2,#3c
def closest(t):
    """ Return the smallest difference between an entry and the sum of the
    entries of its branches .
    >>> t = Tree (8 , [ Tree (4) , Tree (3)])
    >>> closest (t) # |8 - (4 + 3)| = 1
    1
    >>> closest ( Tree (5 , [t])) # Same minimum as t
    1
    >>> closest ( Tree (10 , [ Tree (2) , t])) # |10 - (2 + 8)| = 0
    0
    >>> closest ( Tree (3)) # |3 - 0| = 3
    3
    >>> closest ( Tree (8 , [ Tree (3 , [ Tree (1 , [ Tree (5)])])])) # |3 - 1| = 2
    2
    >>> sum ([])
    0
    """
    diff = abs(t.entry - sum([b.entry for b in t.branches]))
    return min([diff], [closest(b) for b in t.branches])


# Custom Question

def is_path(t, path):
    """Return whether a given path exists in a tree, beginning at the root.
    >>> t = tree(1, [tree(2, [tree(4), tree(5)]), tree(3, [tree(6), tree(7)])])
    >>> is_path(t, [1, 2])
    True
    >>> is_path(t, [1, 2, 4])
    True
    >>> is_path(t, [2, 4])
    False
    """
    if label(t) != path[0]:
        return False
    if not branches(t):
        return True
    return any([is_path(b, path[1:]) for b in branches(t)])

#Spring 2015,Midterm 2,#4b
def scramble(egg):
    return [egg,over(egg)]

def over(easy):
    easy[1]=[[easy],2]
    return list(easy[1])

egg = scramble([12,24])
