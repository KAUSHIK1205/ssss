def eq(arr):
    left=0
    right=0
    n=len(arr)
    for i in range(n):
        left=0
        right=0
        for  j in range (i):

            left+=arr[j]
            for j in range(i+1,n):
                right+= arr [j]
            if left==right:return i
    return -1

arr=[4,-4,-5,5,6,-7]
print("element",arr[eq(arr)])

