import random
def deal_card():
    # Return a random card.
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    card=random.choice(cards)
    return card

def calculate_score(cards):
    """ calculate score of cards """
    if sum(cards)==21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    score=sum(cards)
    return score
def compare(user_comparison,computer_comparison):
    if user_comparison==computer_comparison:
        return "DRAW"
    elif computer_comparison==0:
        return "YOU LOSE!!,Opponent has Blackjack"
    elif user_comparison==0:
        return "YOU WIN!! with a Blackjack"
    elif computer_comparison>21:
        return "YOU WIN,COMPUTER WENT OVER"
    elif user_comparison>21:
        return "YOU LOSE,OPPONENT WENT OVER"
    elif user_comparison>computer_comparison:
        return "YOU WIN"
    else:
        return "YOU LOSE"


def play_again():
    from art import logo
    print(logo)
    user_card = []
    computer_card = []
    computer_score = -1
    user_score = -1
    game_over = False
    for _ in range(2):
        user_card.append(deal_card())
        computer_card.append(deal_card())
    while not game_over:
        user_score=calculate_score(user_card)
        computer_score=calculate_score(computer_card)
        print(f"Your cards: {user_card},current score: {user_score}")
        print(f"Computer first cards: {computer_card[0]}")
        if user_score==0 or computer_score==0 or user_score>21:
             game_over=True
        else:
            draw_card=input("Type 'yes' to get another card,type 'no' pass.").lower()
            if draw_card=="yes":
                user_card.append(deal_card())
            else:
                game_over=True
    while computer_score !=0 and computer_score<17:
        computer_card.append(deal_card())
        computer_score=calculate_score(computer_card)
    print(f"Your final hands: {user_card},final score: {user_score}")
    print(f"Computer final hands: {computer_card},final score: {computer_score}")
    print(compare(user_score,computer_score))

while input(f"Do you want to play again?(yes/no)") =="yes":
    print("\n"*20)
    play_again()