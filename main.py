row = int(input("Enter the no. of row: "))
number = 1

for i in range(1,row+1):
    for j in range(1,i+1):
        print(number, end=" ")
        number = number+1
    print()