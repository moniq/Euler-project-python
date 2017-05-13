#======================
# PITAGORAS
#======================
from math import sqrt
import profile


def calculate(expected_sum):
    for a in range(1, expected_sum):
        for b in range(a, expected_sum):
            c = expected_sum - (a + b)
            if (c > 0 and (c**2 == a**2 + b**2)):
                        assert (a + b + c == expected_sum)
                        return [a, b, c]


profile.run('print(calculate(1000))')
