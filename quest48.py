exp48 = list()
exp48size = int(input("Enter Size :"))
for i in range(0,exp48size):
    exp48.append(input("Enter Value :"))
print("list entered is :", exp48)
findindex = input("Enter Value who's index you want to find from list :")
print(exp48.index(findindex))
