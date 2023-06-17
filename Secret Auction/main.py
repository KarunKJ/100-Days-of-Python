from art import logo
import os
clear = lambda: os.system('clear')
clear()

print(logo)
print("Welcome to Secret Auction program")

auction_list = []

def name_bid():
    bidder_name = input("What is your name? ")
    bid_amount = input("What is your bid? ")
    
    bid_details = {}
    
    bid_details["name"] = bidder_name
    bid_details["amount"] = bid_amount
    auction_list.append(bid_details)

def max_bid(list):
    maximum_bid = list[0]["amount"]
    name = list[0]["name"]
    for i in range(0,len(list)):
        if maximum_bid < list[i]["amount"]:
            maximum_bid = list[i]["amount"]
            name = list[i]["name"]
    print(f"{name} has won the Secret Auction with a bid of {maximum_bid}")

bidding = True
while bidding:
    name_bid()
    continue_bid = input("Are there any more bidders? type yes or no: ")
    while continue_bid == 'yes':
        #then ask name and bid again whilst clearing screen
        clear = lambda: os.system('clear')
        clear()
        name_bid()
        continue_bid = input("Are there any more bidders? type yes or no: ")


    #code to announce winner
    bidding = False
    max_bid(auction_list)
        

