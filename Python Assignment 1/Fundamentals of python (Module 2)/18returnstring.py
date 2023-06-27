# Write a Python function that takes a list of words and returns the length of the string.

def find_longest_word(words_list):
    word_len = []
    for n in words_list:
        word_len.append((len(n), n)) #define word length
    word_len.sort()
    return word_len[-1][0], word_len[-1][1] 
result = find_longest_word(["Java", "Python", "Nodjs","Flutter"]) # print the stirng
print("\nLongest word: ",result[1]) #print longest word
print("Length of the longest word: ",result[0]) #print the length of the longest word