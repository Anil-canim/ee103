#i use import to bring in the secret number and hint tipy files.
#it just easy to carry them in another file when working on multiple files.
from secret_number_library import secret_number
from secret_number_library import hint
while True:
    secret_number=int(secret_number)
    #we need to define this as int because the imported value is str

    print(hint)
    #we need to help to user to guess the number
    guess=input("Enter your guess: ")

    #so now we need to loop until the user guesses correctly
    while int(guess)!=secret_number:
        if int(guess)<secret_number:
            print("Too low.")
        elif int(guess)>secret_number:
            print("Too high.")
        print("Wrong guess. Try again.")
        guess=input("Enter your guess: ")

    #right now, we are out of the loop, so the user guessed correctly    
    print("Congratulations! You guessed the secret number.")
    print("if you want to play again, press y, otherwise press any key to exit.")
    play_again=input()
    if play_again.lower()=="y":
        continue