# Program to display a joke depending on user's favourite number between 1 and 100, using List

userInt= input("Enter your favourite number between 1 and 100: ")
    
Jokes = ("My wife told me to stop impersonating a flamingo. I had to put my foot down.", "I was wondering why the frisbee kept getting bigger and bigger, but then it hit me.", "Don’t you hate it when someone answers their own questions? I do.")

(first, second,third) = Jokes
if int(userInt)<int(30):
 print(first)
elif int(userInt)>int(30) and int(userInt)<int(60):
 print(second)
elif int(userInt)>int(60):
 print(third)