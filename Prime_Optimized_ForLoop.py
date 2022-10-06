import math

n = int(input('Enter an integer number: '))

m = int(math.sqrt(n)) + 1
prime = True

for i in range(2, m):
    if n % i == 0:
        prime = False
        break

if prime and n != 1:
    print('This number is prime')
else:
    print('This number is not prime')
