"""Divide3or5"""
def main():
    """(づ｡◕‿‿◕｡)づ"""
    result = 0
    for i in range(1, int(input()) + 1):
        if i % 5 == 0 or i % 3 == 0:
            result += i
    print(result)
main()
