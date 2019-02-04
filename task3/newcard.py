class card():
    suite_names = ["Clubs","Diamonds","Hearts","Spades"]
    rank_names = [None,"Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]
    
    def __init__(self,rank=0,suit=2):
        self.rank = rank
        self.suite = suit

    def __str__(self):
         return f"The rank is {card.rank_names[self.rank]} and the suit is {card.suite_names[self.suite]}"

ace_of_spade = card(1,3)
print(ace_of_spade)
