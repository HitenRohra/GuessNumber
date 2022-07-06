import random as rd

def guess(x):
    random_number= rd.randint(1,x)
    guess=0
    while guess != random_number:
        guess= int(input(f"Guess a number between 1 and {x}: "))
        if guess<random_number:
            print("Sorry, guess again. Too Low. ")
        elif guess>random_number:
            print("Sorry, guess again. Too High. ")
    print(f"Congratulations! You have guessed the number {random_number} correctly!! ")

def computer_guess(x):
    low=1
    high=x
    feedback=''
    while feedback != 'c':
        if low!=high:
            guess= rd.randint(low,high)
        else:
            guess=low  #you can declare it as high too // high = low
        feedback=input(f'Is {guess} too high (h) or too low (l), or correct (c)?: ').lower()
        if feedback=='h':
            high=guess-1
        elif feedback=='l':
            low=guess+1
    print(f"Congratulations! Computer has guessed your number {guess} correctly!! ")

x=int(input('Please enter the highest number for computer to guess from: '))
computer_guess(x)
y=rd.randint(1,50)
print(f"Computer has chosen the highest number. It is {y}")
guess(y)