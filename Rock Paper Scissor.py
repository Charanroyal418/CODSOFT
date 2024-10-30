import random
user_wins=0
computer_wins=0
options=("Rock","Paper","Scissors")
game =True
while game:
    computer = random.choice(options)
    while True:
        user_input=input("ENTER YOUR CHOICE:").lower()
        if user_input == "rock":
            user_choice=options[0]
        elif user_input == "paper":
            user_choice=options[1]
        elif user_input == "scissors":
            user_choice=options[2]
        else:
            user_choice=None
        if user_choice:
            print("PLAYER CHOICE:", user_choice)
            break
        else:
            print("INVALID CHOICE")
    print("COMPUER CHOICE:",computer)

    if user_input == computer:
        print("IT IS A TIE")
        user_wins+=1
        computer_wins+=1
    elif user_input=="ROCK" and computer=="SCISSORS":
        print("YOU WIN!!")
        user_wins+=1
    elif user_input=="SCISSORS" and computer=="PAPER":
        print("YOU WIN!!")
        user_wins+=1
    elif user_input=="PAPER" and computer=="ROCK":
        print("YOU WIN!!")
        user_wins+=1
    else:
        print("YOU LOSE!")
        computer_wins+=1
    print("user points",user_wins)
    print("computer points",computer_wins)
    while True:
        play_again = input("Play again? (Y/N):").strip().lower()
        if play_again in ['y', 'n']:
            play_again == "y"
            break
        else:
            print("ENTER VALID INPUT (Y/N):")
    if not play_again == "y":
        game = False
print("THANKS FOR PLAYING!!")