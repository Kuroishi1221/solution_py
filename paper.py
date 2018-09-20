"""RPS"""
def main():
    """RPS"""
    text = input()
    score1 = 0
    score2 = 0

    for i in range(0, len(text), 2):
        if text[i:i+2] == "SR" or text[i:i+2] == "RP" or text[i:i+2] == "PS":
            score2 += 1
        elif text[i:i+2] == "RS" or text[i:i+2] == "PR" or text[i:i+2] == "SP":
            score1 += 1
    if score1 == score2:
        print('DRAW %d' %(score2))
    elif score1 > score2:
        print('A win %d-%d' %(score1, score2))
    elif score2 > score1:
        print('B win %d-%d' %(score2, score1))
main()
