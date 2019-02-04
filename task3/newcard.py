class card():
    suite_names = ["Clubs","Diamonds","Hearts","Spades"]
    rank_names = [None,"Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]
    
    def __init__(self,rank=0,suit=2):
        self.rank = rank
        self.suite = suit

    def __str__(self):
         return f"The rank is {card.rank_names[self.rank]} and the suit is {card.suite_names[self.suite]}"

    def __lt__(self):
        if self.suit < other.suit: return True
        if self.suit > other.suit: return False
        return self.rank < other.rank

    def __eq__(self,other):
        return self.rank == self.rank and self.suit == other.suit

class Deck:
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1,14):
                card = card(suit,rank)
                self.cards.append(card)
    
    def pop_card(self):
        return self.cards.pop()

#ace_of_spade = card(1,3)
#print(ace_of_spade)
mycards = Deck()
for card in mycards:
    print(card)
