def kad(a):
    n=len((a))
-
def mcs(a):
    n=len(a)

    mk=kad(a)
    mw=0
    for i in range(0,n):
        mw+=a[i]
        a[i]=-a[i]

    if mw>mk:
        return mw
    else:
        return mk
a=[11,12,-30,123,-424,92]
print("maimum circulating sum",mcs(a))


    

