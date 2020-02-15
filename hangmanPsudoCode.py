'''
Created on Feb 15, 2020

@author: ITAUser
'''
#import the random library

#define a function called pick_random word(words.txt):
    #open and read word dictionary/list 
    
    #variable called index = select random word from words.txt
    #variable called word = strip the randomly selected word
    #return variable 'word'

#define a function called ask_for_next_letter(): 
    #variable called letter = input function that asks user to select a letter
    #return the letter selected

#define a function called generate_word_string(word, letters_guessed):
    #variable called output = empty list
    #make a for loop that goes through letter in the variable 'word':
        #if statement that checks if letter is in letters_guessed:
            #append letter to output
    #else:
        #append ("_")
    #return output
    
#create a main module:
    #variable called WORD = pick_random_word()
    
    #variable called letters_to_guess = set of WORD
    #variable called correct_letters_guessed = empty set
    #variable called incorect_letter_guessed = empty set
    #variable called numberof_guess = number of guess you want user to have
    
    #print statement that welcomes user to hangman
    
    #while loop that runs until number_of_guesses is less than 1 or letters_to_guess is greater than 0
        #variable called guess = ask_for_next_letter() and turn into lower case
        
    #if statement that checks if guess is in correct_letters_guessed or guess in incorrect_letters_guessed:
        #print statement that says you already guessed that letter
    
    #if statement that checks if guess is in letters_to_guess:
        #remove guess from letters_to_guess
        #add guess to correct_letters_guessed
    #else:
        #add guess to incorecct_letters_guessed
        #number_of_guesses goes down by one
        
#variable called word_string = generate_word_string(WORD, correct_letters_guessed)
#print statement that prints word string 
#print statement that prints how many guesses you have left

#if statement to check if numbers of guesses is greater than value:
    #print congratulation you guessed the word