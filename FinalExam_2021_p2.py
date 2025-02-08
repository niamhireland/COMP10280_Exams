
import os

def search_file(filename, target_string):
    with open(filename, 'r') as file: #open file in read mode 
        lines = file.readlines() #reads all the files in a list 
        found = False 
        for line in lines: 
            if target_string in line:
                print (line.strip()) #strip takes out trailing whitespace 
                found = True 
        return found

def main(): 
    filename = input('Enter the file for which to search:')
    if filename == "":  #if the filename input is blank 
        filename = 'lines.txt'  #defaults to this 
    if not os.path.exists(filename):
        print (f'{filename} can\'t be found in the computer.') #if it can't find the filename
        return  
    while True: #while there is a filename 
        target_string = ('Enter the string for which to search: ') 
        if target_string == "":
            break #break loop if the input string is blank 
        target_string = target_string.lower() #set string to lowercase 
        found = search_file(filename, target_string) #search_file function searches for matches 
        if not found and len(target_string)>=5: #if it doesn't find a match and the string is 5 or longer 
            for i in range(len(target_string)-1, 4, -1): #i represemts length of prefix 
                partial_string = target_string[:i] #cuts target string down to length of i 
                found = search_file(filename, partial_string) #searches again for matches 
                if found: 
                    break #breaks when a match is found
    print ('Program terminated.')

main()