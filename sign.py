"""Sign"""
def main():
    """main function"""
    size, style, text = int(input()), input(), input()
    count = len(text)
    if (size-count)%2 == 1:
        space = 1
    else:
        space = 0

    if style == "left":
        print(text)
    elif style == "right":
        print(" "*(size-count)+text)
    else:
        half = (size-count)//2
        print(" "*half+(" "*space)+text+" "*half)

main()
