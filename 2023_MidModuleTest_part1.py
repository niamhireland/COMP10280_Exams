#TASK
#Write a program that prompts the user for a non-negative number (an integer ≥ 0) and uses a while loop to calculate the 
#number of integers from 0 up to and including that number that are evenly divisible by 3, 13, 23 and 33. The program should 
#print out an error message if a negative number is entered. Sample outputs from this program are as follows (each output 
#represents a separate execution of the program, ie the program prompts for a single number, processes it and exits):

#PSEUDOCODE 

#request user to input a positive int 
#check that the number is greater than 0 
    #initialise j to 0
    #while j is less than/equal to the number
        #for each step, check if number can be divided by 3, 13 or 23 respectively 
        #if so, increment a respective count for each divisor by 1 
    #increment j 
    #print out results 
#else print out that the program requires a positive int to function.

number = int(input('Please enter a number > 0: '))

if number > 0:
    divisible_by_3 = 0
    divisible_by_13 = 0
    divisible_by_23 = 0
    j = 0
    while j <= number: 
        if j % 3 == 0:
            divisible_by_3 +=1
        if j % 13 == 0:
            divisible_by_13 +=1
        if j % 23 == 0:
            divisible_by_23 +=1
        j+=1
    print (f'The number you input is {number}.')
    print (f'Number of numbers from 0 up to and including {number} that are evenly divisible by 3 is {divisible_by_3}.')
    print (f'Number of numbers from 0 up to and including {number} that are evenly divisible by 13 is {divisible_by_13}.')
    print (f'Number of numbers from 0 up to and including {number} that are evenly divisible by 23 is {divisible_by_23}.')

else: 
    print (f'Number you entered was {number}. This program requires a positive integer to run.')