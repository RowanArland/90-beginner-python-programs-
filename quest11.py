num1 = int (input ("Enter First Number:"))
num2 = int (input ("Enter Second Number:"))
num3 = int (input ("Enter Third Number:"))
def comp(num1,num2,num3):
    if num1>num2 and num1>num3:
        print("First Number is greatest")
    elif num2>num1 and num2>num3:
        print("Second Number is greatest")
    elif num3>num1 and num3>num2:
        print("Third Number is greatest")
comp(num1,num2,num3)
