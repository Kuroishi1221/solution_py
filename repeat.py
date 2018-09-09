"""reapeater"""
def main():
    """main function"""
    num = int(input())
    if num % 4 == 0 and num % 100 != 0:
        print('Yes')
    elif num % 400 == 0:
        print('Yes')
    else:
        print('No')
main()

