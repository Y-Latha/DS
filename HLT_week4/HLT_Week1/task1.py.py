#Program that compares random number to user's guess and prints if the user guessed right
import random
X = random.randint(1,10)
username = input("Enter username: ")
userInt= input("Enter a number between 1 and 10: ")
if userInt==X:
  print("Yes!," + username + " you guessed the number correctly")
else:
  print("Sorry," + username + " you guessed incorrectly the number is "+str(X)) 
