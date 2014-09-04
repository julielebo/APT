import gofish1

# Create empty deck, ensures both hands are empty
playDeck = []
jHand = {}
aHand = {}
gofish1.drawCard('Julie',playDeck,jHand)
gofish1.drawCard('Adam',playDeck,aHand)
assert len(jHand) == 0
assert len(aHand) == 0
