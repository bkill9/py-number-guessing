import random

print("\nWelcome to the Number Guessing Game!")

# Prompt user for difficulty level (Easy 1-10, 
# Medium 1-50, Hard 1-100, Expert 1-1000)
print("\nDifficulty Levels:")
print(" 1. Easy")
print(" 2. Medium")
print(" 3. Hard")
print(" 4. Expert")

difficulty = input("Enter the difficulty level you wish to play on: ")

# Check input and set random numbers
if difficulty == "1":
  print("\nDifficulty set to Easy. Good luck!")
  computer_number = random.randint(1, 10)

elif difficulty == "2":
  print("\nDifficulty set to Medium. Good luck!")
  computer_number = random.randint(1, 50)

elif difficulty == "3":
  print("\nDifficulty set to Hard. Good luck!")
  computer_number = random.randint(1, 100)

elif difficulty == "4":
  print("\nDifficulty set to Expert. Good luck!")
  computer_number = random.randint(1, 1000)

else:
  print("\nError: invalid input. Please enter a number between 1 and 4.")

print(computer_number)