enternumber = int(input("Enter Number of items to enter in the list:"))
def segrigation(enternumber):
    number = list()
    for i in range(0,enternumber):
          number.append(int(input("Enter Number:")))
    print("Original list:",number)
    for j in range(0,len(number)):
        temp = number[j]
        if temp%2 == 0:
            number.pop(j)
            print(number)
segrigation(enternumber)
