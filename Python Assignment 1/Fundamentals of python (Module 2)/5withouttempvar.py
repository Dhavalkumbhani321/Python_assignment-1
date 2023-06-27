# Write python program that swap two number without temp variable

a=int(input("enter the number a is:"))
b=int(input("enter the number b is:"))


a=a+b # value a is sum with value b in variable a
b=a-b # value a is substract value b in variable b
a=a-b # value a is subsrract value b in variable a

print("After swapping value of a",a)
print("After swapping value of b",b)