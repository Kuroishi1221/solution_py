"""weight"""
def main():
    """cal weight"""
    total = float(input())
    obj1 = float(input())
    obj2 = float(input())
    obj3 = float(input())

    half = total / 2
    unknow = (total*4) - obj1 - obj2 - obj3
    four = obj1 + obj2 + obj3 + unknow


    if four > 15000:
        print('Overweight')

    elif obj1 < 2*total and obj2 < 2*total and obj3 < 2*total and unknow < 2*total:
        if obj1 > half and obj2 > half and obj3 > half and unknow > half:
            print("Pass %.2f" % unknow)
        else:
            print('Unbalance')


    else:
        print('Unbalance')
main()
