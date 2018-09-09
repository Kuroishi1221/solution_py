"""GradeII"""
def main():
    """grade cal"""
    grade = float(input())
    if 95 <= grade <= 100:
        print("A")
    elif grade > 100 or grade <= 0:
        print('ERR')
    elif 90 <= grade < 95:
        print("B+")
    elif 85 <= grade < 90:
        print('B')
    elif 80 <= grade < 85:
        print('C+')
    elif 75 <= grade < 80:
        print('C')
    elif 70 <= grade < 75:
        print('D+')
    elif 65 <= grade < 70:
        print('D')
    elif 60 <= grade < 65:
        print('F+')
    elif 0 < grade < 60:
        print('F')
main()
