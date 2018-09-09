"""Surprise"""
def main():
    """io"""
    total = float(input())
    higher = float(input())
    cal = total - higher
    ans = cal // 2 or cal / 2 #score two guy

    if higher - ans >= 2:
        print('Surprising')
    else:
        print('Not surprising')
main()
