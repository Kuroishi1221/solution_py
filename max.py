"""PlanCDEFGHIJKLMNOPQRSTUVWXYZ"""
def main():
    """io function"""
    text = input()
    num1 = float(input())
    num2 = float(input())
    num3 = float(input())


    if text == "Descend":
        print("%.2f, %.2f, %.2f"% (checkhigh(num1, num2, num3), \
            checkmid(num1, num2, num3), checklow(num1, num2, num3)))

    if text == 'Ascend':
        print("%.2f, %.2f, %.2f"% (checklow(num1, num2, num3), \
            checkmid(num1, num2, num3), checkhigh(num1, num2, num3)))

    if text == "A" and num1 == num2 == num3:
        print("%.2f, %.2f, %.2f"% (num1, num2, num3))

    if text == "A" and num1 == num2 == num3:
        print("%.2f, %.2f, %.2f"% (num1, num2, num3))

    if text == "A" and num1 == num2 > num3:
        print("%.2f, %.2f, %.2f"% (num1, num2, num3))


    elif text == "B" and num1 == num2 < num3:
        print("%.2f, %.2f, %.2f"% (num1, num2, num3))

    elif text == "B" and num1 < num2 == num3:
        print("%.2f, %.2f, %.2f"% (num1, num2, num3))

    elif text == "B" and num1 > num2 == num3:
        print("%.2f, %.2f, %.2f"% (num1, num2, num3))


    elif text == "C" and num1 == num2 > num3:
        print("%.2f, %.2f, %.2f"% (num1, num2, num3))

    elif text == "C" and num1 == num2 < num3:
        print("%.2f, %.2f, %.2f"% (num1, num2, num3))

    elif text == "C" and num1 < num2 == num3:
        print("%.2f, %.2f, %.2f"% (num1, num2, num3))

    elif text == "C" and num1 > num2 == num3:
        print("%.2f, %.2f, %.2f"% (num1, num2, num3))

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
