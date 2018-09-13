"""Mathwar"""
def main():
    """my function"""
    even = 0
    ordd = 0
    while True:
        num = float(input())
        if num == 0:
            break
        elif num % 2 == 0:
            even += num
        elif num % 2 != 0:
            ordd += num
    if even == ordd:
        print("Draw %d" %(even))
    elif even > ordd:
        print("Even %d" %(even))
    elif ordd > even:
        print("Odd %d" %(ordd))

main()
