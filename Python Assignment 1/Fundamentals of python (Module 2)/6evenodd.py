# Write a Python program to find whether a given number is even or odd,print out an appropriate message to the user.

num=int(input("Enter the given number"))

mod=num%2 #formula of modulo

if mod > 0: # if condition
    print("This is an odd number")
else:
    print("This is an even number")
 