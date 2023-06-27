#write a program to count the number of characters(character frequency) in a string.
num=input("Enter the String: ").lower() 
s={}
for i in num: 
    if i in s: # if else condtion
        s[i]+=1
    else:
        s[i]=1
print(s)