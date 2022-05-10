logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)

name_and_price = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print("The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
    name = input("What is your name? \n")
    bid_price = int(input("What is your bid price? \n$"))
    name_and_price[name] = bid_price
    other_users = input("Are there other users who want to bid? Type 'Yes' or 'No'\n")
    if other_users == "No":
        bidding_finished = True
        find_highest_bidder(name_and_price)



