class Link:
    """A linked list.

    >>> s = Link(1)
    >>> s.first
    1
    >>> s.rest is Link.empty
    True
    >>> s = Link(2, Link(3, Link(4)))
    >>> s.first = 5
    >>> s.rest.first = 6
    >>> s.rest.rest = Link.empty
    >>> s                                    # Displays the contents of repr(s)
    Link(5, Link(6))
    >>> s.rest = Link(7, Link(Link(8, Link(9))))
    >>> s
    Link(5, Link(7, Link(Link(8, Link(9)))))
    >>> print(s)                             # Prints str(s)
    <5 7 <8 9>>
    """
    empty = ()
    
    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest
    
    def __repr__(self):
        if self.rest is not Link.empty:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'
    
    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'


# 1.1
def multiply_lnks(lst_of_lnks):
    """
    >>> a = Link(2, Link(3, Link(5)))
    >>> b = Link(6, Link(4, Link(2)))
    >>> c = Link(4, Link(1, Link(0, Link(2))))
    >>> p = multiply_lnks([a, b, c])
    >>> p.first
    48
    >>> p.rest.first
    12
    >>> p.rest.rest.rest is Link.empty
    True
    """
    # recursive solution:
    first = 1
    for i in range(len(lst_of_lnks)):
        if lst_of_lnks[i] is Link.empty:
            return Link.empty
        else:
            first *= lst_of_lnks[i].first
            lst_of_lnks[i] = lst_of_lnks[i].rest
    link = Link(first, multiply_lnks(lst_of_lnks))
    return link
    # Iterative solution:
    # import operator
    # from functools import reduce
    # def prod(factors):
    #     return reduce(operator.mul, factors, 1)
    #
    # head = Link.empty
    # tail = head
    # while Link.empty not in lst_of_lnks:
    #     all_prod = prod(_.first for _ in lst_of_lnks)
    #     if head is Link.empty:
    #         head = Link(all_prod)
    #         tail = head
    #     else:
    #         tail.rest = Link(all_prod)
    #         tail = tail.rest
    #     lst_of_lnks = [_.rest for _ in lst_of_lnks]
    # return head


# 1.2


def remove_duplicates(lnk):
    """
    >>> lnk = Link(1, Link(1, Link(1, Link(1, Link(5)))))
    >>> remove_duplicates(lnk)
    >>> lnk
    Link(1, Link(5))
    """
    # recursive solution:
    # if lnk is Link.empty or lnk.rest is Link.empty:
    #     return
    # elif lnk.first == lnk.rest.first:
    #     lnk.rest = lnk.rest.rest
    #     remove_duplicates(lnk)
    # else:
    #     remove_duplicates(lnk.rest)
    # !!!!sorted linked list
    # Iterative solution:
    while lnk is not Link.empty and lnk.rest is not Link.empty:
        if lnk.first == lnk.rest.first:
            lnk.rest = lnk.rest.rest
        else:
            lnk = lnk.rest


# 3.1
def even_weighted(lst):
    """
    >>> x = [1, 2, 3, 4, 5, 6]
    >>> even_weighted(x)
    [0, 6, 20]
    """
    return [i * lst[i] for i in range(len(lst)) if i % 2 == 0]


# 3.2
def quicksort_list(lst):
    """
    >>> quicksort_list([3, 1, 4])
    [1, 3, 4]
    """
    if len(lst) == 1:
        return lst
    pivot = lst[0]
    less = [i for i in lst if i < pivot]
    greater = [i for i in lst if i > pivot]
    return quicksort_list(less) + [pivot] + quicksort_list(greater)


# 3.3
def max_product(lst):
    """Return the maximum product that can be formed using lst without using any consecutive numbers
    >>> max_product([10,3,1,9,2]) # 10 * 9
    90
    >>> max_product([5,10,5,10,5]) # 5 * 5 * 5
    125
    >>> max_product([])
    1
    """
    if len(lst)==0:
        return 1
    elif len(lst)==1:
        return lst[0]
    else:
        return max(max_product(lst[1:]),lst[0]*max_product(lst[2:]))


# 3.4
def redundant_map(t, f):
    """
    >>> double = lambda x: x*2
    >>> tree = Tree(1, [Tree(1), Tree(2, [Tree(1, [Tree(1)])])])
    >>> redundant_map(tree, double)
    >>> print_levels(tree)
    [2] # 1 * 2 ˆ (1) ; Apply double one time
    [4, 8] # 1 * 2 ˆ (2), 2 * 2 ˆ (2) ; Apply double two times
    [16] # 1 * 2 ˆ (2 ˆ 2) ; Apply double four times
    [256] # 1 * 2 ˆ (2 ˆ 3) ; Apply double eight times
    """
    t.label = f(t.label)
    new_f = lambda x: f(f(x))
    for branch in t.branches:
        return redundant_map(branch,new_f)