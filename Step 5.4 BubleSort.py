def bubleSort(arr):
    n= len(arr)

    for i in range (n-1,0,-1):
        for j in range (i):
            if arr[j]>arr[j+1]:
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp


arr=[3,5,2,6,4,9,8]
bubleSort(arr)

print(arr)