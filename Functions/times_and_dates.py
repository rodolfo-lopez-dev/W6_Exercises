# Author: Rodolfo 
# Date: October 30
# Script shows the usage of datetime 

import datetime

# finding today's datetime

today = datetime.datetime.now()
print("Today is", today.strftime("%A, %B %d, %Y"))

# define my birthday
my_birthday = datetime.date(1999, 11, 25)
print ("My birthday is:", my_birthday.strftime("%m/%d/%Y"))

# define 90 days from today 
ninety_d = today + datetime.timedelta(days=90)
print("90 days from today is:", ninety_d.strftime("%B %d, %Y"))

# bonus for me
#from datetime import datetime
#today = datetime.now()
#jan_1 = datetime(today.year + 1, 1, 1)
#days_left = (jan_1 - today).days
#print("You got this many days left for your grind:", days_left)
# 62 days left

# finding out when dinner time is 
dinner_time = datetime.time(18,00)
print("Be ready for dinner at:", dinner_time.strftime("%I:%M %p"))
