"""SceneSwitch I"""
def main(num):
    """output and input"""
    warm = 0
    result = 0
    if num == 'End':
        print(0)
    else:
        while float(num) == 0:
            num1 = input()
            if num1 == 'End':
                break
            num2 = input()
            if num2 == 'End':
                break
            elif abs(float(num1) - float(num2)) <= 6 and warm == 0:
                warm = 1
                result += 1
            else:
                warm = 0
        print(result)
main(input())

