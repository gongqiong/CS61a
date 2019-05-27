def make_skipper(n):
    """
    >>> a = make_skipper(2)
    >>> a(5)
    1
    3
    5
    """
    
    def skip(k):
        for i in range(k):
            if (i + 1) % n != 0:
                print(i + 1)
            i += 1
    
    return skip


def make_alternator(f, g):
    """
    >>> a = make_alternator(lambda x: x * x, lambda x: x + 4)
    >>> a(5)
    1
    6
    9
    8
    25
    >>> b = make_alternator(lambda x: x * 2, lambda x: x + 2)
    >>> b(4)
    2
    4
    6
    6
    """
    
    def inner(x):
        for i in range(x):
            if (i + 1) % 2 == 0:
                print(g(i + 1))
            else:
                print(f(i + 1))
            i += 1
    
    return inner


# print(f(i)) if i % 2 == 1 else print(g(i))
# (i=i+1)

# Recursion
# What are three things you find in every recursive function?
# 1. One or more Base Cases
# 2. Way(s) to make the problem into a smaller problem of the same type (so that it can be solved
# recursively).
# 3. One or more Recursive Cases that solve the smaller problem and then uses the solution the
# smaller problem to solve the original (large) problem

# Python does not care
# about a function’s body
# until it is called
# 这是俳句？？？（音排）

# domain 输入数据类型
# range 输出数据类型

# Fibonacci number
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def cascade2(n):
    """Print a cascade of prefixes of n."""
    print(n)
    if n >= 10:
        cascade2(n // 10)
        print(n)


def mystery(n):
    if n == 0:
        return 0
    else:
        return n + mystery(n - 1)


# 1+2+...+n

# 题目错了！！！
def foo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return foo(n - 2) + foo(n - 1)


# nth fibonacci number

def fooply(n):
    if n < 0:
        return 0
    return foo(n) + fooply(n - 1)


# the sum of first n fibonacci number

def mario_number(level):
    """
    Return the number of ways that Mario can traverse the level,
    where Mario can either hop by one digit or two digits each turn.
    A level is defined as being an integer with digits where a 1 is
    something Mario can step on and 0 is something Mario cannot step
    on.
    >>> mario_number(10101) # Hops each turn: (1, 2, 2)
    1
    >>> mario_number(11101) # Hops each turn: (1, 1, 1, 2), (2, 1, 2)
    2
    >>> mario_number(100101)# No way to traverse through level
    0
    """
    if level == 1:
        return 1
    elif level % 10 == 0:  # 起点终点必须为1
        return 0
    else:
        return mario_number(level // 10) + mario_number(level // 100)


# 正反方向结果一样。 例子给出的路径可能不正确？


from operator import add, mul, pow


def combine(n, f, result):
    """
    Combine the digits in n using f.
    >>> combine (3, mul, 2) # mul (3, 2)
    6
    >>> combine (43, mul, 2) # mul (4, mul (3, 2))
    24
    >>> combine (6502, add, 3) # add (6, add (5, add (0, add (2 , 3)))
    16
    >>> combine (239, pow, 0) # pow (2, pow (3, pow (9, 0)))
    8
    """
    if n == 0:
        return result
    else:
        return combine(n // 10, f, f(n % 10, result))
