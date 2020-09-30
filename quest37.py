itemno = int(input("Enter Number of items to enter in the list:"))

itemlist1 = list()
for i in range(0,itemno):
          itemlist1.append(input("Enter Item in list 1:"))
print("First List",itemlist1)
          
itemlist2 = list()
for j in range(0,itemno):
          itemlist2.append(input("Enter Item in list 2:"))
print("Second List",itemlist2)

def compare(itemno,itemlist1,itemlist2):
    for l in range(0,itemno):
        for m in range(0,itemno):
            if itemlist1[l] == itemlist2[m]:
                print("common item found!!!")
compare(itemno,itemlist1,itemlist2,)
    

