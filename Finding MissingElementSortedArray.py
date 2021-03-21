def missingElemnet (arr,N):

    diff = arr[0]

    for i in range (N):
        if (arr[i]-i!=diff):

            while (diff<arr[i]-1):
                print(i+diff, end='')
                diff += 1


arr = [6,7,10,11,13]
N=len(arr)

missingElemnet(arr,N)