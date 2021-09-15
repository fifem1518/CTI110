# CTI 110
# P1T2 - Salary Calculator
# Fife Marshall
# 9/15/21

# Start

# Input thte hours worked
hoursWorked = input("How many hours did you work this week?")
hoursWorked = float(hoursWorked) # convert to intger

# Input the hourly pay rate
hourlyPay = float(input("What's your hourly pay rate?")) # get and convert

# Calulate gross pay (hours worked times pay rate)
grossPay = hoursWorked * hourlyPay

# Display the gross pay
print ("Your gross pay for the week is: $", grossPay)

# End

"""

userNum = int(input())
userNumSquared = userNum + userNum   # Bug here; fix it when instructed
   
print(userNumSquared, end=' ')       # Output formatting issue here; fix it when instructed
