# need python 3.9+
from math import gcd, atan, pi, tan
from fractions import Fraction as Frac
from time import time

def atan_sum(f, g):
	# a, b = f.as_integer_ratio()
	# p, q = g.as_integer_ratio()
	a, b = f._numerator, f._denominator
	p, q = g._numerator, g._denominator
	return Frac(a * q + p * b, b * q - a * p)


# input:	 n * atan(f)
# output:	g such that n * atan(f) == atan(g)
def atan_nf(n, f):
	r = Frac(0)
	while n > 0:
		if n & 1:
			r = atan_sum(r, f)
		f = atan_sum(f, f)
		n >>= 1
	return r

# [7, 10, 5, 3]
# [23, 30, 38, 182]
def check_sequence(coef, frac):
	s = Frac(0, 1)
	for c, f in zip(coef, frac):
		s = atan_sum(s, atan_nf(abs(c), Frac(1 if c > 0 else -1, f)))
	print(s, s == Frac(1, 1))

# Checking known expressions equal to tg(pi / 4) = tg(atan(1)) = 1

# print(atan_sum(atan_nf(1, Frac(1, 2)), atan_nf(1, Frac(1, 3))))
# print(atan_sum(atan_nf(4, Frac(1, 5)), atan_nf(1, Frac(-1, 239))))

def assert_all_good():
	check_sequence([1, 1], [2, 3])
	check_sequence([4, -1], [5, 239])
	check_sequence([7, 10, 5, 3], [23, 30, 38, 182])
	check_sequence([5, 2, 3], [8, 18, 57])
	check_sequence([-5, 5, -5, 5, 2, 3], [566, 109, 135, 8, 18, 57])

# assert_all_good()

print("import check_answer")
