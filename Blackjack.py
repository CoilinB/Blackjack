# Imports the shuffle function from the random library, this is to shuffle the deck
# Imports the exit function from the sys library, this is to exit the program when the user wants to stop playing
from random import shuffle
from sys import exit

# Declares the deck
deck = []

class user:
    #Creates a name, amount, empty hand, and result of last round for each user
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount
        self.hand = []
        self.lastRound = None

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
    
    def calcHand(self):
        # Sets the default value of hands value
        handValue = 0

        # Adds the values of each card
        # This assumes the user wants to keep the ace card as a value of 11, after this calculation it can be adjusted
        for card in self.hand:
            match card:
                case '2' | '3' |'4' | '5' | '6' | '7' | '8' | '9' | '10':
                    handValue += int(card)
                case 'J' | 'Q' | 'K':
                    handValue += 10
                case 'A':
                    handValue += 11
        
        # Adjusts the value of aces to 1 if the hand value is greater than 21
        # It will only do this until the hand value is equal to or less than 21
        # If there are no more aces in the hand but the hand value is still over 21, the hand Value is set to bust and we stop trying to calculate the value
        tempHand = self.hand.copy()
        while handValue > 21:
            try:
                tempHand.pop('A')
            except:
                handValue = 'bust'
                break
            else:
                handValue -= 10

        # Returns the value of the hand
        # This could be either an integer from 0-21 or a string "bust"
        return handValue
            

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

def printInfoScreen(dealer, player):
    # Depending on the whether it's the players first round or not, it will ask the player to start the game or play again

    # If it's the users first time playing, it will continue to ask them to start the game until they type play
    # This insures the player is ready, as it will go straight into the first game after this
    if player.lastRound == None:
        clearScreen()
        print(f'You have ${player.amount} in your account')
        setScreen()

        while True:
            play = input('Type "play" when you\'re ready to start the game: ').lower().replace(' ', '')
            if play == 'play':
                break
            else:
                clearScreen()
                print(f'You have ${player.amount} in your account')
                setScreen()

    # If the user has already played a round, it will ask if they want to play again or stop
    # If they want to play again, it will start another round
    # If they want to stop playing, it will ask them to confirm and then exit the game with a nice message if they confirmed the exit
    else:
        clearScreen()
        print(f'You have ${player.amount} in your account')
        print(f'You {player.lastRound} your last round')
        setScreen()
        
        while True:
            again = input(f'Would you like to play again? (type "yes" or "no"): ').lower().replace(' ', '')
            if again == 'yes':
                blackjack(dealer, player)
            elif again == 'no':
                clearScreen()
                confirmation = input('Are you sure you want to leave the Blackjack table?\nYou will lose all your progress (type "exit" to exit or "cancel" to go back): ').lower().replace(' ', '')
                if confirmation == 'exit':
                    clearScreen()
                    exit('See you soon!' + '\n'*4)
                else:
                    clearScreen()
                    print(f'You have ${player.amount} in your account')
                    print(f'You {player.lastRound} your last round')
                    setScreen()
            else:
                clearScreen()
                print(f'You have ${player.amount} in your account')
                print(f'You {player.lastRound} your last round')
                setScreen()

def shuffleDeck():
    # Makes a deck and shuffles it
    global deck # -- Do we need to do this?
    deck = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] * 4
    shuffle(deck)

def clearScreen():
    # Clears the screen by printing 7 lines (the height of the terminal)
    print('\n'*9)

def setScreen():
    # Brings the output up by 4 lines so it's nice to look at
    print('\n'*4)

def dealCards(dealer, player):
    # Deals two cards two both the player and dealer from the top of the deck
    player.hand.append(deck.pop(0))
    dealer.hand.append(deck.pop(0))
    player.hand.append(deck.pop(0))
    dealer.hand.append(deck.pop(0))

def printHands(dealer, player):
    # Prints the dealers first card and the users hand
    dealer.printHand(True)
    player.printHand()
    setScreen()

def choices(player):
    pass

def calcDealerHand(dealer):
    pass


def blackjack(dealer, player):
    '''
    Plays one round of the game
    This can be called multiple times if the user wants to play again
    '''
    clearScreen()
    shuffleDeck()
    dealCards(dealer, player)
    
    choice = 'hit'
    while player.calcHand != 'bust' and choice == 'hit':
        choice = choices(player)

    calcDealerHand(dealer)
        

    # The next two lines will be removed later when we can actually decide who won and lost
    dealer.lastRound = 'lost'
    player.lastRound = 'won'
    printInfoScreen(dealer, player)

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

    # prints out the info screen for the user, this will be their first time playing so it will be different this time
    printInfoScreen(dealer, player)

    # Starts the game
    blackjack(dealer, player)

# Name guard
if __name__ == '__main__':
    main()