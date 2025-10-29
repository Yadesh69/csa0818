num=int(input("Enter a number:"))
sum=0
temp=num
while temp>0:
    digit=temp%10
    sum+=digit
    temp=temp//10
print("Sum of Digits:",sum)
