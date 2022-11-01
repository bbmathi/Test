# Write a program or algorithm to implement bubble sort. 
#lst = [85,65,45,35,25,95]

# lst.sort()
# print(lst)
# lst.sort(reverse=True)
# print(lst)

def bubbleSort(arr):
    n = len(arr)
    swapping = False
    for i in range(n-1):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                swapping = True
                arr[j],arr[j+1]=arr[j+1],arr[j]
        if not swapping:
            return 

arr= [85,65,45,35,25,95]
bubbleSort(arr)
print(arr)

