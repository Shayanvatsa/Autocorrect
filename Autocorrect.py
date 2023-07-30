import nltk
from nltk.corpus import words
from nltk.metrics.distance import edit_distance


nltk.download('words')


Eng_word = set(words.words())
def auto_correct(word):
    word = word.lower()  
    if word in Eng_word:
        return word
    min_distance = float('inf')
    nearest_word = None

    for w in Eng_word:
        distance = edit_distance(word, w)
        if distance < min_distance:
            min_distance = distance
            nearest_word = w
    return nearest_word
while True:
    input_word = input("Enter a word (type 'exit' to stop): ")

    if input_word.lower() == 'exit':
        break
    corrected_word = auto_correct(input_word)
    print("Input Word:", input_word)
    print("Corrected Word:", corrected_word)
