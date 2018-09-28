"""gift"""
def main():
    """main function"""
    num = int(input())
    first = 0
    sec = 0
    for _ in range(num):
        gift = int(input())
        if gift > first:
            sec = first
            first = gift
        if gift > sec and gift < first:
            sec = gift
    if sec != 0 and first != 0:
        print(sec)
    else:
        print('Exit')
main()

