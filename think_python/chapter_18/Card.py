import random

# Card class
class Card:
    """Represents a standard playing card."""
    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
   
    def __init__(self, suit=0, rank=2):        
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return '%s of %s' % (Card.rank_names[self.rank], Card.suit_names[self.suit])

    def __lt__(self, other):
        return (self.suit, self.rank) < (other.suit, other.rank)


# Deck class
class Deck:
    """Represents a deck of playing cards."""
    def __init__(self):        
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)
        
    def __str__(self):
        cardsStr = []
        for card in self.cards:
            cardsStr.append(str(card))
        return '\n'.join(cardsStr)

    def shuffle(self):
        random.shuffle(self.cards)

    def sort(self, reverse=True):        
        self.cards.sort(reverse=reverse)

    def pop_card(self):
        return self.cards.pop()

    def add_card(self, card):
        self.cards.append(card)

    def move_card(self, hand, num):
        for i in range(num):
            hand.add_card(self.pop_card())

    def deal_hands(self, hands, cards):
        hands_list = []
        for i in range(hands):
            hand = Hand('Hand' + str(i))
            for i in range(cards):
                hand.add_card(self.pop_card())
            hands_list.append(hand)
        return hands_list

    
# Hand class
class Hand(Deck):
    """Represents a hand of playing cards."""
    def __init__(self, label=''):
        # if we call the following line the cards will be populated in the constructor of class 'Deck' but we need an empty hand at the beginning
        # super().__init__()
        self.cards = []
        self.lable = label


######################## main #########################
def main():
    # c1 = Card(2, 10)
    # print(c1)
    # c2 = Card(0, 12)
    # print(c2)
    # print(c1 > c2)
    # print('-------------------------')
    # deck = Deck()
    # deck.shuffle()
    # print(deck.pop_card())
    # print(deck.pop_card())
    # print(deck.pop_card())
    # deck.shuffle()
    # print(deck.pop_card())
    # print(deck.pop_card())
    # print(deck.pop_card())
    # deck.sort()
    # print('------------ sorted -------------')    
    # print(deck)
    deck = Deck()
    deck.shuffle()
    # hand = Hand('Ramin')
    # print(hand.lable)
    # deck.move_card(hand, 5)
    # print('------------ hand -------------')    
    # print(hand)
    # print('------------ deck -------------')    
    # print(deck)
    for l in deck.deal_hands(3, 5):
        print('......')
        print(l)




if __name__ == "__main__":
    main()