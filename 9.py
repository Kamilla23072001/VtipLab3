import collections
e = '''I have been twice in England. In 1833, on my return from a short tour in Sicily, Italy, and France, I crossed from Boulogne, and landed in London at the Tower stairs. It was a dark Sunday morning; there were few people in the streets; and I remember the pleasure of that first walk on English ground, with my companion, an American artist, from the Tower up through Cheapside and the Strand, to a house in Russell Square, whither we had been recommended to good chambers'''
spisok = e.split()
count = (collections.Counter(spisok))

print(count)