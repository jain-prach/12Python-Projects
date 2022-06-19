import random
def play():
    user=input("choose 'r' for rock, 'p' for paper or 's' for scissors: ")
    computer=random.choice(['r', 'p', 's'])
    print(f'The computer chose: {computer}')
    if user==computer:
        return "It's a tie"
    if is_win(user, computer):
        return "You won"
    
    return "you lost"

def is_win(player, opponent):
    #true if player wins
    #p>r s>p r>s
    if (player=='p' and opponent=='r') or (player=='s' and opponent=='p') or (player=='r' and opponent=='s'): 
        return True
    
print(play())