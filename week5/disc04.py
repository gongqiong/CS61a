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


# 2.1Write a function that returns the largest number in a tree
def tree_max(t):
    """Return the maximum label in a tree.
    >>> t = tree(4, [tree(2, [tree(1)]), tree(10)])
    >>> tree_max(t)
    10
    """
    return max([label(t)] + [tree_max(branch) for branch in branches(t)])


# 2.2
def height(t):
    """Return the height of a tree.
    >>> t = tree(3, [tree(5, [tree(1)]), tree(2)])
    >>> height(t)
    2
    """
    if is_leaf(t):
        return 0
    return 1 + max([height(branch) for branch in branches(t)])


# 2.3
def square_tree(t):
    """Return a tree with the square of every element in t"""
    return tree(label(t) ** 2, [square_tree(branch) for branch in branches(t)])


# 2.4
def find_path(tree, x):
    """
    >>> t = tree(2, [tree(7, [tree(3), tree(6, [tree(5), tree(11)])] ), tree(15)])
    >>> find_path(t, 5)
    [2, 7, 6, 5]
    >>> find_path(t, 10) # returns None
    """
    if x == label(tree):
        return [x]
    for branch in branches(tree):
        path = find_path(branch, x)
        if path:
            return [label(tree)] + path


# 2.5
def prune(t, k):
    """
    >>> t = tree(2, [tree(7, [tree(3), tree(6, [tree(5), tree(11)])] ), tree(15)])
    >>> prune(t,2)
    [2, [7, [3], [6]], [15]]
    """
    if k == 0:
        return tree(label(t), [])
    else:
        return tree(label(t), [prune(branch, k - 1) for branch in branches(t)])


# 2.6
def hailstone_tree(n, h):
    """Generates a tree of hailstone numbers that will
    reach N, with height H.
    >>> hailstone_tree(1, 0)
    [1]
    >>> hailstone_tree(1, 4)
    [1, [2, [4, [8, [16]]]]]
    >>> hailstone_tree(8, 3)
    [8, [16, [32, [64]], [5, [10]]]]
    """
    if h == 0:
        return [n]
    else:
        if (n - 1) % 3 == 0 and n - 1 != 0 and n-1!=3:
            return tree(n, [hailstone_tree(2 * n, h - 1), hailstone_tree(int((n - 1) / 3), h - 1)])
        else:
            return tree(n, [hailstone_tree(2 * n, h - 1)])
