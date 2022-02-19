import os
import random

DECK = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] * (10 * 4)

wins = 0
losses = 0
draws = 0
count = 0
choice = 0


def dealer(deck, player="Dealer"):
    hand = []
    random.shuffle(deck)

    if player == "Player":
        return _dealPlayer(deck, hand)

    return _dealDealer(deck, hand)


def _dealPlayer(deck, hand):
    _blacklistedCards = [10, 11, 12, 13]
    while True:
        card = deck.pop()
        if card not in _blacklistedCards:
            if card == 14:
                card = "A"

            hand.append(card)

        if len(hand) > 1:
            return hand


def _dealDealer(deck, hand):
    _mustContainCards = [10, 11, 12, 13]
    for i in range(2):
        card = deck.pop()
        if card == 11:
            card = "J"
        if card == 12:
            card = "Q"
        if card == 13:
            card = "K"
        if card == 14:
            card = "A"
        hand.append(card)

        if hand[0] not in _mustContainCards:
            randomCard = random.choice(_mustContainCards)
            if randomCard == 11:
                randomCard = "J"
            elif randomCard == 12:
                randomCard = "Q"
            elif randomCard == 13:
                randomCard = "K"
            hand[0] = randomCard

    return hand


def play_again():
    global count
    c = 99
    again = input("Do you want to play again? (Y/N) : ").lower()
    while again == "y" and count > c:
        print("bye")
        exit()

    else:
        count += 1
        print("the total of games are " + str(count))
        game()


def total(hand):
    _total = 0
    for card in hand:
        if card == "J" or card == "Q" or card == "K":
            _total += 10
        elif card == "A":
            if _total >= 11:
                _total += 1
            else:
                _total += 11
        else:
            _total += card
    return _total


def hit(hand):
    card = DECK.pop()
    if card == 11:
        card = "J"
    if card == 12:
        card = "Q"
    if card == 13:
        card = "K"
    if card == 14:
        card = "A"
    hand.append(card)
    return hand


def clear():
    if os.name == 'nt':
        os.system('CLS')
    if os.name == 'posix':
        os.system('clear')


def print_results(dealer_hand, player_hand):
    clear()

    print("\n    WELCOME TO BLACKJACK!\n")
    print("-" * 30 + "\n")
    print(
        "\033[1;32;40mWINS:  \033[1;37;40m%s   \033[1;31;40mLOSSES:  \033[1;37;40m%s   \033[1;34;40mDRAWS \033[1;37;40m%s\n" % (
            wins, losses, draws))
    print("-" * 30 + "\n")
    print("The dealer has a " + str(dealer_hand) + " for a total of " + str(total(dealer_hand)))
    print("You have a " + str(player_hand) + " for a total of " + str(total(player_hand)))


def blackjack(dealer_hand, player_hand):
    global wins
    global losses
    if total(player_hand) == 21:
        print_results(dealer_hand, player_hand)
        print("Congratulations! You got a Blackjack!\n")
        wins += 1
        play_again()
    elif total(dealer_hand) == 21:
        print_results(dealer_hand, player_hand)
        print("Sorry, you lose. The dealer got a blackjack.\n")
        losses += 1
        play_again()


def score(dealer_hand, player_hand):
    # score function now updates to global win/loss variables
    global wins
    global losses
    global draws
    if total(player_hand) == 21:
        print_results(dealer_hand, player_hand)
        print("Congratulations! You got a Blackjack!\n")
        wins += 1
    elif total(dealer_hand) == 21:
        print_results(dealer_hand, player_hand)
        print("Sorry, you lose. The dealer got a blackjack.\n")
        losses += 1
    elif total(player_hand) > 21:
        print_results(dealer_hand, player_hand)
        print("Sorry. You busted. You lose.\n")
        losses += 1
    elif total(dealer_hand) > 21:
        print_results(dealer_hand, player_hand)
        print("Dealer busts. You win!\n")
        wins += 1
    elif total(player_hand) < total(dealer_hand):
        print_results(dealer_hand, player_hand)
        print("Sorry. Your score isn't higher than the dealer. You lose.\n")
        losses += 1
    elif total(player_hand) > total(dealer_hand):
        print_results(dealer_hand, player_hand)
        print("Congratulations. Your score is higher than the dealer. You win\n")
        wins += 1
    elif total(player_hand) == total(dealer_hand):
        print_results(dealer_hand, player_hand)
        print(". Your score is tie with the dealer. You draw\n")
        draws += 1


def game():
    global wins
    global losses
    global draws
    global count
    global choice
    clear()
    print("\n    WELCOME TO BLACKJACK!\n")
    print("-" * 30 + "\n")
    print(
        "\033[1;32;40mWINS:  \033[1;37;40m%s   \033[1;31;40mLOSSES:  \033[1;37;40m%s   \033[1;34;40mDRAWS \033[1;37;40m%s\n" % (
            wins, losses, draws))
    print("-" * 30 + "\n")
    dealer_hand = dealer(DECK)
    player_hand = dealer(DECK, "Player")
    print("The dealer is showing a " + str(dealer_hand[0]))
    print("You have a " + str(player_hand) + " for a total of " + str(total(player_hand)))
    blackjack(dealer_hand, player_hand)

    _quit = False
    while not _quit:
        choice = input("Do you want to [H]it, [S]tand, or [Q]uit: ").lower()
        if count > 100:
            print("Bye!")
            _quit = True
            exit()
        elif choice == 'h':
            hit(player_hand)
            print(player_hand)
            print("Hand total: " + str(total(player_hand)))
            if total(player_hand) > 21:
                print('You busted')
                losses += 1
                play_again()
        elif choice == 's':
            while total(dealer_hand) < 17:
                hit(dealer_hand)
                print(dealer_hand)
                if total(dealer_hand) > 21:
                    print('Dealer busts, you win!')
                    wins += 1
                    play_again()
            score(dealer_hand, player_hand)
            play_again()
        elif choice == "q":
            print("Bye!")
            _quit = True
            exit()


if __name__ == "__main__":
    game()