'''main '''
def main():
    '''main function'''
    price = int(input())
    service = 0.1*price
    if service > 1000:
        service = 1000
    elif service < 50:
        service = 50
    elif service > 50:
        service = service
    vat = (price + service)*0.07
    total = price + service + vat
    print("%.2f"%(total))
main()
