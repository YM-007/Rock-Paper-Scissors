import random
import math

def play():
    user = input("Let's Play. What's your choice from these options? 'R' for rock, 'P' for paper, and 'S' for scissors.\n")

    computer = random.choice(['R', 'P', 'S'])

    if user == computer:
        return (0, user, computer)

    # R > S, S > P, P > R
    if is_win(user, computer):
        return (1, user, computer)

    return (-1, user, computer)

def is_win(player, opponent):
    # return true is the player beats the opponent
    # winning conditions: R > S, S > P, P > R
    if (player == 'R' and opponent == 'S') or (player == 'S' and opponent == 'P') or (player == 'P' and opponent == 'R'):
        return True
    return False

def play_best_of(n):
    # play against the computer until someone wins best of n games
    # to win, you must win ceil(n/2)
    player_wins = 0
    computer_wins = 0
    wins_necessary = math.ceil(n/2)
    while player_wins < wins_necessary and computer_wins < wins_necessary:
        result, user, computer = play()
        # wrong option or error
        if user not in ['R', 'P', 'S']:
            print('Error! Invalid option, select again. Remember, only select from options provided, and options are case sensitive:)')
        # tie
        elif result == 0:
            print('It is a tie. You and the computer both chose {}. \n'.format(user))
        # you win
        elif result == 1:
            player_wins += 1
            print('You chose {} and the computer chose {}. You won! :)\n'.format(user, computer))
        else:
            computer_wins += 1
            print('You chose {} and the computer chose {}. You lost :(\n'.format(user, computer))

    if player_wins > computer_wins:
        print('You have won the best of {} Games! Bravo!'.format(n))
    else:
        print('Sorry, the computer has won the best of {} games. Good luck next time.'.format(n))


if __name__ == '__main__':
    play_best_of(3)



