#!/usr/bin/env python

import logging

import users

log_format = '{%(pathname)s:%(lineno)d} %(levelname)s:%(message)s'
logging.basicConfig(format=log_format, level=logging.DEBUG)



# return: 
#	success: int(msg_list[1])
#	fail:	 -1 (out of range)
#			 -2 (not number)

def check_message_syntax(msg_list, str_max_num='6', player_name=''):
	logging.debug(msg_list)
#	logging.debug(str_max_num)
	logging.debug(msg_list[0])
	if msg_list[0][0:4] == 'pick':
		logging.debug(str_max_num)
		if len(msg_list[1]) != 1:
			return -1
		elif ord('1') <= ord(msg_list[1]) <= ord(str_max_num):
			return int(msg_list[1])
		else:
			return -1
	elif msg_list[0][0:4] == 'play':
		try:
			chosen_num = int(msg_list[1])
		except ValueError:
			return -2
		users_card_num = len(users.gs_users[player_name][2])
		if chosen_num <= users_card_num:
			return chosen_num
		else:
			return -1

	return False

def check_on_time(msg_list, users):
	if msg_list[0][0:4] == 'pick':
		for name, user_info in users.items():
			if user_info[7] != -1:
				return False

	return True
	

if __name__ == '__main__':
	print check_message_syntax('pick 3')
	print check_message_syntax('pick 9')
	print check_message_syntax('pick 31')

	users.test_init()
	print check_on_time('pick 3', users.gs_users)
