"""triangle"""
def main():
    """io"""
    num1 = float(input())
    num2 = float(input())
    num3 = float(input())
    hhh = checkhigh(num1, num2, num3)
    mmm = checkmid(num1, num2, num3)
    lll = checklow(num1, num2, num3)
    pakrob = (mmm**2 + lll**2)
    total = hhh**2
    n11 = two(total, pakrob)
    n22 = one(total, pakrob)

    if n11 - n22 <= 0.01:
        print('Yes')
    else:
        print('No')
def two(num1, num2):
    """2s check"""
    if num1 > num2:
        return num1
    else:
        return num2

def one(num3, num4):
    """2 check"""
    if num3 < num4:
        return num3
    else:
        return num3
def checkhigh(high, mid, low):
    """check high"""
    if high >= mid >= low:
        return high
    if mid >= low >= high:
        return mid
    if low >= high >= mid:
        return low
    if high >= low >= mid:
        return high
    if mid >= high >= low:
        return mid
    if low >= mid >= high:
        return low

def checkmid(high, mid, low):
    """check mid"""
    if high >= mid >= low:
        return mid
    if mid >= low >= high:
        return low
    if low >= high >= mid:
        return high
    if high >= low >= mid:
        return low

    if mid >= high >= low:
        return high

    if low >= mid >= high:
        return mid
def checklow(high, mid, low):
    """check low"""
    if high >= mid >= low:
        return low
    if mid >= low >= high:
        return high
    if low >= high >= mid:
        return mid
    if high >= low >= mid:
        return mid
    if mid >= high >= low:
        return low
    if low >= mid >= high:
        return high
main()
