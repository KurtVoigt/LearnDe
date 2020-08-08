import deck

#loads deck into memory
#inp = input("Enter name of deck file: ")
cards = deck.Deck("example.deck")
#runs through each card in the deck, each card will be assesed and weighted in the card class
#print(cards.deck[0].word)
lengthCards = len(cards.deck)
for i in range(lengthCards):
  cards.deck[i].displayCard()
cards.writeWeight()
