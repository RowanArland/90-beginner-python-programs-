exp45list1 = list()
exp45list2 = list()

sizeoflist1 = int(input("Enter the size of list 1:"))
sizeoflist2 = int(input("Enter the size of list 2:"))

for i in range(0,sizeoflist1) :
    exp45list1.append(int(input("Enter value for list 1:")))
print("First list :" ,exp45list1)

for j in range(0,sizeoflist2):
    exp45list2.append(int(input("Enter value for list 2:")))
print("Second list :" ,exp45list2)

print("Difference between the lists :",set(exp45list1) - set(exp45list2))
