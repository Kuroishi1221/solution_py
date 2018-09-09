"""GradeIII"""
def main(num, total=0):
    """calculated"""
    for _ in range(num):
        score = float(input())
        if 100 >= score >= 95:
            total += 4
        elif 95 > score >= 90:
            total += 3.5
        elif 90 > score >= 85:
            total += 3
        elif 85 > score >= 80:
            total += 2.5
        elif 80 > score >= 75:
            total += 2
        elif 75 > score >= 70:
            total += 1.5
        elif 70 > score >= 65:
            total += 1
        elif 65 > score >= 60:
            total += 0.5
        elif 60 > score >= 0:
            total += 0
    total = total / num
    total = int(total*100)/100
    print("%.2f" % (total))
main(int(input()))

