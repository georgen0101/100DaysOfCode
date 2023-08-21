from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
print("Running...")
print(logo)


participants_list = []

auction_live = True
while auction_live:

    participant_name = input("What is yout name? ")
    given_bid = int(input("What is your bid? "))
    
    participant_dictionary = {}
    participant_dictionary["name"] = participant_name
    participant_dictionary["bid"] = given_bid
    participants_list.append(participant_dictionary)
    
    more_bidders = input("Are there any other bidders? Type 'yes or 'no'. \n").lower()
    
    if more_bidders == "yes":
        clear()
    elif more_bidders == "no":
        auction_live = False
    else:
        print("Error! Invalid option")
        auction_live = False

highest_bidder_bid = 0
highest_bidder_name = ""
for participants in participants_list:
    if participants["bid"] > highest_bidder_bid:
        highest_bidder_bid = participants["bid"]
        highest_bidder_name = participants["name"]

message = f"/nThe winner is {highest_bidder_name} with a bid of ${highest_bidder_bid}"

print(message)

# print(participants_list)

print("Exiting... ")