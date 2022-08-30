words = ["hello", "hey", "goodbye", "yo", "yes"]


def print_upper_words(words):
    for word in words:
        print(word.upper())


"""prints all words on seperate lines in uppercase"""


def print_upper_words1(words):
    for word in words:
        if word[0] == ("e") or word[0] == ("E"):
            print(word.upper())


def print_upper_words(words):
    for word in words:
        if word[0] == "h" or word[0] == "y":
            print(word.upper())


"""Only prints out words that starts with h or y in uppercase"""

# print_upper_words(["hello", "hey", "goodbye", "yo", "yes"], must_start_with={"h", "y"})
