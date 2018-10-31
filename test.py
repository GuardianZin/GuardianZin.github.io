import random

def exact_match(code,guess):
    for i in range(4):
        # print(code[i], guess[i])
        exact = ""
        if code[i] == guess[i]:
            exact = exact + 'C'
            #print(i, exact)
        return exact


def feedback(code,guess):
    for i in range(4):
        # print(code[i], guess[i])
        exact = ""
        if code[i] == guess[i]:
            exact = exact + 'C'
            #print(i, exact)
        return exact
    
    hint = exact_match(code, guess)
    

print(feedback("RRGW, GRRW"))

def random_color():
    return random.choice("RGBW")
    random.choice()

def get_code():
  code = ""
  for i in range(4):
    code = code + random_color()
  return code

def user_guess():
    prompt = "Enter 4 letters, R,G,B, or W "
    guess = input(prompt).upper()

def good_guess(guess):
  result = False


if len(guess) == 4:
 result = True

for letter in guess:
 if letter not in "RGBW":
   result = False
return result

while not good_guess(guess):
print("Bad guess, must be R,G,B, or W")
 guess = input(prompt).upper()
  return guess

#def checkAndContinue(code, guess):
  
  #while not correct answer 
    #get user guess
    #check and print feed back




    