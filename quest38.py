elementListsize = int(input("Enter List Size:"))
elementList = list()

for i in range(0,elementListsize):
    elementList.append(input("Enter Element:"))
print(elementList)

def manip(elementListsize,elementList):
    elno = int(input("Enter number of Elements you wish to remove:"))
    removed_element = list()
    for i in range(0,elno):
        elementno = int(input("Enter Element position to be removed:"))
        removed_element.append(elementList.pop(elementno))
        print(elementList)
    print("Items you have removed",removed_element)
manip(elementListsize,elementList)
