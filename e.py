def sas(a,n,s):
    for i in range(n):
        cs=a[i]
    j=i+1
    while j<=n:

        if cs==s:
            print("sum found in btw")
            print("index /d and /d"%(i,j-1))
            return 1
        if cs >s or j==n:
            break
        cs=cs+a[i]
        j+=1
    print ("no subarray found")
a=[3,2,5,5,9,3,4,5,3,2,3,5]
n=len(a)
s=10
sas(a,n,s)
