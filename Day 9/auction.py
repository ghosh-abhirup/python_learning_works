print("AUCTION HOUSE")

bid_collection = {}
bids_finished = False


def find_max_bid(bid_collection):
    maxBid = ""
    res = 0
    for bid in bid_collection:
        if res < bid_collection[bid]:
            res = bid_collection[bid]
            maxBid = bid

    print(f"The maximum bid of ${bid_collection[maxBid]} is from {maxBid}")


while not bids_finished:
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))

    bid_collection[name] = bid

    confirmation = input("Are there any more bids? Say 'Yes' or 'No' ")

    if confirmation == 'No':
        bids_finished = True

find_max_bid(bid_collection)
