import random


def easy_level():
    print('Welcome to the Easy Level\n'
          'Guess a number between 1 - 10\n'
          'You have maximum of 6 trials\n'
          )
    
    secret_number = random.randint(1,10)
    guess_count = 0
    guess_limit = 6

    while guess_count < guess_limit:
        while True:
            try:
                guess = int(input('Guess number: '))
                guess_count += 1
                limit = guess_limit - guess_count
                print(f'(You have {limit} guesses left)')
            except:
                print('Whoops! Be sure the number contain only digits(integers)')
                continue
            break

        if guess == secret_number:
            print('You got it right')
            break
        elif guess != secret_number:
            print('That was wrong')

    else:
        print('Game Over!')

def medium_level():
    print('Welcome to the Medium Level\n'
          'Guess a number between 1 - 20\n'
          'You have maximum of 4 trials\n'
          )
    number = random.randint(1,20)
    count = 0
    limit = 4

    while count < limit:
        while True:
            try:
                guess = int(input('Guess number: '))
                count += 1
                guess_limit = limit - count
                print(f'You have {guess_limit} guesses lefts')
            except:
                print('Whoops! Be sure the number contains only digits(integers)')
                continue
            break

        if guess == number:
            print('You got it right!')
            break
        elif guess != number:
            print('That was wrong!')

    else:
        print('Game Over!')
              
def hard_level():
    print('Welcome to the Hard Level\n'
          'Guess a number between 1 - 50\n'
          'You have a maximum of 3 trials\n'
          )
    answer = random.randint(1,50)
    count_number = 0
    count_limit = 3

    while count_number < count_limit:
        while True:
            try:
                guess = int(input('Guess number: '))
                count_number += 1
                limit = count_limit - count_number
                print(f'(You have {limit} guesses left)')
            except:
                print('Whoops! Be sure the number contains only digits(integers)')
                continue
            break

        if guess == answer:
            print('You got it right!')
            break
        elif guess != answer:
            print('That was wrong!')
    else:
        print('Game Over!')

def start_game():
    print('Welcome to Number Guessing Game')
    action = input('Select game level; Easy, Medium or Hard: ')

    if action.upper() == 'EASY':
        easy_level()
                   
    elif action.upper() == 'MEDIUM':
        medium_level()
           
    elif action.upper() == 'HARD':
        hard_level()
        

start_game()

