import random

def rps():
  computer_pick = random.randint(1, 3)
  if computer_pick == 1:
      rock()
  elif computer_pick == 2:
      paper()
  else:
      scissors()

def rock():
  rps()
  human_pick = input("1:Rock, 2:Paper, 3:Scissors")
  print(human_pick)
  print("vs")
  print("computer: 1")
  if human_pick == "1":
    print ("Tie!")
    try_again()
  if human_pick == "2":
    print ("Lose!")
    try_again()
  if human_pick == "3":
    print ("Win!")
    try_again()

  else:
    print("Try again")
    rock()

def paper():
  human_pick = input("1:Rock, 2:Paper, 3:Scissors")
  print(human_pick)
  print("vs")
  print("computer: 2")
  if human_pick == "1":
    print("Lose!")
    try_again()
  if human_pick == "2":
    print("tie!")
    try_again()
  if human_pick == "3":
    print("Win!")
    try_again()

  else:
    print("Try again")
    paper()

def scissors():
  human_pick = input("1:Rock, 2:Paper, 3:Scissors")
  print(human_pick)
  print("vs")
  print("computer: 3")
  if human_pick == "1":
    print("Lose!")
    try_again()
  if human_pick == "2":
    print("Win!")
    try_again()
  if human_pick == "3":
    print("Tie!")
    try_again()

  else:
    print("Try again")
    scissors()

def try_again():
  choice = input("Play Again?y/n ")
  if choice == "y" or choice == "yes" or choice == "Y":
    rps()
  elif choice == "n" or choice == "no" or choice == "N":
      print("Thanks")
      quit()
  else:
    print("Try again")
    try_again()



rps()