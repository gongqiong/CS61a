###### OOP ######


class Foo():
    x = 'bam'
    
    def __init__(self, x):
        self.x = x
    
    def baz(self):
        return self.x


class Bar(Foo):
    x = 'boom'
    
    def __init__(self, x):
        Foo.__init__(self, 'er' + x)
    
    def baz(self):
        return Bar.x + Foo.baz(self)


class Student:
    def __init__(self, subjects):
        self.current_units = 16
        self.subjects_to_take = subjects
        self.subjects_learned = {}
        self.partner = None
    
    def learn(self, subject, units):
        print('I just learned about ' + subject)
        self.subjects_learned[subject] = units
        self.current_units -= units
    
    def make_friends(self):
        if len(self.subjects_to_take) > 3:
            print('Whoa! I need more help!')
            self.partner = Student(self.subjects_to_take[1:])
        else:
            print("I'm on my own now!")
            self.partner = None
    
    def take_course(self):
        course = self.subjects_to_take.pop()
        self.learn(course, 4)
        if self.partner:
            print('I need to switch this up!?')
            self.partner = self.partner.partner
        if not self.partner:
            print('I have failed to make a friend :(')


######Nonlocal######
# 2.3
def make_max_finder():
    """
    >>> m = make_max_finder()
    >>> m([5, 6, 7])
    7
    >>> m([1, 2, 3])
    7
    >>> m([9])
    9
    >>> m2 = make_max_finder()
    >>> m2([1])
    1
    """
    max_value = 0
    
    def f(list):
        nonlocal max_value
        max_value = max(max_value, max(list))
        return max_value
    
    return f


######Object Oriented Trees######
# 3.1
def filter_tree(t, fn):
    """
    >>> t = Tree(1, [Tree(2), Tree(3, [Tree(4)]), Tree(6, [Tree(7)])])
    >>> filter_tree(t, lambda x: x % 2 != 0)
    >>> t
    Tree(1, [Tree(3)])
    >>> t2 = Tree(2, [Tree(3), Tree(4), Tree(5)])
    >>> filter_tree(t2, lambda x: x != 2)
    >>> t2
    Tree(2)
    """
    if not fn(t.label):
        t.branches = []
    else:
        for b in t.branches[:]:  # 无[:]情况：因为列表变化，0位元素被删，接下来仍从1位（原2位）开始
            if not fn(b.label):
                t.branches.remove(b)
            else:
                filter_tree(b, fn)


# 3.2
def nth_level_tree_map(fn, tree, n):
    """Mutates a tree by mapping a function all the elements of a tree.
    >>> tree = Tree(1, [Tree(7, [Tree(3), Tree(4), Tree(5)]), Tree(2, [Tree(6), Tree(4)])])
    >>> nth_level_tree_map(lambda x: x + 1, tree, 2)
    >>> tree
    Tree(2, [Tree(7, [Tree(4), Tree(5), Tree(6)]), Tree(2, [Tree(7), Tree(5)])])
    """
    
    def helper(tree, level):
        if level % n == 0:
            tree.label = fn(tree.label)
        for b in tree.branches:
            helper(b, level + 1)
        return helper
    
    helper(tree, 0)


######Linked Lists######
# 4.3
def has_cycle(link):
    """
    >>> s = Link(1, Link(2, Link(3)))
    >>> s.rest.rest.rest = s
    >>> has_cycle(s)
    True
    """
    # iteratively with two pointers
    # linkfirst =link
    # linksecond = link.rest
    # while linkfirst.rest and linksecond.rest and linksecond.rest.rest:
    #     if linkfirst is linksecond:
    #         return True
    #     linkfirst = link.rest
    #     linksecond = linksecond.rest.rest
    # return False
    # keeping track of Link objects we’ve seen already
    seen =[]
    while link.rest:
        if link in seen:
            return True
        seen.append(link)
        link = link.rest
    return False

#4.4
def seq_in_link(link, sub_link):
    """
    >>> lnk1 = Link(1, Link(2, Link(3, Link(4))))
    >>> lnk2 = Link(1, Link(3))
    >>> lnk3 = Link(4, Link(3, Link(2, Link(1))))
    >>> seq_in_link(lnk1, lnk2)
    True
    >>> seq_in_link(lnk1, lnk3)
    False
    """
    if link == Link.empty:
        return False
    if sub_link == Link.empty:
        return True
    if sub_link.first == link.first:
        return seq_in_link(link.rest, sub_link.rest)
    else:
        return seq_in_link(link.rest,sub_link)
    


# Tree class
class Tree:
    """
    >>> t = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
    >>> t.label
    3
    >>> t.branches[0].label
    2
    >>> t.branches[1].is_leaf()
    True
    """
    
    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = list(branches)
    
    def is_leaf(self):
        return not self.branches
    
    def map(self, fn):
        """
        Apply a function `fn` to each node in the tree and mutate the tree.

        >>> t1 = Tree(1)
        >>> t1.map(lambda x: x + 2)
        >>> t1.map(lambda x : x * 4)
        >>> t1.label
        12
        >>> t2 = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
        >>> t2.map(lambda x: x * x)
        >>> t2
        Tree(9, [Tree(4, [Tree(25)]), Tree(16)])
        """
        self.label = fn(self.label)
        for b in self.branches:
            b.map(fn)
    
    def __contains__(self, e):
        """
        Determine whether an element exists in the tree.

        >>> t1 = Tree(1)
        >>> 1 in t1
        True
        >>> 8 in t1
        False
        >>> t2 = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
        >>> 6 in t2
        False
        >>> 5 in t2
        True
        """
        if self.label == e:
            return True
        for b in self.branches:
            if e in b:
                return True
        return False
    
    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(self.label, branch_str)
    
    def __str__(self):
        def print_tree(t, indent=0):
            tree_str = '  ' * indent + str(t.label) + "\n"
            for b in t.branches:
                tree_str += print_tree(b, indent + 1)
            return tree_str
        
        return print_tree(self).rstrip()


# Link class
class Link:
    """A linked list with a first element and the rest."""
    empty = ()
    
    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest
    
    def __getitem__(self, i):
        if i == 0:
            return self.first
        else:
            return self.rest[i - 1]
    
    def __len__(self):
        return 1 + len(self.rest)
