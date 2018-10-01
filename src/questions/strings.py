"""
String Manipulation Questions

1. As a user I can enter a phrase "hello" and see it translated to Pig Latin "ellohay"
2. As a user I can enter a phrase "hello world" and see it translated to Pig Latin "ellohay orldway"

3. As a user I can enter a phrase "Hello World" and see it translated to Pig Latin "Ellohay Orldway"
# given 'h' -> 'hay'
# given 'Hello WorLD' -> 'Ellohay OrLDway'

4. As a user I can enter a phrase "Hello, world!" and see it translated to Pig Latin "Ellohay, orldway!"
5. As a user I can enter a phrase "eat apples" and see it translated to Pig Latin "eatay applesay"
"""
import string


def get_pig_latin_word(s):
    latin_ending = 'ay'

    # Handle edge cases of 0 or 1 string length
    if len(s) == 0:
        return None
    elif len(s) == 1:
        return s + latin_ending

    # Check if first letter is vowel
    vowels = ('a', 'e', 'i', 'o', 'u')
    if s[0] in vowels:
        return s + latin_ending

    # Process non-vowel pig latin
    first_letter = s[1]
    last_letter = s[0]
    last_letter_has_punctuation = s[-1] in string.punctuation

    if s[0].isupper():
        first_letter = s[1].upper()
        last_letter = s[0].lower()

    ending = s[2:] + last_letter + latin_ending
    if last_letter_has_punctuation:
        ending = s[2:-1] + last_letter + latin_ending + s[-1]

    return first_letter + ending


def get_pig_latin_phrase(phrase):
    """
    Phrase has spaces in the string.
    """
    pig_latin_words = []
    for word in phrase.split():
        pig_latin_words.append(get_pig_latin_word(word))

    return " ".join(pig_latin_words)


# A1
print(get_pig_latin_phrase('hello'))

# A2
print(get_pig_latin_phrase('hello world'))

# A3
print(get_pig_latin_phrase('Hello World'))

# A4
print(get_pig_latin_phrase('Hello, world!'))

# A5
print(get_pig_latin_phrase('eat apples'))

"""
JD ran 64 lines of Python 3 (finished in 1.26s):

ellohay
ellohay orldway
Ellohay Orldway
Ellohay, orldway!
eatay applesay

Passed all tests!
"""
