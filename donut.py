"""donut"""
def main():
    """Delicious"""
    price = int(input()) 
    pro = int(input())
    free = int(input())
    need = int(input())
    pay = need//(pro + free)*pro
    pay += need %(pro + free) if need%(pro + free) < pro else pro
    print("{} {}".format(pay*price, pay+pay//pro*free))
main()
    
        
