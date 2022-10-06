
#Printing doubles with formatting
#d = 7823.1293912
#temp_d = "{:.3f}".format(d)

#print(temp_d)

#7.8231293912e3

nums = [1, 4, 5, 6, 8, 19, 20, 34, 12, 5, 10]

nums[5] = 60
print(nums)
print('The last element =', nums[-1])
print('The second to last element =', nums[-2])

#scanning an array backward by making the for loop backward
n = len(nums)
for i in range(n - 1, -1, -1):
    print(nums[i], end = ' ')

print('')

#scanning an array backward by using the negative indexes
for i in range(1, n + 1):
    print(nums[-i], end = ' ')

print('')

#using in to check if an element is in the list and then search
#for its position
x = int(input('Enter an integer: '))
if x in nums:
    a = nums.index(x)
    print(x, 'is at position =', a)
else:
    print(x, 'is not in the array')

#strings can be considered as list of characters
st = 'This is a string'
chlist = ['T', 'h', 'i', 's', ' ', 'i', 's', ' ', 'a', 's', 't', 'r', 'i', 'n', 'g']

#Counting number of 'i's in a string using scan of elements not indexes
count = 0
for ch in st:
    if ch == 'i':
        count = count + 1

print(count)

#Scanning a string via indexes is possible as long as we don't change
#the characters (characters of a string are read-only)
l = len(st)
print('length of the string =', l)

for i in range(0, l):
    print(st[i], end = ' ')

#We are allowed to change elements of a list
for i in range(0, n):
    nums[i] = 0

print(nums)

#We are not allowed to change characters of a string in Python
#for i in range(0, l):
#    st[i] = '*'

#Converting a string to a list of characters to be able to change characters
stl = list(st)
print('Converted list =', stl)
for i in range(0, l):
    stl[i] = '*'
    
#Concatenation in strings using +
st = 'Rahim' + 'Bahrami'
print(st)

#Converting back the list of characters to a string by adding characters to
#the string one by one
st = ''
for i in range(0, l):
    st = st + stl[i]
print(st)

