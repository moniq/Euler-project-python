import itertools
from math import sqrt
import profile


divisions_dict = {}


def get_range(x):
    if not divisions_dict.get(x):
        divisions_dict[x] = list(itertools.chain(*[[d, x/d]
                       for d in range(1, int(sqrt(x))+1)
                       if x % d == 0]))
    return divisions_dict.get(x)


def get_triang(maxlen, k=1):
    for k in range(maxlen**2):
        if k % 2:
            x, y = (k + 1)/2, k
        else:
            x, y = k/2, k + 1
        if len(get_range(x)) * len(get_range(y)) >= maxlen:
            return x*y


profile.run('print(get_triang(500))')
