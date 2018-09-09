"""data_spike"""
def main():
    """main func"""
    result = 0
    A = calc(int(input()), int(input()))
    B = calc(int(input()), int(input()))
    C = calc(int(input()), int(input()))
    D = calc(int(input()), int(input()))

    E = calc(A, B)
    F = calc(C, D)
    result = calc(E, F)

    print(result)

def calc(num1, num2):
    """calculate"""
    if num1 > num2:
        return num1
    else:
        return num2

main()
