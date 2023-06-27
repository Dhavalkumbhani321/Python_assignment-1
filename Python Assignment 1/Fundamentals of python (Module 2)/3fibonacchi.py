# Write a Python program to get the Fibonacci series of given range. 
num = int(input("Enter the number "))
# first two terms
n1, n2 = 0, 1
count = 0

# check if the number of terms is valid
if num in range (num<= 0):
    print("Please enter a positive integer")
elif num in range (num== 1):
    print("Fibonacci sequence upto",num,":")
    print(n1)
else:
    print("Fibonacci sequence:")
    while count < num:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1