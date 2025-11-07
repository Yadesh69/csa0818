def rsum(n):
    if n == 0:
        return 0
    return (n % 10) + rsum(n // 10)
def rpro(n):
    if n == 0:
        return 1
    return (n % 10) * rpro(n // 10)
n = int(input("Enter a number: "))
sum_digits = rsum(n)
prod_digits = rpro(n)
print("Sum of digits:", sum_digits)
print("Product of digits:", prod_digits)
if sum_digits == prod_digits:
    print(n, "is a Lucky Number")
else:
    print(n, "is Not a Lucky Number")
