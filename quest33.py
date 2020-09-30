itemno = int(input("Enter Number of items to enter in the list:"))
itemlist= list()
count = 0
count2 = 0
def tryu(itemno,itemlist,count,count2):
     for i in range(0,itemno):
          itemlist.append(input("Enter Item:"))    
     print(itemlist)
     for j in range(0,len(itemlist)):
         if len(itemlist[j]) >= 2:
             count = count + 1
             temp = itemlist[j]
             if temp[0]==temp[-1]:
                 count2 = count2 + 1
     print("Items in the List with Length equal or greater than 2 is:",count)
     print("Stings with First an Last string value same is:",count2)
tryu(itemno,itemlist,count,count2)
