# Program Bike value depreciation using function
import datetime

now = datetime.datetime.now().year

def bike_dep(Value,dep_percentage):
     
     global bike_value, now
     
     bike_value = (1-(dep_percentage/100))*bike_value
     now=now +1
     output="In year " + str(now) +" Bike's value is: " + str(bike_value)
     
     return output

bike_value= int(input("What is the value of the bike in "+str(now)+": "))    
dep = int(input("What is the rate of depreciation? "))

while bike_value > 1000:
    print(bike_dep(bike_value,dep))
else:
     print("Bike value is less than 1000 so no more depreciation") 
  
     