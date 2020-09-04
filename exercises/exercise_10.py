# Rock, Paper, Scissor Game
import random

def generate_random_int(minimum_value: int, maximum_value: int) -> int:
    return random.randint(minimum_value, maximum_value)

def get_move(move: int) -> str:
    if move == 0:
        move = "Rock"
    elif move == 1:
        move = "Paper"
    elif move == 2:
        move = "Scissor"
    return move

def decide_game(user_move: int, computer_move: int) -> int:
    if 0 <= user_move <= 2:
        if (
                (user_move == 0 and computer_move == 0)
            or  (user_move == 1 and computer_move == 1)
            or  (user_move == 2 and computer_move == 2)
            ):
            return -1
            
        elif (
                (user_move == 0 and computer_move == 1)
            or  (user_move == 1 and computer_move == 2)
            or  (user_move == 2 and computer_move == 0)
            ):
            return 0

        elif (
                (user_move == 0 and computer_move == 2)
            or  (user_move == 1 and computer_move == 0)
            or  (user_move ==2 and computer_move == 1)
            ):
            return 1
    else:
        return -2

def main():
    while True:
        print("Rock", "Paper", "Scissors")
        print("[0] Rock\n[1] Paper\n[2] Scissors")
        user_move = int(input("Enter your move: "))
        computer_move = generate_random_int(0,2)
        user_move_marker = get_move(user_move)
        computer_move_marker = get_move(computer_move)
        game_outcome = decide_game(user_move=user_move, computer_move=computer_move)
        if game_outcome == -1:
            print("It's a tie")
            break
        elif game_outcome == 0:
            print(f"The computer won!\nComputer: {computer_move_marker}\tYou: {user_move_marker}")
            break
        elif game_outcome == 1:
            print(f"You won!\nComputer: {computer_move_marker}\tYou: {user_move_marker}")
            break
        elif game_outcome == -2:
            print("Enter 0-2 only")
    
main()