from random import shuffle

card_dict = {}
for i in range(1,53):
	suit_idx = (i-1)//13
	if suit_idx == 0: suit = 'H' 
	if suit_idx == 1: suit = 'D' 
	if suit_idx == 2: suit = 'S'
	if suit_idx == 3: suit = 'C'


	value = (i%13)+1 
	face = str(value) 
	if value == 11: face = 'J' 
	if value == 12: face = 'Q'
	if value == 13: face = 'K'
	if value == 1:  face = 'A'	

	name = face+suit 
	card_dict[i] = (suit, value, face, name)

#print(cardDict) 

class Deck(object): 
	deck_num = 0
	def __init__(self):
		self.cards = []
		self.discard_pile = []
		Deck.deck_num += 1 
		for i in range(1,53):
			self.cards.append(i)
		
	def shuffle(self):
		shuffle(self.cards)
		return self.cards
	
	def remove(self):
		self.discard_pile.append(self.cards.pop())
		
	def deal_card(self):
		return (self.cards.pop()) 

	def count(self):
		return len(self.cards)



class Player(object):
	def __init__(self):
		self.hand = []
	
	def hit(self, deck):
		try: 
			self.hand.append(deck.deal_card())
		except TypeError as e:
			return e
	def hand_check(self):
		return self.hand


...
