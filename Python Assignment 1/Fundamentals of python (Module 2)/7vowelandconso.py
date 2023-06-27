# Write a Python program to test whether a passed letter is a vowel or not.
c = input("Input a letter of the alphabet: ")

if c in ('a', 'e', 'i', 'o', 'u', 'A','E','I','O','U'):# print the vowels
    print("%s is a vowel." % c)
    
elif c == 'y':# else_if condition
    print("Sometimes letter y stand for vowel, sometimes stand for consonant.")

else:
    print("%s is a consonant." % c)