"""vat"""
def main():
    '''main function'''
    num = float(input())
    service = num * 0.10

    if service < 50:
        service = 50
    elif service >= 1000:
        service = 1000
    vat = (num + service) * 0.07
    print('%.2f' %(vat + num + service))
main()
