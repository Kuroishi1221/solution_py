"""GiftIII"""
def main():
    """main func"""
    num = int(input())
    numa = 0
    numb = 0
    for _ in range(num):
        num1 = int(input())
        if num1 > numa:
            numb = numa
            numa = num1
        if num1 > numb and num1 < numa:
            numb = num1
 
    if numa != 0 and numb != 0:
        print(numb)
    else:
        print("Exit")
 
main()
