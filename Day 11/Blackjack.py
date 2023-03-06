import random
from logo import logo


def dealCard():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculateScore(arr):
    score = sum(arr)
    if score == 21 and len(arr) == 2:
        return 0
    elif 11 in arr and score > 21:
        arr.remove(11)
        arr.append(1)
        return score - 10

    return score


def compareScore(player_score, dealer_score):
    if player_score == dealer_score:
        return "Draw"
    elif dealer_score == 0:
        return "You lose, dealer has a Blackjack"
    elif player_score == 0:
        return "You win, you have a Blackjack"
    elif player_score > 21:
        return "You lose, went over the limit"
    elif dealer_score > 21:
        return "You win, opponent went over the limit"
    elif player_score > dealer_score:
        return "You win, you have the higher hand"
    else:
        return "You lose, dealer has the higher hand"


choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

if choice == 'y':
    print(logo)

while choice == 'y':
    isGameOver = False

    player = []
    dealer = []

    for _ in range(2):
        player.append(dealCard())
        dealer.append(dealCard())

    while not isGameOver:
        playerScore = calculateScore(player)
        dealerScore = calculateScore(dealer)

        print(f"Your cards: {player}, Your score: {playerScore}")
        print(f"Dealer's first card: {dealer[0]}")

        if playerScore == 0 or dealerScore == 0 or playerScore >= 21:
            isGameOver = True
        else:
            player_deal = input("Type 'y' to get another card or 'n' to pass: ")
            if player_deal == 'y':
                player.append(dealCard())
                playerScore = calculateScore(player)
            else:
                isGameOver = True

    while dealerScore != 0 and dealerScore < 17:
        dealer.append(dealCard())
        dealerScore = calculateScore(dealer)

    print(f"Your hand: {player}")
    print(f"Dealer's hand: {dealer}")
    result = compareScore(playerScore, dealerScore)
    print(result)

    choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")