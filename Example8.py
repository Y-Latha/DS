#Then write a loop program that ask the user for an integer number and check if it is < 10. If it is < 10 then it keeps adding 1 to the value.

User_Num = int(input("Please enter an interger : "))
   
if User_Num < 10:
       
   while User_Num < 10:
     User_Num += 1
     print(User_Num)
       
else:
     print(" Number is greater than 10")
    