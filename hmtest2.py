import random

def read_file():
  f = open("wordlist.txt")
  words = f.read()
  words = words.split("\n")
  return words

def get_letter():
    letter = input("Letter please ")
    while len(letter) < 1:
        letter = input("Letter please ")
    return letter[0].lower()
    print(letter)


def get_a_word(words, min_len=4, max_len=7):
  word = random.choice(words)

  while len(words) < min_len or len(word) > max_len:
    word = random.choice(words)

  return word

def get_clue(word):
  return "@" * len(word)


words_list = read_file()
word = get_a_word(words_list)
clue = get_clue(word)
print(clue, word)
get_letter()