def prime (n, i ) :
    if i == 1:
        return 1
    if n % i == 0 :
        return 0 
    return prime (n, i - 1)

n = int(input("enter number: "))
ind = prime(n, n-1)
if  ind == 1 :
    print("prime") 
else:
    print("not prime")
