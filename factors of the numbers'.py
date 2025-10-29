x=int(input("Enter a number:"))
y=[]
print("The factors of",x,"are")
for i in range(1,x):
    if x%i==0:
        y.append(i)
print(y)
print("Number of factors",len(y))
n=int(input("Enter N value:"))
if n>len(y):
    print("Invalid")
else:
    print("First",n,"factors:")
    for k in range(0,n):
        print(y[k],end='')
