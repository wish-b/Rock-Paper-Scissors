import random

while True:
  user_name= input("Enter your name: ") #username
  if user_name:
    break
  print("Name cannot be empty! ")

  print(f"Hi {user_name} , welcome to the game")
  print("Please select \n r for rock \n p for paper \n s for scissor")
  print("What do you choose")

  game_dictonary = {"r":1,"p":0,"s":-1} 
  rev_game_dictonary = {1:"Rock",0:"Paper",-1:"Scissor"}


  user_input = input("Rock,Paper,Scissor: ").lower() #user choose r,s,p
  if user_input not in ("r","p","s"):
      print("Invalid")
      continue

  computer = random.choice([1,0,-1]) #choose random number for computer
  you = game_dictonary[user_input] #r,p,s converted into number of user
  computer_input = rev_game_dictonary[computer] # number converted into r,p,s of computer


  print(f"{user_name} chosen {rev_game_dictonary[you]}\ncomputer chosen {computer_input}") #prints what we choose

  if (you == computer):
    print("It's a Draw")
  elif (you == 1 and computer == -1):
    print(f"{user_name} wins")
  elif (you == 0 and computer == 1):
    print(f"{user_name} wins")
  elif (you == -1 and computer == 0):
    print(f"{user_name} wins")
  else:
    print("computer wins")
      
  user_choice = input("Do you want to continue (y/n): ").lower()
  if user_choice == "n":
    print("Thanks for playing")
    break
  elif user_choice != "y":
    print("Invalid input, continuing game...")
    
