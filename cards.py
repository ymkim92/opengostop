class Card:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class GoStopCard(Card):
    def __init__(self, x, y, point):
        super.__init__(x, y)
        self.point = point


gscards_dict = {'1A':['GW', 0],
				'1B':['TT', 1],
				'1C':['PI', 0],
				'1D':['PI', 0],
				'2A':['GO', 1],
				'2B':['TT', 1],
				'2C':['PI', 0],
				'2D':['PI', 0],
				'3A':['GW', 0],
				'3B':['TT', 1],
				'3C':['PI', 0],
				'3D':['PI', 0],
				'4A':['GO', 1],
				'4B':['TT', 2],
				'4C':['PI', 0],
				'4D':['PI', 0],
				'5A':['GO', 0],
				'5B':['TT', 2],
				'5C':['PI', 0],
				'5D':['PI', 0],
				'6A':['GO', 0],
				'6B':['TT', 3],
				'6C':['PI', 0],
				'6D':['PI', 0],
				'7A':['GO', 0],
				'7B':['TT', 2],
				'7C':['PI', 0],
				'7D':['PI', 0],
				'8A':['GW', 0],
				'8B':['GO', 1],
				'8C':['PI', 0],
				'8D':['PI', 0],
				'9A':['GO', 0],
				'9B':['TT', 3],
				'9C':['PI', 0],
				'9D':['PI', 0],
				'AA':['GO', 0],
				'AB':['TT', 3],
				'AC':['PI', 0],
				'AD':['PI', 0],
				'BA':['GW', 0],
				'BB':['PI', 1],
				'BC':['PI', 0],
				'BD':['PI', 0],
				'CA':['GW', 1],
				'CB':['GO', 0],
				'CC':['TT', 0],
				'CD':['PI', 1],
				'DA':['BO', 0],
				'DB':['BO', 0]}

if __name__ == '__main__':
	print "Total number of cards: %d" % len(gscards_dict)
	#print "Total number of GWANG: %d" % len(gscards_dict)
	for items in gscards_dict:
		print items, gscards_dict[items]
