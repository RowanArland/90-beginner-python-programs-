firstlist = list()
secondlist=list()
lengthofList = int(input("Enter Size of List:"))
for i in range(0,lengthofList):
    firstlist.append(input("Enter value of First list: "))
    
for j in range(0,lengthofList):
    secondlist.append(input("Enter value of Second list: "))
print("1st",firstlist)
print("2nd",secondlist)
firstlist.extend(secondlist)
print("appended",firstlist)
    
