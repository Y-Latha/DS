# Program than takes two integers from user to perform mathematical operation according to the user's choice 
First_Num = int(input("Please enter a number between 1 and 100: "))
Second_Num = int(input("Please enter another number between 1 and 100: "))
print("\n 1> If you want to add the numbers type a \n 2> If you want the difference between the numbers type b \n 3> If you want product of the numbers type c \n 4> If you want to divide first with second number type d \n 5> If you want to get the square of numbers type e ")
User_Choice= input("\n Please enter the letter according to the menu above : ")
if User_Choice == "a":
     print(First_Num + Second_Num )
elif  User_Choice == "b":
     if First_Num > Second_Num:
      print(First_Num - Second_Num )
     else:
      print(Second_Num - First_Num )   
elif User_Choice == "c":
     print(First_Num * Second_Num )
elif User_Choice == "d":
     print(First_Num / Second_Num )    
elif User_Choice == "e":
     print(First_Num ** Second_Num )
else:
    print("An appropriate operator was not selected!")