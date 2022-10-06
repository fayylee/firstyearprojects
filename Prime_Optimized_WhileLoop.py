import math

n = int(input('Enter an integer number: '))

prime = True
i = 2

while i * i <= n:
    if n % i == 0:
        prime = False
        break
    i = i + 1

if prime and n != 1:
    print('This number is prime')
else:
    print('This number is not prime')
