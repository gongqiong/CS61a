def total(s0, s1):
	print(s0 + s1)
	return echo


def echo(s0, s1):
	print(s0, s1)
	return total

say = echo

say = say(2,0)
say = say(2,3)