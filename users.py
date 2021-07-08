#!/usr/bin/env python
import time
import random
#import unittest
from operator import itemgetter
import logging

#import cards
# http://www.developer.nokia.com/Community/Wiki/List_of_Dictionaries_in_Python
# http://stackoverflow.com/questions/8550912/python-dictionary-of-dictionaries
''' {name: [[my cards], [score cards], score, money]} '''
'''
NM: name (key)
0: order = [1,2,3]
1: connection (conn) 
2: my cards
3: score cards
4: score
5: money
6: my turn (True or False)
7: is first? (-1: not yet, 0: no, 1: yes) ==> -1: no, 1: yes
8: tmp
users[name] = [play_order, conn, [], [], 0, 100000, False, -1, '0']
'''

class User:
    def __init__(self, name):
        self.name = name

        
log_format = '{%(pathname)s:%(lineno)d} %(levelname)s:%(message)s'
logging.basicConfig(format=log_format, level=logging.DEBUG)

# gs_users is a list of dictionaries
gs_users = {}
# [(name, order),...]
ordered_user_list = []

cards_badak = []
# pick_cards_badak is used during processing pick command only
pick_cards_badak = []
cards_draw_pile = []

def match_with_badak(card_of_user):
	cards_badak.sort()
	matching_list=[]
	for card in cards_badak:
		if card[0] == card_of_user[0]:
			matching_list.append(card)
	return matching_list
	
def start_gs_game():
	assert len(gs_users) == 3, 'check on-line users...'
	del cards_badak[:]
	del cards_draw_pile[:]
	del ordered_user_list[:]

	play_cards=[x+y for x in '123456789ABC' for y in 'ABCD']
	play_cards.append("DA")
	play_cards.append("DB")
	random.shuffle(play_cards)
	logging.debug(play_cards)

	# distribute cards
	for i in range(6):
		cards_badak.append(play_cards.pop())
	pick_cards_badak[:] = cards_badak
	# it must be delayed to decide first player
	# cards_badak.sort()

	logging.debug(gs_users)
	for name, userlist in gs_users.items():
		logging.debug("%s is getting cards" % name)
		# initialize userlist
		userlist[2][:] = []
		userlist[3][:] = []
		userlist[4] = 0
		userlist[6] = False
		userlist[7] = -1
		userlist[8] = '0'
		
		for i in range(7):
			userlist[2].append(play_cards.pop())
		userlist[2].sort()
		assert len(userlist[2]) == 7, 'not equal...'
	logging.debug(gs_users)

	cards_draw_pile[:] = play_cards
	logging.debug(len(cards_draw_pile))
	logging.debug(cards_draw_pile)

# This function is for test...
def start_gs_game_with_arranged_cards():
	assert len(gs_users) == 3, 'check on-line users...'
	del cards_badak[:]
	del cards_draw_pile[:]
	del ordered_user_list[:]

	play_cards=['BD', 'AA', '5C', '3A', '2D', '2B', '4B', '4A', '7B', 'DB', '8A', 
			'3B', 'BB', '3D', '7D', '5A', 'DA', '9A', 'CC', '8D', '1D', '1A', '6D', 
			'6B', '4D', '1B', 'AB', '5D', '4C', 'BA', '9D', 'CD', '8C', '1C', '6A', 
			'2C', '2A', '3C', '9B', 'CB', '5B', 'AD', '7A', '7C', '9C', '6C', 'AC', 
			'BC', 'CA', '8B']
	logging.debug(play_cards)

	# distribute cards
	for i in range(6):
		cards_badak.append(play_cards.pop())
	pick_cards_badak[:] = cards_badak
	# it must be delayed to decide first player
	# cards_badak.sort()

	logging.debug(gs_users)
	for name, userlist in gs_users.items():
		logging.debug("%s is getting cards" % name)
		# initialize userlist
		userlist[2][:] = []
		userlist[3][:] = []
		userlist[4] = 0
		userlist[6] = False
		userlist[7] = -1
		userlist[8] = '0'
		
		for i in range(7):
			userlist[2].append(play_cards.pop())
		userlist[2].sort()
		assert len(userlist[2]) == 7, 'not equal...'
	logging.debug(gs_users)

	cards_draw_pile[:] = play_cards
	logging.debug(len(cards_draw_pile))
	logging.debug(cards_draw_pile)

def get_ordered_user_list():
	global ordered_user_list
	for name, userlist in gs_users.items():
		ordered_user_list.append((name, userlist[0]))
	ordered_user_list = sorted(ordered_user_list, key=itemgetter(1))

def who_is_next_player(cur_name):
	for idx in range(3):
		if ordered_user_list[idx][0] == cur_name:
			return ordered_user_list[(idx+1)%3][0]
	return None

def who_is_first_player():
	tmp_user_list = []
	for name, user_info in gs_users.items():
		assert user_info[8] != '0', "Error..."
		#change 2nd char of user_info[8]
		#A->G, B->F, C->E, D->D
		char = chr(2*ord('D') - ord(user_info[8][1]))
		tmp_user_list.append((name, user_info[8][0]+char))
	logging.debug(tmp_user_list)
	# if now is day, sort as ascending order
	# if night, sort as descending order
	now = time.localtime()
	if 6 <= now.tm_hour < 18: 
		tmp_user_list = sorted(tmp_user_list, key=itemgetter(1), reverse=True)
	else:
		tmp_user_list = sorted(tmp_user_list, key=itemgetter(1))
	name = tmp_user_list[0][0]
	# set "is_first" to True... where??
	gs_users[name][7] = 1
	gs_users[name][6] = True
	return name

# Get maximum pick_num : (4-6)
def get_str_pick_num():
	pick_num = 6
	for name, user_info in gs_users.items():
		if user_info[8] != '0':
			pick_num -= 1
	return str(pick_num)


def test_init():
	gs_users['01'] = [1, 1, [], [], 0, 10000, False, -1, '1A']
	gs_users['02'] = [4, 2, [], [], 0, 10000, False, -1, 'AB']
	gs_users['03'] = [3, 3, [], [], 0, 10000, False, -1, 'AA']

if __name__ == "__main__":
	test_init()
	#print get_str_pick_num()
	start_gs_game()
	logging.debug(who_is_first_player())
	print 'xxxxxxxxxxxxxxxxxxxxxxxxx'
	print cards_badak
	print cards_draw_pile
	cards_badak[3] = 'DB'
	cards_draw_pile[-1] = 'DC'
	print 'xxxxxxxxxxxxxxxxxxxxxxxxx'
	print cards_badak
	print cards_draw_pile
#	preparing_new_round('01')
	print 'xxxxxxxxxxxxxxxxxxxxxxxxx'
	print gs_users
	print cards_badak
	print cards_draw_pile
	'''
	get_ordered_user_list()
	print ordered_user_list
	print "xxxxxxxxxxxxxxxxxxxxxxxxxx"
	print who_is_next_player('01')
	print who_is_next_player('02')
	print who_is_next_player('03')
	print who_is_next_player('04')
	who_is_first_player()
	'''



'''
def find_gs_user(name):
	return True

def create_gs_user():

def get_gs_user()
'''


'''
import pickle

#save gs_users
try:
	with open('gsusers.dat', 'wb') as gsusers_save_data:
		pickle.dump(gs_users, gsusers_save_data)
except IOError as err:
	print('File error: ' + str(err))
except pickle.PickleError as perr:
	print('Pickling error: ' + str(perr))
'''

'''
#initialize gs_users..
with open('gsusers.dat', 'rb') as gsusers_restored_data:
	gs_users = pikcle.load(gsusers_restored_data)
'''
