no = int(input("Enter an integer below 10:"))
temp = 0 
def add(no,temp):
    if no<=10:
        while no<=10:
            temp = temp + no
            print("Number is :",temp)
            no+=1
    else:
        print("Invalid input , enter integer less than 10!")
add(no,temp)
