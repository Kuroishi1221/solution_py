""" FOR!F-Ball """

def main():
    """
    current state == 1, left
    current state == 2, center
    current state == 3, right
    """
    moves = input()
    current_state = 1
    for i in moves:
        if i == "A":
            if current_state == 1:
                current_state = 2
            elif current_state == 2:
                current_state = 1
        elif i == "B":
            if current_state == 2:
                current_state = 3
            elif current_state == 3:
                current_state = 2
        elif i == "C":
            if current_state == 3:
                current_state = 1
            elif current_state == 1:
                current_state = 3

    print(current_state)

main()
