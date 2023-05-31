def find_odd_sum (arr):
    subarrays = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr) + 1):
            subarray = arr[i:j]
            if sum (subarray) % 2 == 1 :
                subarrays.append(subarray)
                return subarrays
            arr = []
            n  = int (input("enter the number of elements"))
            for i in range (0,n):
                ele = int(input())
                arr.append(ele)
                odd_sum = find_odd_sum(arr)
                print(odd_sum)
                
