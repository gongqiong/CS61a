"""Lab 1: Expressions and Control Structures"""


# Coding Practice

def repeated(f, n, x):
	"""Returns the result of composing f n times on x.

	>>> def square(x):
	...     return x * x
	...
	>>> repeated(square, 2, 3)  # square(square(3)), or 3 ** 4
	81
	>>> repeated(square, 1, 4)  # square(4)
	16
	>>> repeated(square, 6, 2)  # big number
	18446744073709551616
	>>> def opposite(b):
	...     return not b
	...
	>>> repeated(opposite, 4, True)
	True
	>>> repeated(opposite, 5, True)
	False
	>>> repeated(opposite, 631, 1)
	False
	>>> repeated(opposite, 3, 0)
	True
	"""
	"*** YOUR CODE HERE ***"
	while n > 0:
		x = f(x)
		n -= 1
	return x


def square(x):
	return x * x


print(repeated(square, 2, 3))


def sum_digits(n):
	"""Sum all the digits of n.

	>>> sum_digits(10) # 1 + 0 = 1
	1
	>>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
	12
	>>> sum_digits(1234567890)
	45
	"""
	"*** YOUR CODE HERE ***"
	nstr = str(n)
	nlen = len(nstr)
	sum_of_digits = 0
	for i in range(nlen):
		sum_of_digits += int(nstr[i])
	return sum_of_digits


def double_eights(n):
	"""Return true if n has two eights in a row.
	>>> double_eights(8)
	False
	>>> double_eights(88)
	True
	>>> double_eights(2882)
	True
	>>> double_eights(880088)
	True
	>>> double_eights(12345)
	False
	>>> double_eights(80808080)
	False
	"""
	"*** YOUR CODE HERE ***"
	nstr = str(n)
	nlen = len(nstr)
	for i in range(nlen-1):
		if nstr[i]+nstr[i+1] == '88':
			return True
	return False

print(not 0 and 12 or 0)