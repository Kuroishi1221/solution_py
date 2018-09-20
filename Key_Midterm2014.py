""" Key_Midterm2014 """

def main():
    """ a """
    text = input()
    count_1 = 0
    for i in text:
        count_1 += int(i)
    count_2 = (int(text)%1000)*10
    key = count_1+count_2
    if key > 9999:
        key %= 10000
    elif key < 1000:
        key += 1000
    print('%04d'%(key))
}
main()
