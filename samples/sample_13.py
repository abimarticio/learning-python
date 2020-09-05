import random

def generate_random_int(minimum_value: int, maximum_value: int) -> int:
    return random.randint(minimum_value, maximum_value)
def main():
    names = ["Adam", "Ben", "Carl", "Dave", "Eva", "Fatima", "George", "Heather",
            "Ivan", "Jack", "Kath", "Lando"]

    random_number = generate_random_int(0, len(names)-1)
    print(f"The winner is {names[random_number]}")
    print(names)
    random.shuffle(names)
    print(names)
    print("=" * 110)
    print("Rock", "Paper", "Scissor")
    print("[0] Rock\n[1] Papers\n[2] Scissor")
    user_move = int(input("Enter your move: "))
    computer_move = random.randint(0,2)


    if user_move == 0:
        user = "Rock"
    elif user_move == 1:
        user = "Paper"
    elif user_move == 2:
        user = "Scissor"
    if computer_move ==0:
        computer = "Rock"
    elif computer_move == 1:
        computer = "Paper"
    elif computer_move == 2:
        computer = "Scissor"

    if 0 <= user_move <= 2:
        if ((user_move == 0 and computer_move == 0)
        or (user_move == 1 and computer_move == 1)
        or (user_move == 2 and computer_move == 2)
        ):
            print(f"It's a tie")
        elif(
            (user_move == 0 and computer_move == 1)
            or (user_move == 1 and computer_move == 2)
            or (user_move == 2 and computer_move == 0)
        ):
            print(f"The computer won!\nComputer: {computer}\tYou: {user}")
        elif (
            (user_move == 0 and computer_move == 2)
            or (user_move == 1 and computer_move == 0)
            or (user_move ==2 and computer_move == 1)
        ):
            print(f"You won!\nComputer: {computer}\tYou: {user}")
    else:
        print("Enter 0-2 only")
main()