import json

incorrect_letters = []

with open("wordle_list.json") as file:
    word_list = json.load(file)


# Checks if word contains any letter from incorrect_letters array
def contains_incorrect_letter(word):
    for x in incorrect_letters:
        if x in word:
            return True

    return False


# Returns words that follow the criteria
def get_relevant_words(result, guessed_word):
    words = []
    relevant = True

    for current_word in word_list:
        # if current word contains incorrect letter, move on to next one
        # because it will always be wrong
        if contains_incorrect_letter(current_word):
            continue

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

            # letter is not in word
            else:
                incorrect_letters.append(guessed_word[i])

        if relevant:
            words.append(current_word)

    return words
