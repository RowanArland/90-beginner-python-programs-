newListsize = int(input("Enter Size of List:"))
newList = list()
for i in range(0,newListsize):
    newList.append(input("Enter the element:"))
print("User entered list is ",newList)
def cpy(newList):
    copyList = list()
    copyList = newList.copy()
    print("The copy List is:",copyList)
cpy(newList)

    
    
