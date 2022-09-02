import json

with open("wordle_list.json") as file:
    word_list = json.load(file)


def get_relevant_words(result, guessed_word):
    words = []
    relevant = True

    for current_word in word_list:
        for i in range(0, 5):

            # current letter in guessed word is in same position as word
            if result[i] == "G":
                relevant = guessed_word[i] == current_word[i]
                if not relevant:
                    break

            # current letter in guessed word is in word at different position
            elif result[i] == "Y":
                relevant = guessed_word[i] in current_word
                if not relevant:
                    break

        if relevant:
            words.append(current_word)

    return words
