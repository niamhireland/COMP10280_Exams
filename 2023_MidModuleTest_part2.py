#TASK

#The 2023–2024 academic year for a particular Australian university runs from 1 March 2023 to the end of February the 
#following year. Write a program that prompts the user for a series of days (integer numbers) and, for each day, prints 
#out the date, the monthand the year in the 2023–2024 academic year of that day. The program should continue
#until a non-positive number is entered.


def main():
    month_days = {
        "March": 31,
        "April": 30,
        "May": 31,
        "June": 30,
        "July": 31,
        "August": 31,
        "September": 30,
        "October": 31,
        "November": 30,
        "December": 31,
        "January": 31,
        "February": 29
    }

    months = list(month_days.keys())
    
    print("Program to calculate the date, month and year in the academic year 2023-2024 of a given day.")
    
    while True:
        day_number = int(input("Enter the day for which you want to find the date (an integer): "))
        if day_number <= 0:
            print("Finished!")
            break
        
        print(f"You entered: {day_number}")

        if day_number < 1 or day_number > 366:
            print(f"Day number {day_number} is not in the academic year 2023-2024!")
            continue

        day_of_year = day_number
        for month in months:
            if day_of_year <= month_days[month]:
                print(f"Day number {day_number} is {day_of_year} {month} 2023")
                break
            else:
                day_of_year -= month_days[month]  
        
if __name__ == "__main__":
    main()
