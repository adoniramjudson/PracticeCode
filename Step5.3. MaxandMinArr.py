def MaxMin (arr, size):
    max= arr[0]
    min= arr[0]

    for i in range (0,size):
        if arr[i]>max:
            max=arr[i]

    print (max)

    for i in range (0,size):
        if arr[i]<min:
            min=arr[i]

    print(min)

arr=[12,13,15,17,20,21,22,24,25]
size=len(arr)

MaxMin (arr, size)