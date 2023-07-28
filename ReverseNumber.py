number = int(input("Enter the Number:"))
rev = 0

while number!=0:
    rem = number % 10
    rev = rem + (rev*10)
    number = int(number/10)

print(f'Reverse = {rev}')