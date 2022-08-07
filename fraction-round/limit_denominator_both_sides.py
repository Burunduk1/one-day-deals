from fractions import Fraction as Frac

# same as https://github.com/python/cpython/blob/main/Lib/fractions.py
def limit_denominator_both_sides(f, max_denominator=1000000):
    if max_denominator < 1:
        raise ValueError("max_denominator should be at least 1")
    if f._denominator <= max_denominator:
        return (Frac(f), Frac(f)) # make two copies

    p0, q0, p1, q1 = 0, 1, 1, 0
    n, d = f._numerator, f._denominator
    while True:
        a = n//d
        q2 = q0+a*q1
        if q2 > max_denominator:
            break
        p0, q0, p1, q1 = p1, q1, p0+a*p1, q2
        n, d = d, n-a*d
    k = (max_denominator-q0)//q1

    c1 = Frac(p1, q1, _normalize=False)
    c2 = Frac(p0+k*p1, q0+k*q1, _normalize=False)
    return (c1, c2) if c1 < f else (c2, c1)

# Test 1
x = Frac(1243434235, 2434342351)
a, b = limit_denominator_both_sides(x, 900)
print(a < x < b)
print(f"{a} <= {x} <= {b}")

# Test 2
x = Frac(31, 100)
a, b = limit_denominator_both_sides(x, 900)
print(a <= x <= b)
print(f"{a} <= {x} <= {b}")
