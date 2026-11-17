import random

print("\nWelcome to the Number Guessing Game!")

# Game repeating loop
active = True

while active:

  # Set initial guess count to 0
  guess_count = 0

  # Loop until valid input is received
  while True:

    try:

      # Prompt user for difficulty level (Easy 1-10, 
      # Medium 1-50, Hard 1-100, Expert 1-1000)
      print("\nDifficulty Levels:")
      print(" 1. Easy")
      print(" 2. Medium")
      print(" 3. Hard")
      print(" 4. Expert")

      difficulty = int(input("Enter the difficulty level you wish to play on: "))

      # Check input and set the cap number (ex. Easy the cap = 10)
      if difficulty == 1:
        print("\nDifficulty set to Easy. Good luck!")
        cap = 10
        break

      elif difficulty == 2:
        print("\nDifficulty set to Medium. Good luck!")
        cap = 50
        break

      elif difficulty == 3:
        print("\nDifficulty set to Hard. Good luck!")
        cap = 100
        break

      elif difficulty == 4:
        print("\nDifficulty set to Expert. Good luck!")
        cap = 1000
        break

      else:
        print("\nError: invalid input. Please enter a number between 1 and 4.")

    except ValueError:
      print("\nError: invalid input. Please enter a number between 1 and 4.")

  # Set the computer number based on difficulty
  computer_number = random.randint(1, cap)

  # Prompt the user for their guess and continue until correct
  while True:

    try:
      
      user_number = int(input(f"\nEnter a number 1 and {cap}: "))

      # Ensure the guess is in range (no negatives and not greater than the cap)
      if user_number > cap or user_number < 1:
        print("\nYour guess is out of range. Try again.")
      else:
        guess_count += 1

        if user_number < computer_number:
          print("Higher!")
        
        elif user_number > computer_number:
          print("Lower!")
        
        else:
          print("\nCorrect!")
          break

    except ValueError:
      print(f"\nError: invalid input. Please enter a number between 1 and {cap}.")

  # Check if guesses should be plural
  if guess_count == 1:
    print(f"It took you {guess_count} guess.")
  else:
    print(f"It took you {guess_count} guesses.")

  # Loop until valid input is received
  while True:

    # Prompt the user if they'd like to play again
    play_again = input("\nWould you like to play again (y/n)? ")

    if play_again.lower() == "n":
      print("Thanks for playing! Goodbye.\n")
      active = False
      break
    
    elif play_again.lower() == "y":
      print("Starting game...")
      break
    
    else:
      print("\nError: invalid input. Please enter y/n.")

# TODO
# Add error handling - program shouldn't end on invalid input
# Enforce integer input (no floats)?