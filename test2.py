import gofish1

# Create empty deck, ensures both hands are empty
playDeck = [("5","spades"),("5","diamonds"),("5","hearts"),("5","cloves")]
jHand = {}
gofish1.drawCard("Julie",playDeck,jHand)
gofish1.drawCard("Julie",playDeck,jHand)
gofish1.drawCard("Julie",playDeck,jHand)
gofish1.drawCard("Julie",playDeck,jHand)
assert len(jHand)==0
