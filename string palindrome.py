string=input("Enter a string:")
string=string.lower()
reverse_string=string[::-1]
if string==reverse_string:
    print("It is a palindrome")
else:
    print("It is not a palindrome")
