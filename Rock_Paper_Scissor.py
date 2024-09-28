import random

def get_ai_choice():
    choice = ["rock", "paper", "scissor"]
    return random.choice(choice)

def get_user_choice():
    user_choice = input("choose rock, paper, scissor:").lower()
    while user_choice not in ["rock", "paper","scissor"]:
        print("invalid choice. please retry")
        user_choice = input("choose rock, paper, scissor: ").lower()
    return user_choice

def get_winner(user_choice, cmp_choice):
    if user_choice == cmp_choice:
        return "tie"
    
    elif user_choice == "rock" and cmp_choice == "scissor":
        return "Rock"
    
    elif user_choice == "rock" and cmp_choice == "paper":
        return "Rock"
    
    elif user_choice == "scissor" and cmp_choice == "paper":
        return "Scissor"
    
    elif user_choice == "scissor" and cmp_choice == "rock":
        return "Rock"
    
    elif user_choice == "paper" and cmp_choice == "rock":
        return "Rock"
    
    elif user_choice == "paper" and cmp_choice == "scissor":
        return "Scissor"
    
def main():
    user_choice = get_user_choice()
    cmp_choice = get_ai_choice()
    print(f"user choice {user_choice}")
    print(f"Cmp chose: {cmp_choice}")
    print(get_winner(user_choice, cmp_choice))

main()