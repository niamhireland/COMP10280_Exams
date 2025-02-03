#TASK

#The 2023–2024 academic year for a particular Australian university runs from 1 March 2023 to the end of February the 
#following year. Write a program that prompts the user for a series of days (integer numbers) and, for each day, prints 
#out the date, the monthand the year in the 2023–2024 academic year of that day. The program should continue
#until a non-positive number is entered.

#PSEUDOCODE 

#ask user to input a number 
#set functions to identify the date, year and date, using if statements 
#while the user input is greater than 0 and less than 366: 
    #print out results 
    #ask for repeat input 

#else terminate the program 

def year(date):
    if date <= 306: 
        year = 2023 
    else: 
        year = 2024
    return year 

def month(date):
    if date <= 31: 
        month = 'March' 
    elif date > 31 and date <= 61: 
        month = 'April' 
    elif date > 61 and date <= 92:
        month = 'May'
    elif date > 92 and date <= 122: 
        month = 'June'
    elif date > 122 and date <= 153: 
        month = 'July' 
    elif date > 153 and date <= 184: 
        month = 'August'
    elif date > 184 and date <= 214: 
        month = 'September'
    elif date > 214 and date <= 245: 
        month = 'October'
    elif date > 245 and date <= 275: 
        month = 'November' 
    elif date > 275 and date <= 306:
        month = 'December' 
    elif date > 306 and date <= 337: 
        month = 'January' 
    elif date > 337 and date <= 366:
        month = 'February' 
    return month 

def day(date):
    if date <= 31: #March 
        day = date  
    elif date > 31 and date <= 61: #April 
        day = date - 31
    elif date > 61 and date <= 92: #May 
        day = date - 61
    elif date > 92 and date <= 122: #June 
        day = date - 92
    elif date > 122 and date <= 153: #July 
        day = date - 122
    elif date > 153 and date <= 184: #August
        day = date - 153
    elif date > 184 and date <= 214: #Sept
        day = date - 184
    elif date > 214 and date <= 245: #Oct 
        day = date - 214
    elif date > 245 and date <= 275: #Nov 
        day = date - 245
    elif date > 275 and date <= 306: #Dec
        day = date - 275
    elif date > 306 and date <= 337: #Jan 
        day = date - 306
    elif date > 337 and date <= 366: #Feb 
        day = date - 337
    return day 

print ('Program to calculate the date, month and year in the academic year 2022-2023 of a given day.')
date = int(input('Enter the day for which you want to find the date (an integer): '))

while date > 0 and date <= 366:
    print (f'You entered {date}.')
    print (f'This is day {day(date)} in {month(date)} {year(date)}')
    print ()
    date = int(input('Enter the day for which you want to find the date (an integer): '))

else: 
    if date <= 0:
        print ('You entered a non-positive integer and the program terminated.')
        print ('Finished!')
    elif date < 366: 
        print (f'You entered {date}, which is outside of the academic calendar.')
        print ('Restart if you wish to continue.')