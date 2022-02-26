# Program to display a joke depending on user's favourite number between 1 and 100

userInt= input("Enter your favourite number between 1 and 100: ")
if int(userInt)<int(30):
    print("My wife told me to stop impersonating a flamingo. I had to put my foot down.")
elif int(userInt)>int(30) and int(userInt)<int(60):
    print("I was wondering why the frisbee kept getting bigger and bigger, but then it hit me.")
elif int(userInt)>int(60):
    print("Don’t you hate it when someone answers their own questions? I do.")
    
    