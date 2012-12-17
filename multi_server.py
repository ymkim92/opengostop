#!/usr/bin/env python
# base code: http://rosettacode.org/wiki/Chat_server#Python

import socket
import thread
import time
import logging

import users
import check
from users import cards_draw_pile

HOST = ""
PORT = 4004
MAX_USERS = 3
# If 3 user is on-line, the GAME_READY is True
GAME_READY = False
GAME_START = False
play_order = 1

log_format = '{%(pathname)s:%(lineno)d} %(levelname)s:%(message)s'
logging.basicConfig(format=log_format, level=logging.DEBUG)

help_msg = ["Basic commands", 
			"- who: show who are here and each score if game is started", 
			"- hel: help",
			"- exit: quit or exit",
			"Commands related to playing game",
			"- pick # (1-6) : e.g., pick 3",
			"- match ## (1A~CD, DA, DB) : e.g., match 3C or 3c",
			"Commands related to cards", "- smc: show my cards",
			"- sms: show my score cards (+ score)", 
			"- sbc: show badak cards"]

def accept(conn):
	"""
	Call the inner func in a thread so as not to block. Wait for a 
	name to be entered from the given connection. Once a name is 
	entered, set the connection to non-blocking and add the
	user to the users dict.
	This thread is very simple. Server does almost everything for clients
	"""
	def threaded():
		global play_order
		while True:
			conn.send("Please enter your name: ")
			try:
				name = conn.recv(1024).strip()
			except socket.error:
				continue
			if name in users.gs_users:
				conn.send("Name entered is already in use.\n")
			elif name:
				conn.setblocking(False) 
				# add new user and initialize its information
				users.gs_users[name] = [play_order, 
							conn, [], [], 0, 100000, False, -1, '0']
				play_order += 1
				broadcast(name, "+++ %s arrived +++" % name) 
				break 
	thread.start_new_thread(threaded, ()) 

def send_all(message): 
	logging.info(message) 
	for to_name, userlist in users.gs_users.items(): 
		try: 
			userlist[1].send(message + "\n") 
		except socket.error: 
			pass 

def broadcast(name, message): 
	""" Send a message to all users from the given name.  """ 
	logging.info(message)
	for to_name, userlist in users.gs_users.items(): 
		if to_name != name: 
			try: 
				userlist[1].send(message + "\n") 
			except socket.error: 
				pass 

def disconnect(name):
	global GAME_READY, GAME_START
	del users.gs_users[name] 
	broadcast(name, "--- %s leaves ---" % name) 
	GAME_READY = False
	GAME_START = False

def show_cards_to_all_users():
	for to_name, userlist in users.gs_users.items(): 
		try: 
			userlist[1].send("Your cards are %s\n" % userlist[2]) 
		except socket.error: 
			pass 
	users.cards_badak.sort()
	send_all("Badak cards are %s" % users.cards_badak)

# if badak cards have bonus cards, then give it to first player
def preparing_new_round(first_player):
	for idx in range(len(users.cards_badak)):
		if users.cards_badak[idx][0] == 'D':
			users.gs_users[first_player][3].append(users.cards_badak.pop(idx))
			msg="%s got a bonus card" % first_player
			send_all(msg)
			card = users.cards_draw_pile.pop()
			users.cards_badak.append(card)
			while card[0] == 'D':
				users.gs_users[first_player][3].append(users.cards_badak.pop())
				msg="%s got a bonus card" % first_player
				send_all(msg)
				card = users.cards_draw_pile.pop()
				users.cards_badak.append(card)



'''
def send_message_in_order(msg, ordered_list, first=False):
	if first:
		for name, userlist in users.gs_users.items():
			userlist[6] = '0'
		player_name = ordered_list[0][0]
	else:
		player_name = ordered_list[1][0]
#		if users.gs_users[player_name][6] != '0'
	print msg
	users.gs_users[player_name][1].send(msg)
'''

def start_game():
	msg_ready='We need to decide first player... Wait to pick a card..'
	send_all(msg_ready)
	users.start_gs_game_with_arranged_cards()

	#elect_first_player
	users.get_ordered_user_list()
	# [(name, order),...]
	# send message to first user in order to select a card
	# so we want to decide who is first player..
	player_name = users.ordered_user_list[0][0]
	users.gs_users[player_name][1].send("Choose a card (1-6): pick #\n") 
	users.gs_users[player_name][6] = True
	return True
		
def process_play_command(message, name, userlist):
	msg_list = message.split()
	# your turn?
	if not userlist[6]:
		msg = "This is not your turn..\n"
		userlist[1].send(msg)
		return

	if not GAME_START:
		msg = "Game is not started.. You can't use this command\n"
		userlist[1].send(msg)
		return
	
	# argument is correct?
	card_num = check.check_message_syntax(msg_list, player_name=name)
	logging.debug(card_num)
	if card_num < 0:
		msg = "play command ERROR.. Try again."
		userlist[1].send(msg)
		return
	
	# Okay, so far so good..
	logging.debug("users's cards: %s" % userlist[2])
	logging.debug("users's card[%d]: %s" % (card_num-1, userlist[2][card_num-1])) 
	logging.debug("badak card: %s" % str(users.cards_badak)) 

	card_from_pile = []

	card_of_user = userlist[2].pop(card_num-1)

	card_from_pile.append(users.cards_draw_pile.pop())
	
	while card_from_pile[-1][0] == 'D':
		card_from_pile.append(users.cards_draw_pile.pop())

	logging.debug("draw pile: %s" % str(cards_draw_pile))
	# Phase 1
	if card_of_user[0] != card_from_pile[-1][0]:
		matched_list = users.match_with_badak(card_of_user)
		logging.debug("matched list: %s" % str(matched_list))
		if len(matched_list) == 0:
			# Phase 2
			matched_list_with_pile = users.match_with_badak(card_from_pile[-1])
			logging.debug("matched_list_with_pile: %s" % str(matched_list_with_pile))
			if len(matched_list_with_pile) == 0:
				pass
			elif len(matched_list_with_pile) == 1:
				userlist[3].extend(matched_list_with_pile)
				userlist[3].extend(card_from_pile)
			elif len(matched_list_with_pile) == 2:
				pass
			elif len(matched_list_with_pile) == 3:
				pass
			else:
				assert(False)

		elif len(matched_list) == 1:
			# 1. just get one pair
			
			# 2. just get two different pairs (Happy!!)
			
			pass
		elif len(matched_list) == 2:
			pass
		elif len(matched_list) == 3:
			pass
		else:
			assert(False)
		users.cards_badak.append(card_of_user)

	else:
		# more complicated...
		pass

