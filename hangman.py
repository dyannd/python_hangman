# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# # end of helper code

# # -----------------------------------

# # Load the list of words into the variable wordlist
# # so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    #verify if its true    
    match=0
    for guessletter in letters_guessed:
        iteration=0
        for letter in secret_word:
            iteration=iteration+1
            if guessletter==letter :
                match=match+1
                break
            # elif iteration==len(secret_word):
            #     return False
    if match==unique_count(secret_word):
        return True
    else:
        return False

    #unique character count:
def unique_count (secret_word):
    word=[]
    for character in secret_word:
        word.append(character)
    for indices in word:
        appearance=0
        for character in word:
            if indices==character and appearance <=1:
                appearance=appearance+1
                if appearance==2:
                    word.remove(indices)  
    # print(word)
    return len(word)

# print(unique_count('chauvinism'))
def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # Determine which positions should be kept of the secret_word.
    keep_index=[]
    temp_word=[]
    for character in secret_word:
        temp_word.append(character)
    for guessletter in letters_guessed:
        for index in range(len(temp_word)): 
            if guessletter == temp_word[index]:
                keep_index.append(index)
    ans=[]
    for letters in secret_word:
       ans.append(letters)
       
    for index in range(len(ans)):
        # print(index)
        if index not in keep_index:
            ans[index]='_'
    return (' '.join(str(x) for x in ans))
        


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    alphabet='abcdefghijklmnopqrstuvwxyz'
    for guessletter in letters_guessed:
        if guessletter in alphabet:
            alphabet=alphabet.replace(str(guessletter),'' )
    
    return(alphabet)


def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    print('-----------------------')
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is '+ str(len(secret_word))+' letters long')
    # print('-------------------------')
    #Game begin with number of guesses = 6 and 3 warnings.
    guess_num=6
    warning=3
    alphabet='abcdefghijklmnopqrstuvwxyz'
    # print('You have '+str(guess_num+1)+' guesses left.')
    # print('Availabe letters: '+alphabet)
    
    # print(secret_word)
    # while str(user_input) not in alphabet or len(str(user_input))>1:
    #     user_input=str(input('Enter a letter again (only 1): '))
    #     warning=warning-1
    # user_input_array=[]
    # user_input_array.append(str(user_input))
    # print(user_input_array)
    
    #while the word is not guessed, keep repeating the game
    user_input_array=[]
    while is_word_guessed(secret_word,user_input_array) == False:
        #begin guess
        print('------------------------')
        print('You have '+str(warning)+' warnings left.')
        print('You have '+str(guess_num)+' guesses left.')
        print('Available letters: '+str(get_available_letters(user_input_array)))
        user_input=input('Please guess a letter: ')

        #Check for correct form of input
        while str(user_input) not in alphabet or len(str(user_input))>1:
            warning=warning-1
            if warning >0:
                print('You have '+str(warning)+' warnings left.')
                user_input=str(input('Enter a letter again (only 1): '))
            else:
                print('You broke the rules!')
        #if the user guess it wrong:s
        if user_input not in secret_word and guess_num>1 and user_input not in user_input_array:
            guess_num=guess_num-1
            print('Letter is not in word')
        #if the user ans a completely new matched letter
        elif user_input in secret_word and user_input not in user_input_array:
            print('Good guess!')
        #if the user types in the letter already guessed:
        elif user_input in user_input_array:
            print('Already guessed!')
        else: 
            print('-----------------------------')
            print('You lost! The word is '+secret_word)
            guess_num=0
            break
        #add the entry into the input array
        if user_input not in user_input_array:
            user_input_array.append(str(user_input))
        #call the guess_word function to deploy the interface
        guessed_word=get_guessed_word(secret_word,user_input_array)
        print(guessed_word)
        # print(user_input_array)
#print correct after breaking the game loop (guessing is True)
    if guess_num !=0:
        print('Correct! The word is '+secret_word)
        print('Your total points are: '+str((guess_num)*unique_count(secret_word)))
        
# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------
# secret_word='mosieuthua'
secret_word=str(choose_word(wordlist))  
game=hangman(secret_word)

def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


# if __name__ == "__main__":
#     # pass

#     # To test part 2, comment out the pass line above and
#     # uncomment the following two lines.
    
#     secret_word = choose_word(wordlist)
#     hangman(secret_word)

# ###############
    
#     # To test part 3 re-comment out the above lines and 
#     # uncomment the following two lines. 
    
#     #secret_word = choose_word(wordlist)
#     #hangman_with_hints(secret_word)
