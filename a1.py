number=int(input("Enter number to check"))
print("Number to be : ", number)

if number%2==0:
    print(number, "is an even number")

elif number%2==1:
    print(number, "is an odd number")

else:
    print(number, "is not a valid input")