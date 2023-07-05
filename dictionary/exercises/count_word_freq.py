
# Count Word Frequency
# Define a function to count the frequency of words in a given list of words.

# Example:

words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple'] 
# count_word_frequency(words) 
# Output:

#  {'apple': 3, 'orange': 2, 'banana': 1}

def count_word_frequency(words):
    word_freq = {}
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    return word_freq

print(count_word_frequency(words))

# time complexity: O(n) where n is the length of the input list. The loop iterates through the list once,
#  and the dictionary operations (get and update) take constant time, O(1)

# space complexity: O(n) since we use a dictionary to store the word frequencies, where n
# is the number of unique words in the input list