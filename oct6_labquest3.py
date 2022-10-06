n = str(input('Enter a word: '))
m = str(input('Enter another word: '))

# outer if and else condition checks the length (boolean sort, does the length of the first word match the length of the second?)
if(len(n) == len(m)):

    # sort the strings
    sorted_n = sorted(n)
    sorted_m = sorted(m)

    # if sorted char arrays are same, print the appropriate output:
    if(sorted_n == sorted_m):
        print(n + " and " + m + " are anagram.")
    else:
        print(n + " and " + m + " are not anagram.")

else:
    print(n + " and " + m + " are not anagram.")
