#player_actions.py

#this will make the user input actually usable when responding at the bottom.
def check_play_again(user_input):
    #Your code here
#this "if" and "elif" will lwt you respond with "y" or "n" if you want to play the game.
#the else will give say "incorrect"if given a different response.   
    if user_input == "y":
        print ("Play Again!")
    elif user_input == "n":
        print("Quit Game")
    else:
        print ("Incorrect!")
#this input will ask you if you want to play again with the possible reponses.
check_play_again(input("Would you like to play again? Type Y for Yes or N for No: \n"))
