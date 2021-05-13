# Day 9 Project: Secret Auction Program
from art import logo

print(logo)

print("Welcome to the secret action program.")

bidders_dictionary = {}

continue_program = True
while continue_program:

    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))

    bidders_dictionary[name] = bid

    more_bidders = input(
        "Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if more_bidders == "no":
        continue_program = False

highest_bid = 0
highest_bidder = ""
for bidder in bidders_dictionary:
    bid = bidders_dictionary[bidder]
    if bid > highest_bid:
        highest_bid = bid
        highest_bidder = bidder

print(f"The highest bidder is {highest_bidder} with ${highest_bid}")
