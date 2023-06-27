# Write a Python program to count the occurrences of each word in a given sentence.
 
def word_count(str):
    counts = dict()
    words = str.split() #split the words

    for word in words: 
        if word in counts:
            counts[word] += 1 #count the words
        else:
            counts[word] = 1

    return counts

print( word_count("i am dhaval and i living in surat")) #print the words