#	if len(card_from_pile) == 1:
		# only one match with badak cards?

		
		#userlist[3].append(card_from_pile)
	
#	on_time_flag = check.check_on_time(msg_list, users.gs_users)
#	if pick_num != -1 and on_time_flag:
#		logging.debug(users.pick_cards_badak) 

def process_pick_command(message, name, userlist):
	global GAME_START
	msg_list = message.split()
	str_pick_num = users.get_str_pick_num()
	pick_num = check.check_message_syntax(msg_list, str_pick_num)
	logging.debug(pick_num)
	on_time_flag = check.check_on_time(msg_list, users.gs_users)
	if GAME_START:
		msg = "Game was already started.. You can't use this command\n"
		userlist[1].send(msg)
		return
	if pick_num != -1 and on_time_flag:
		logging.debug(users.pick_cards_badak) 
		if userlist[8] != '0':
			userlist[1].send("You already choosed a card (%s)\n" % 
				userlist[8])
			userlist[1].send("Wait a moment\n") 
		elif userlist[6]:
			userlist[8] = users.pick_cards_badak[pick_num-1]
			# delete a picked card from pick_cards_badak
			users.pick_cards_badak.pop(pick_num-1)

			send_all("%s picks %s" % (name, userlist[8]))
			userlist[6] = False
			# if user is last one, then start go-stop game
			if name == users.ordered_user_list[2][0]:
				# decide first user and play game...
				first_player = users.who_is_first_player()
				logging.info("First player is %s" % first_player)
				# if badak cards have bonus cards, 
				# then give it to first player
				preparing_new_round(first_player)
				GAME_START = True
				logging.info('start this round...')
				msg = "First player is %s. Let's start.." % first_player
				send_all(msg)
				# show one's own cards to user
				show_cards_to_all_users()
#				users.gs_users[first_player][1].send(users.gs_users[first_player][2], "\n")
				msg = "Your turn\n"
				users.gs_users[first_player][1].send(msg)

				#play_game_now()
			else:
				# send pick message to next user
				player_name = users.who_is_next_player(name)
				msg = ('Choose a card (1-%d): pick #\n' % 
						(int(str_pick_num) - 1))
				logging.debug(msg)
				users.gs_users[player_name][1].send(msg) 
				users.gs_users[player_name][6] = True
		else:
			# need to be more specific [TODO]
			msg = "It's not your turn... Wait a sec..\n"
			userlist[1].send(msg)
	elif pick_num == -1:
		msg = 'You have to use pick 1-%s..\n' % str_pick_num
		logging.debug(msg)
		userlist[1].send(msg)

def processing_command():
	for name, userlist in users.gs_users.items(): 
		try: 
			message = userlist[1].recv(1024) 
			if not message: 
				# Empty string is given on disconnect. 
				disconnect(name)
			elif message.strip() == 'help':
				for message in help_msg:
					userlist[1].send("%s\n" % message)	
			# play command has two function
			# 1. match with one of the badak cards
			# 2. put down a bonus card
			# if you have bonus card(s), you can use "play" command
			# to put down your card and take one from draw pile
			# You can use this command if following two conditions meet
			# 1. You have to have bonus card(s)
			# 2. This is your turn
			elif message.strip()[0:4] == 'play':
				process_play_command(message.strip(), name, userlist)

			# pick # to decide first player
			elif message.strip()[0:4] == 'pick':
				process_pick_command(message.strip(), name, userlist)


			elif message.strip() == 'who':
				logging.info(users.gs_users)
				logging.info(users.ordered_user_list)

			elif message.strip() == 'quit' or message.strip() == 'exit':
				disconnect(name)
				userlist[1].close()
				break
			else: 
				broadcast(name, "%s> %s" % (name, message.strip())) 
		except socket.error: 
			continue 

# Set up the server socket. 
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
server.setblocking(False) 
server.bind((HOST, PORT)) 
server.listen(1) 
logging.info("Listening on %s" % ("%s:%s" % server.getsockname())) 
# Main # event # loop.  
while True: 
	try: 
		# Accept new connections. 
		while True: 
			try: 
				conn, addr = server.accept() 
				# limit max users as 3
				if len(users.gs_users) >= MAX_USERS:
					conn.send("I'm sorry that users are already full...\n")
					conn.close()
					break 
			except socket.error: 
				break 
			accept(conn) 

		if not GAME_READY:
			if len(users.gs_users) == MAX_USERS:
				GAME_READY = start_game()


		# From now on, codes are run by server
		# Read from connections. 
		processing_command()
		time.sleep(.1) 
	except (SystemExit, KeyboardInterrupt): 
		break
