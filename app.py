##############################################
# Copyright Theodore Chiu 2021
# theochiu.me@gmail.com 
# West Campus Best Campus!
##############################################

import requests
from datetime import datetime

# groupme access token (api access)
token = r'06lbAWJcU77H9lyCNVSSuVQfpzl4GVx32880yGAr'

announcements_groupid = r'69765237'

# bot testing chat
groupid = r'70744704'

bot_id = r'6cce054c14e89aeea59b2315b9'

def send(endpoint, data):
	response = requests.post(endpoint, json=data, verify=False)
	# print(response.json())
	return response

def send_message(message):
	data = {
		"bot_id": bot_id,
		"text": message
	}
	send("https://api.groupme.com/v3/bots/post", data)

send_message("Jarvis test! #2")


# tick = datetime.now()

# print(tick)







