def number_of_repeated_words(input_sentences):
    words = input_sentences.lower().split()
    word_count = {}

    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

    max_frequency = max(word_count.values())
    most_frequent_words = [word for word, count in word_count.items() if count == max_frequency]
    return most_frequent_words, max_frequency


''' This is a sample paragraph. It contains several words, some of which are repeated. This is a good exercise to find the most frequent words.
Most Frequent Word(s): ['this', 'is', 'a']
Frequency: 2 '''
input_str = input("please enter your sentences : ")
result_words, result_frequency = number_of_repeated_words(input_str)

print("Most Frequent Word(s):", result_words)
print("Frequency:", result_frequency)
