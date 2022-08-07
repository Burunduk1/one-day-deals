import sympy, sys

ans = []

# print(sympy.factorint(566**2 + 1))
def search(p, limit):
	global ans
	def go(x, i):
		if x > limit: return

		t = int((x - 1)**0.5 + 0.5)
		if t * t + 1 == x:
			ans.append((x, t))

		for j in range(i, len(p)):
			go(x * p[j], j)
	go(1, 0)


x = 566
# x = 30

print(sympy.factorint(x**2 + 1))
p = list(sympy.factorint(x**2 + 1)) + [2,3,5,7,11,13,19] #+ [2, 3, 5]
print(p)
search(p, 10**14)

for x in sorted(ans):
	print(x, sympy.factorint(x[1]**2 + 1))
print()

# sys.exit(0)

import math
# (17, 4)
# (901, 30)

# WA: nums = [30, 38, 182]
# OK: nums = [23, 30, 38, 182]
# nums = [30, 182, 268, 242] # 30, 38, 182, 242, 268
# nums = [566, 109, 135, 57, 6826318]
# nums = [566, 109, 135, 57, 18]
# nums = [23, 30, 38, 182]

# coef[0] != 0 (so it founds solution for nums[0])
nums = [566, 109, 135, 8, 18, 57]
# nums = [23, 30, 38, 182]

# |coef| <= M
M = 9

# 7*artcg(1/23) + 10*artcg(1/30) + 5*artcg(1/38) + 3*arctg(1/182)
# [7, 10, 5, 3]
# [23, 30, 38, 182]

# 8*arctg(1/57) - 5*arctg(1/239) + 12*arcg(1/18)
# [8, -5, 12]
# [57, 239, 18]

for x in nums:
	print(x, sympy.factorint(x * x + 1))
goal = math.pi / 4
xs = [math.atan(1/num) for num in nums]
print(goal)
for x in xs: 
	print(x)
print()

k = len(xs)
best = [1] + [0] * k
coef = [0] * k

def search_coef(i, goal):
	global best, coef
	if i == k-1:
		tmp = goal / xs[i]
		err = abs(tmp - round(tmp))
		# print(err, i, coef, goal)
		if err < best[0]:
			coef[i] = int(round(tmp))
			best = [err] + coef.copy()
			print(f"err={best[0]}")
		return
	for y in range(-M,M):
		if y == 0 and i == 0: continue
		coef[i] = y
		search_coef(i+1, goal - coef[i]*xs[i])
search_coef(0, goal)

print()
print(f"err={best[0]} seems {best[0]<1e-10}")

coef = best[1:]
print(coef)
print(nums)

from check_answer import check_sequence
print("Checking... ", end="")
print(check_sequence(coef, nums))

# print(x*best[1] + y*best[2] + z*best[3])
# print(1/10 + 2/10 - 3/10)

# $$\frac{\pi}{4} = 7\arctg\frac{1}{23} + \boxed{\color{red} 10\arctg\frac{1}{30}} + 5\arctg\frac{1}{38} + 3\arctg\frac{1}{182}$$
def tex_str():
	global coef, nums
	def part(c, n):
		c = abs(c)
		return "%s\\arctg\\frac{1}{%d}" % ("" if c == 1 else str(c), n)
	def sign(c, plus, minus):
		assert(c != 0)
		return plus if c > 0 else minus
	s = "$$\\frac{\\pi}{4} = \\boxed{\\color{red} %s%s}" % (sign(coef[0], "", "-"), part(coef[0], nums[0]))
	for c, n in list(zip(coef, nums))[1:]:
		s += " %s %s" % (sign(c, "+", "-"), part(c, n))
		# print(c, n)
	s += "$$"
	return s

print(tex_str())
