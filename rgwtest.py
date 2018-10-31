import random

def guess():  #users pick
    prompt = "Enter 4 letters, R,G,B, or W "
    guess = input(prompt).upper()
    
    while not good_guess(guess):
        print("Bad input, must be R,G,B, or W")
        guess = input(prompt).upper()
     
    return guess

def good_guess(guess):
    result = False
    if len(guess) == 4:
        result = True
        for letter in guess:
            if letter not in "RGBW":
                result = False
        
    return result

def look_for_exact(code, guess):
    result = ""
    new_code = ""
    new_guess = ""
    for i in range(4):
        if code[i] == guess[i]:
            result = result +  "C"
        else:
            new_code = new_code + code[i]
            new_guess = new_guess + guess[i]
            
    return result, new_code, new_guess

def match_for_color(new_code, new_guess):
    result = ""
    sec_code = ""
    sec_guess = ""
    for i in range(len(new_code)):
        if new_code[i] == new_guess[i]:
            result = result + "B"
        else:
            sec_code = sec_code + new_code[i]
            sec_guess = sec_guess + new_guess[i]
        
    return result

def hint(code, guess):
    result, new_code, new_guess = look_for_exact(code, guess)
    result = result + match_for_color(new_code, new_guess)
    return result

    #look for match of color only
    #Note: excact match have been removed
    #return a B for each color match
    
def main():
    code = "RGBW"
    user_guess = guess()
    print( hint(code, user_guess) )
    
main()
