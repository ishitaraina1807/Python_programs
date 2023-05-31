#fabonacci series using recursion :
def fabonacci (n) :
    if n <= 1 :
        return n
    else:
        return ( fabonacci(n-1) + fabonacci(n-2) )
terms = int(input("enter the number of terms"))
if terms <= 1 :
        print("cannot print fabonacci series")
else :
    for i in range (terms) :
        print(fabonacci(i)) 
