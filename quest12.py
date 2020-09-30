num1 = int (input ("Enter First Number:"))
num2 = int (input ("Enter Second Number:"))
num3 = int (input ("Enter Third Number:"))
def comp(num1,num2,num3):
    if num1<num2 and num1<num3:
        print("First Number is Lowest")
    elif num2<num1 and num2<num3:
        print("Second Number is Lowest")
    elif num3<num1 and num3<num2:
        print("Third Number is Lowest")
comp(num1,num2,num3)
