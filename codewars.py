# first problem EVEN OR ODD``


def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


# second problem CONVERT A NUMBER TO A STRING


def number_to_string(num):
    new = str(num)
    return new


# third problem REMOVE STRING SPACES


def no_space(x):
    return x.replace(" ", "")


# forth problem VOWEL COUNT


def get_count(sentence):
    count = 0
    vowels = ["a", "e", "i", "o", "u"]
    for char in sentence:
        if char in vowels:
            count += 1
    return count