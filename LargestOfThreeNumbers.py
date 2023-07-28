# a = 25
# b = 50
# c = 10

a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
c=int(input("Enter the thrid number:"))

if a>b and a>c:
    largest = a
elif b>a and b>c:
    largest =b
else:
    largest=c

print(f"Largest number ={largest}")