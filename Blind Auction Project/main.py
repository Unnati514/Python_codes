# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be adde
import art
print(art.logo)
def find_highest_bid(bidding_dictionary):
    highest_bid = 0
    winner = ""
      for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

print (f"the winner is {winner} with a bid of ${highest_bid}")

bids={}
continue_bidding = True
while continue_bidding:
    name = input("What is your name?")
    price = int(input("what's your bid?: $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? type 'yes' or 'no'").lower()
    if should_continue == 'no':
       continue_bidding = False
       find_highest_bid(bids)
    elif should_continue == 'yes':
        print("\n"*20)
# TODO-4: Compare bids in dictionary
