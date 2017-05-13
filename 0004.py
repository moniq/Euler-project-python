#=====================================
# PALINDROMIC NUMBER e.g. 9009, 90109
#=====================================
import profile


def is_palindromic(number):
    # if number < 0 or has only one digit is not palindromic
    if number-10 <= 0:
        return False
    st = str(number)
    if st == st[::-1]:
        return True
    return False


def find_palindromic(limit_min, limit_max):
    max_paldimore = [0, 0, 0]  # x*y, x, y
    for x in range(limit_max, limit_min, -1):
        for y in range(x, limit_min, -1):
            tmp = x * y
            if tmp > max_paldimore[0] and is_palindromic(tmp):
                max_paldimore = [tmp, x, y]
    return max_paldimore


profile.run('print (find_palindromic(100, 999))')
