no = int(input("Enter Number for prime number range :"))
def primeno(no):
    prime_list = []
    for i in range(2, no+1):
        if i not in prime_list:
            print(i)
            for j in range(i*i, no+1, i):
                prime_list.append(j)
primeno(no)
