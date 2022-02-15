# Display Bike value depreciation by 10% for every year until it reaches 1000
import datetime
bike_value = 2000
now = datetime.datetime.now().year
while bike_value > 1000:
  print("In year " + str(now) +" Bike's value is: " + str(bike_value))
  now=now +1
  bike_value=0.9*bike_value
  if bike_value < 1000:
   break