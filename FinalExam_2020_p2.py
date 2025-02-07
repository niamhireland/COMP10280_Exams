#PSEUDOCODE 

#function count vowels: 
    #create a list of all vowels 
    #iterate through each character of each line, add to the sum if a character is in the vowel list 

#function count consonants: 
    #create a list of all consonants 
    #define list of all consonants 
    #iterate through each character of each line, add to sum if a character is in the consonant list 

#function count words: 
    #use split to split the line wherever it encounters whitespace 
    #after split, use len to determine number of words in the list. return same. 

#main function: 
    #request user input of a file to analyse 
    #if file is blank, print termination message and break 
    #else open the textfile in read mode: 
        #initialise max vowels, words and consonants, line number counts for all (all to 0)
        #print out all counts at end of iteration

def count_vowels (line):
    '''counts all vowels on each line of the file '''
    vowels = "AEIOUaeiou"
    return sum(1 for char in line if char in vowels)

def count_consonants (line):
    '''counts all consonants on each line of the file'''
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    return sum(1 for char in line if char in consonants)

def count_words(line):
    '''counts all words on each line of the file'''
    words = line.split()
    return len(words)

def main(): 
    """Function to open a file, use subfunctions to count vowels/consonants and print out result"""
    while True:
        filename = input('Enter the file for which to search (empty string to terminate): ')
        if filename == "":
            print ('You entered Enter and the program will now terminate.')
            print ('Restart if you wish to continue.')
            break 
        try: 
            with open(filename, 'r') as file: 
                max_vowels = 0
                max_consonants = 0
                max_words = 0
                line_number_vowels = 0
                line_number_consonants = 0
                line_number_words = 0
                for current_line, line in enumerate(file, 1):
                    num_vowels = count_vowels(line)
                    num_consonants = count_consonants(line)
                    num_words = count_words(line)
                    if num_vowels > max_vowels: 
                        max_vowels = num_vowels
                        line_number_vowels = current_line
                    if num_consonants > max_consonants: 
                        max_consonants = num_consonants
                        line_number_consonants = current_line
                    if num_words > max_words: 
                        max_words = num_words
                        line_number_words = current_line
                file.seek(0)
                content = file.read()
                total_vowels = count_vowels(content)
                total_consonants = count_consonants(content)
                total_words = count_words(content)
                print (f'Total vowels in the text: {total_vowels}')
                print (f'Line with the most vowels is {line_number_vowels}. The vowel count on it is {max_vowels}')
                print ()

                print (f'Total consonants in the text: {total_consonants}')
                print (f'Line with the most consonants is {line_number_consonants}. The consonant count on it is {max_consonants}')
                print ()

                print (f'Total words in the text: {total_words}.')
                print (f'Line with the most words is {line_number_words}. The consonant count on it is {max_words}')
                print ()
        except FileNotFoundError: 
            print (f'File {filename} not found. Please restart if you wish to continue.')
    
main ()