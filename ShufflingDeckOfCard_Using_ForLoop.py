import random
card_faces = []
suit = ['Club', 'Spade', 'Hearts', 'Diamond']
royals = ['J', 'Q', 'K', 'A']
deck = []

for i in range(2,11):
    card_faces.append(str(i))
    
for j in range(4):
    card_faces.append(royals[j])
    
for k in range(4):
    for l in range(13):
        card = (card_faces[l] + " of " + suit[k])
        deck.append(card)

random.shuffle(deck)

for m in range(52):
    print(deck[m])
