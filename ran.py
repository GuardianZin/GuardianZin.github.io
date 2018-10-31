import random

def random_color():
 return random.choice("RGBW")

def correct_color(code, guess):
    return ""

def exact_match(code, guess):
    exact = ""
    codeNM = ""
    guessNM = ""
    
    for i in range(4):
        print(code[i], guess[i])
        if code[i] == guess[i]:
            exact = exact + 'C'
        else:
            codeNM = codeNM + code[i]
            guessNM = guessNM + guess[i]
            #print(i, exact)
            return exact, codeNM, guessNM
        


def feedback(code, guess):
    hint, codeNM, guessNM = exact_match(code, guess)
    hint = hint + correct_color(code, guess)
    return hint

def get_code(): #computer pick
 code = ''
 for i in range(4):
  code = code + random_color()
 return code

def good_guess(guess):
    result = False
    
    if len(guess) == 4:
        result = True
        
        for letter in guess:
         if letter not in "RGBW":
             result = False
        
    return result

def user_guess():  #users pick
    prompt = "Enter 4 letters, R,G,B, or W "
    guess = input(prompt).upper()
    
    while not good_guess(guess):
        print("Bad input, must be R,G,B, or W")
        guess = input(prompt).upper()
     
    return guess

code = get_code()
user = user_guess()
#print(code)
#print(user)
feedback(code, user)
print(feedback)