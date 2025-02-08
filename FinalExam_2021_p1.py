#A palindrome is a string that reads the same backwards as it does forwards. For the purposes of this exercise, letters, 
#numeric digits (0–9), the underscore ( ) character and spaces are considered, but all other characters are ignored. Also, 
#the case (upper-case/lowercase) of letters is to be considered. Thus “abba”,“A-9*A” and “A2 3b4b3 2A” are palindromes 
#according to this definition, but “Abba”, “abc9 cba” and “Madam, I’m Adam” are not. Write a program in Python 3 that 
#prompts the user for a series of strings and checks whether each one is a palindrome according to the above definition. 
#The program should continue until an empty string is entered. Your program should include a non-recursive function that 
#checks whether a given string is a palindrome.

#PSEUDOCODE 

#take a user input of a string 
#while the string is not empty:
    #call function isPalindrome 
        #within the function, first use function isChars to define what are and are not usable characters and return a letterstring
        #then use a separate function to evaluate whether it is a palindrome 
            #set each end of the string to be 'left' and 'right'
            #if left and right don't match, return False 
            #else increment left, decrement right and check again
    #print result of function and request repeat user input 

def isPalindrome(string):
    """Function for evaluating whether a string is a palindrome."""
    def isChars(string):
        '''Function to define what is an acceptable character to be considered in the string.'''
        letterstring = ""
        specialchars = "0123456789() "
        for s in string: 
            if s.isalpha() or s in specialchars:
                letterstring += s
        return letterstring
    
    def isPal(letterstring):
        ''''evaluate whether the generated letterstring is a palindrome'''
        left, right = 0, len(letterstring) - 1
        while left < right: 
            if letterstring[left] != letterstring[right]:
                return False 
            left +=1 
            right -= 1 
        return True 
    return isPal(isChars(string))

string = input ('Enter a string (empty string to exit): ')

while string != "":
    if isPalindrome (string):
        print (f'{string} is a palindrome.')
    else: 
        print (f'{string} is not a palindrome.')
    string = input ('Enter a string (empty string to exit): ')

print ('You entered an empty string and the program terminated.')