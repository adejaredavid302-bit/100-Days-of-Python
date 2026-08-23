from art import logo
print(logo)
bids={}
game_over=False
def find_highest_bidder(secret_auction):
    winner = ""
    highest_bidder = 0
    for bidder in secret_auction:
        bid = secret_auction[bidder]
        if bid > highest_bidder:
            highest_bidder = bid
            winner = bidder
    print(f"The winner is {winner} with the bid of ${highest_bidder}")
while not game_over:
    user_name = input("What is your name:\n").lower()
    user_bid = int(input("What is your bid: "))
    bids[user_name] =user_bid
    other_bidder=input("Are there any other bidders? type 'yes' or 'no': ")
    if other_bidder=='yes':
        print("\n" * 20)
    else:
        game_over=True
        find_highest_bidder(bids)





