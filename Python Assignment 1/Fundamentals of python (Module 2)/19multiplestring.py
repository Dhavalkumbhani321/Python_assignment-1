# Write a Python function to reverses a string if its length is a multiple of 4.
def reverse_string(str1):
    if len(str1) % 6 == 0:
       return ''.join(reversed(str1)) # define join reverse
    return str1

print(reverse_string('python')) #print the string
print(reverse_string('Nodejs')) #print the string
