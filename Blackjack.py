# Imports the shuffle function from the random library, this is to shuffle the deck
from random import shuffle

# Declares the deck
deck = []

class user:
    #Creates a name, amount and an empty hand for each user
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount
        self.hand = []

    # Prints the hand of either the dealer or user depending on which is called
    # Set dealersFirst to True if you want to print the first card of the dealers hand
    def printHand(self, dealersFirst=False):
        if dealersFirst == True and self.name == 'dealer':
            print(f'The Dealers first card is: {self.hand[0]}')
        else:
            if self.name == 'dealer':
                print(f'The Dealers hand was: {', '.join(self.hand)}')
            else:
                print(f'Your Hand is: {', '.join(self.hand)}')

def getMoney():
    '''
    Gets the users money and makes sure its acceptable
    Returning the value once it's acceptable
    '''
    amount = 0

    while True:
        tryAmount = input('How much money would you like to add to your account? ')
        try:
            amount = round(float(tryAmount), 2)
            if amount <= 0:
                raise ValueError('Needs to be a positive number')
        except:
            clearScreen()
            print('You need to input a positive number for your money')
            setScreen()
        else:
            break
    
    return amount

def shuffleDeck():
    # Makes a deck and shuffles it
    global deck # -- Do we need to do this?
    deck = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] * 4
    shuffle(deck)

def clearScreen():
    # Clears the screen by printing 7 lines (the height of the terminal)
    print('\n'*8)

def setScreen():
    # Brings the output up by 4 lines so it's nice to look at
    print('\n'*4)

def dealCards(dealer, player):
    # Deals two cards two both the player and dealer from the top of the deck
    player.hand.append(deck.pop(0))
    dealer.hand.append(deck.pop(0))
    player.hand.append(deck.pop(0))
    dealer.hand.append(deck.pop(0))

    # Prints the dealers first card and the users hand
    dealer.printHand(True)
    player.printHand()
    setScreen()

def blackjack(dealer, player):
    '''
    Plays one round of the game
    This can be called multiple times if the user wants to play again
    '''
    clearScreen()
    shuffleDeck()
    dealCards(dealer, player)

def main():
    # Welcomes the user
    clearScreen()
    print('----------| Welcome To The Blackjack Table |----------')
    setScreen()

    # Gets the users money
    amount = getMoney()

    # Creates the players
    dealer = user('dealer', 2500)
    player = user('player', amount)

    # Starts the game
    blackjack(dealer, player)

if __name__ == '__main__':
    main()