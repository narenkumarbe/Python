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

Output:
J of Diamond
3 of Spade
6 of Spade
5 of Club
10 of Diamond
6 of Diamond
J of Club
5 of Spade
K of Diamond
2 of Club
9 of Diamond
8 of Diamond
A of Diamond
5 of Hearts
4 of Hearts
Q of Spade
A of Club
J of Hearts
8 of Hearts
9 of Club
A of Hearts
7 of Spade
9 of Spade
4 of Club
6 of Club
8 of Spade
6 of Hearts
J of Spade
2 of Diamond
3 of Club
9 of Hearts
5 of Diamond
7 of Diamond
4 of Spade
Q of Hearts
K of Club
Q of Diamond
10 of Spade
10 of Club
2 of Hearts
4 of Diamond
7 of Club
7 of Hearts
3 of Diamond
Q of Club
3 of Hearts
K of Spade
8 of Club
K of Hearts
A of Spade
10 of Hearts
2 of Spade
