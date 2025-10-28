#swapping two numbers without using temp variable
a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
print("The numbers before swapping:",a,b)
a=a+b
b=a-b
a=a-b
print("The numbers after swapping:",a,b)
