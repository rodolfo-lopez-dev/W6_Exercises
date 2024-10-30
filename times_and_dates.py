# Author: Rodolfo 
# Date: October 30
# Script shows the usage of datetime 

import datetime

# finding today's datetime

today = datetime.datetime.now()
print("Today is", today.strftime("%A, %B %d, %Y"))

# define my birthday