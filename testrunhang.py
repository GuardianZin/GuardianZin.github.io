def get_dashes(word):
    clue = "_ " * len(word)
    return clue

def get_clue(word):
    clue = "@" * len(word)
    return clue


def get_letter(alreadyGuessed):
    while True:
        print('Guess a letter.')
        guess = input()
        guess == guess.lower()
        if len(guess) != 1:
            print ('Please enter a single letter.')
        elif guess in alreadyGuessed:
                print('You have already guessed that letter.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
                print('Please enter a LETTER.')
        else:
            return guess
            
def playAgain():
    print('Do you want to lay again? (yes or no.)')
    return input().lower.startswith('y')


def update_clue(word, clue, ch):
    #print(word, clue, ch)
    clue = list(clue)
    for idx, letter in enumerate(word):
        if letter == ch:
            clue[idx] = ch
    return " ".join(clue)

word = "elephant"

clue = get_clue(word)


#print(clue)
while clue != word:
    letter = get_letter()
    if letter in word:
        clue = update_clue(word, clue, letter)
print(clue)
get_letter(alreadyGuessed)
dashes = get_dashes("elephant")
print(dashes)
