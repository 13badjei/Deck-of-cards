class Card:
    def __init__(self, suit, number):
        self._suit = suit
        self.number = number
        
    def __repr__(self):
        return self.number + " of " + self.suit
    
    @property
    def suit(self):
        return self._suit

    @suit.setter
    def suit(self, suit):
        if suit in ["hearts", "clubs", "diamonds", "spades"]:
            self._suit = suit
        else:
            print("That's not a suit!")
            
my_card = Card("hearts", "6")
print(my_card)
        
