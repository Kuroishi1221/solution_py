"""segment"""
def main():
    """lift is strange"""
    result = 0
    while True:
        num = input()
        if num == "0":
            break
        while int(num) >= 10:
            for i in num:
                result += int(i)
            num = str(result)
            result = 0
        print(num)
main()

        
            
            
        
        
