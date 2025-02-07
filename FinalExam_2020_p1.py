#A palindrome is a string that reads the same backwards as it does forwards. For the purposes of this exercise, letters and 
#spaces are considered, but all other characters are ignored. Thus “abba”,“A-9*A” and “A2 3b4b3 2A” are palindromes according
#to this definition, but “Abca”, “a bc98cba” and “Madam, I’m Adam” are not. Write a program in Python 3 that prompts the user
#for a series of strings and checks whether each one is a palindrome according to the above definition. The program should
#continue until an empty string is entered. Your program should include a recursive
#function that checks whether a given string is a palindrome.

def isPalindrome(string):
    '''function evaluates whether a given string is a palindrome or not'''
    def isChars(string):
        '''returning a letterstring of all characters to be considered for the palindrome'''
        letterstring = ""
        specialchars = "0123456789 "
        for s in string: 
            if s.isalpha() or s in specialchars:
                letterstring += s
        return letterstring

    def isPal(letterstring):
        '''evaluating whether previous function's letterstring is a palindrome, recursively'''
        if len(letterstring) <= 1: 
            return True 
        else: 
            return letterstring[0] == letterstring[-1] and isPal(letterstring[1:-1])
    return isPal(isChars(string))

string = input('Enter a string (empty string to exit): ')

while string != '':
    if isPalindrome(string): 
        print (f'{string} is a palindrome.')
        string = input('Enter a string (empty string to exit): ')
else: 
    print (f'{string} is not a palindrome.')
    string = input('Enter a string (empty string to exit): ')

print ('You pressed Enter and the program has terminated.')
print ('Restart if you wish to continue.')