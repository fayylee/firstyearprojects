a = int(input('Enter the first digit '))
b = int(input('Enter the second digit '))
c = int(input('Enter the third digit '))

if a > b and a > c:
    if b < c:
        Largest = a * 100 + c * 10 + b
        Smallest = b * 100 + c * 10 + a
    else:
        Largest = a * 100 + b * 10 + c
        Smallest = b * 100 + c * 10 + a
elif b > a and b > c:
    if a < c:
        Largest = b * 100 + c * 10 + a
        Smallest = a * 100 + c * 10 + b
    else:
        Largest = b * 100 + a * 10 + c
        Smallest = c * 100 + a * 10 + b
else:
    if b < a:
        Largest = c * 100 + a * 10 + b
        Smallest = b * 100 + a * 10 + c
    else:
        Largest = c * 100 + b * 10 + a
        Smallest = a * 100 + b * 10 + c

print('Largest =', Largest)
print('Smallest =', Smallest)
