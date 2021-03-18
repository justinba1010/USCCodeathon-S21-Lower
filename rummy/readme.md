Over breaks, I enjoy playing various card games with my friends. One of my favorites is Gin Rummy, a card game which follows a very strict scoring algorithm for each hand played.

Given an input n number of cards between 1 and 52, in the format shown below, your program should return the total points available in the hand based on my house Rummy rules. 

Sets of 3 cards of the same numerical value of different suits: 15 points
Sets of 4 cards of the same numerical value of different suits: 20 points
Sets of 3 face-cards (including tens) of the same value of different suits: 30 points
Sets of 4, face-cards (including tens) of the same value of different suits: 40 points
Set of 3 aces of different suits: 45 points
Set of 4 aces of different suits: 60 points

Constraints:
1 <= n <= 52

Format of data:
H = Hearts
C = Clubs
S = Spades
D = Diamonds

2-9: numerical value cards
0: ten
J: jack
Q: queen
K: king
A: ace

Example format of data:
10 0H 0S 0C KS 3D 5C 8C 9S AC 2D
would return 30, for three tens of different suits.

45 JH 9D 3S 0S 4D 3D 9S 7H JS KH 3S 0H 9C QH AS QS QS 4C 2S 5S 8C 6H 6C 9C KC JC AS 3C AC 2C 6C 0C 6H 2D 2S KH JD JD 6D 0D AS 7S 2C KD 7D
210

40 7C 3D QH 2S 4H 4C 3D 4S 9H 5D 6D 8H 8S 5H 8S AS JD 4D AD 0H 0S KH 5D AC JH AD 4D QH 2C 0S 5C 5H JC KH 9S 4D 7D KH 7H 2D
180

25 QH QD 2C AH QD 0D 0H JS QC 6C 8D 3D 3S AD 7S 2H 0H QD 6D KC 6C 7H 2H 8S 2D
60

33 8S 9H 6S 6H QC QC 2S 4C 2H KD 0C 7C 9H 3D 8S 0C 6C 4D 2D 9C 9D AC 8D 4H 0S AH 4C KC 8S KC JH 8S 5H
130

39 0D KH AS 4S 8D 8D QC QH 5H QC 4D 4D 6D 8H 0S 6C QS 6S 4S JC JS 0H KS 0C 2C 5S 6C 5H 2S 4S 7D 5S 5C 7C 2C QC 9D 5D 4H
90

38 7H QS JH 6S AH QD 7D KS 4S 4H 8C 8H 4D 9S JC 7H AD 8H 9D 7S 0S 8H 7C 4S 5S 7C 9D 6S 6D 7C 3C 3C JS 3S 8C 3H 8D QC
100
