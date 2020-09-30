nolist=list()
nolist=[1,2,3,4,5]
print(nolist)
def multi(nolist):
    res=1
    for i in range(0,len(nolist)):
        res = res * nolist[i]
    print("product of the list is:",res)
multi(nolist)
