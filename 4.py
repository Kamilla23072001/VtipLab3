s = '''Stay you imperfect Speakers, tell me more:
By Sinells death, I know I am Thane of Glamis,
But how, of Cawdor? the Thane of Cawdor liues
A prosperous Gentleman: And to be King,
Stands not within the prospect of beleefe,
No more then to be Cawdor. Say from whence
You owe this strange Intelligence, or why
Vpon this blasted Heath you stop our way
With such Prophetique greeting?
Speake, I charge you.'''

e = '''I have been twice in England. In 1833, on my return from a short tour in Sicily, Italy, and France, I crossed from Boulogne, and landed in London at the Tower stairs. It was a dark Sunday morning; there were few people in the streets; and I remember the pleasure of that first walk on English ground, with my companion, an American artist, from the Tower up through Cheapside and the Strand, to a house in Russell Square, whither we had been recommended to good chambers'''

s1= s.split()
e1 = e.split()

s2 = set(s1)
e2 = set(e1)

sameWords = s2 & e2
seperateWords = s2 ^ e2

print(sameWords)
print(seperateWords)