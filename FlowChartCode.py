# Flow chart cade for pizza order
print("Welcome! Lets start your Pizza order.")
topping = input("Do you want any toppings? Y/N : " )
drink = input("Do you want a drink? Y/N : " )
if topping== "Y" and drink=="Y":
 print("\nPizza     £9.99\nToppings  £0.99 \nDrink     £0.99\n\nTotal     £11.97\n") 
elif   topping== "N" and drink=="Y":
 print("\n Pizza    £9.99\n Drink    £0.99\n\n Total    £10.98\n ") 
elif   topping== "Y" and drink=="N":
 print("\n Pizza    £9.99\n Toppings £0.99\n\n Total    £10.98\n ")   
elif   topping== "N" and drink=="N":
  print("\nPizza    £9.99\n\nTotal    £9.99\n ")
else:
 print("Please type in capital Y or Capital N as answer")       