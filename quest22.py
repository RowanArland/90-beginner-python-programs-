age=int(input("Enter the age:"))
def agevalidate(age):
    if(age<18):
        print("You are minor and you are not eligible to work")
    elif(18<=age<60):
        print("Eligible to work, fill your details and apply")
    else:
        print("Too old to work, collect your pension")

agevalidate(age)
        
                  
