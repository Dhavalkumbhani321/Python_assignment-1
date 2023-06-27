# Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5.

def test_number5(a, b):
    if a == b or abs(a-b) == 5 or (a+b) == 5: 
        return  True
    else:
         return False
print(test_number5(7, 2)) #print the number
print(test_number5(3, 2)) #print the number
print(test_number5(2, 2)) #print the number
print(test_number5(7, 3)) #print the number
print(test_number5(27, 53)) #print the number
