def is_prime(n):
    '''
    :param n:7
    :return: True
    :param n:10
    :return: False
    :param n:1
    :return: False
    '''
    def prime_helper(i):
        if n==i:
            return True
        elif n%i==0:
            return False
        else:
            return prime_helper(i+1)
    return prime_helper(2)

#takes in a one-argument function f and an integer x.
#It should return another function which takes in one argument, another integer.
#This function returns the result of applying f to x this number of times.
def make_func_repeater(f, x):
    """
    >>> incr_1 = make_func_repeater(lambda x: x + 1, 1)
    >>> incr_1(2) #same as f(f(x))
    3
    >>> incr_1(5)
    6
    """
    def repeat(n):
        if n==1:
            return f(x)
        else:
            return f(repeat(n-1))
    return repeat

def count_stair_ways(n):
    '''
    
    '''
    if n ==1:
        return 1
    elif n==2:
        return 2
    else:
        return count_stair_ways(n-1)+count_stair_ways(n-2)

def count_k(n, k):
    """
>>> count_k(3, 3) # 3, 2 + 1, 1 + 2, 1 + 1 + 1
4
>>> count_k(4, 4)
8
>>> count_k(10, 3)
274
>>> count_k(300, 1) # Only one step at a time
1
"""
    if n==1:
        return 1
    elif n<0:
        return 0
    else:
        total =0
        i=1
        while i<=k:
            total+=count_k(n-i,k)
            i+=1
        return total

#杨辉三角
def pascal(row, column):
    if row==0 and column==0:
        return 1
    elif column>row or column<0:
        return 0
    else:
        return pascal(row-1,column)+pascal(row-1,column-1)
