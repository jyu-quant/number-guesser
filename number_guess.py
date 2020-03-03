""" number guessing game where an integer from 1-100 is randomly generated """
import numpy as np
np.random.seed()

def main(): #initializes program
    print('This is a number guessing game')
    print('A random integer from 1 to 100 has been generated')
    print('Guess the number')
    rand_num = np.random.randint(1,101) #generates a random integer
    found = False                       #from 1 to 100
    while not found:
        guess = eval(input('Your guess: '))
        if guess == rand_num:
            print('You got it!')
            found = True
        elif guess < rand_num:
            print('Guess higher.')
        else:
            print('Guess lower.')
        
    
if __name__ == '__main__':
    main()
