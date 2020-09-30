FirstList = [55, 55, 0, 0, 27]
print("First List" ,FirstList )
SecondList = [27, 55, 55, 0, 0]
print("Second List", SecondList)
ThirdList = [30, 55, 55, 0, 0]
print("Third List",ThirdList)
def circ_identi(FirstList, SecondList): 
    ThirdList = FirstList * 2 
    for x in range(0, len(FirstList)): 
        z = 0 
        for y in range(x, x + len(FirstList)): 
            if SecondList[z]== ThirdList[y]: 
                z+= 1
            else: 
                break	
            if z == len(FirstList): 
                return True
    return False 
 
if(circ_identi(FirstList, SecondList)): 
	print ("First List and Second List are Circularly Identical")
else: 
	print ("First List and Second List are  Not Circularly Identical")

if(circ_identi(SecondList, ThirdList)): 
	print ("Second List and Third List are Circularly Identical")
else: 
	print("Second List and Third List are Not Circularly Identical")
