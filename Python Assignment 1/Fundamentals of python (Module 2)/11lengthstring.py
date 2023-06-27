# Write a Python program to calculate the length of a string.
def string_length(str1): # define the string length
    count = 0
    for char in str1: 
        count += 1
    return count
print(string_length("I am dhaval")) # print string length 