number1 =  int(input("Enter  1st-digit of number to check if it is a armstrong number:"))
number2 =  int(input("Enter  2nd-digit number to check if it is a armstrong number:"))
number3 =  int(input("Enter  3rd-digit number to check if it is a armstrong number:"))
def arm(number1,number2,number3):
    sumn = (number1**3)+(number2**3)+(number3**3)
    if sumn == ((number1*100)+(number2*10)+(number3)):
        print("the entered digits form an armstrong number")
    else:
        print("the entered digits dont form an armstrong number")
arm(number1,number2,number3)
