##############################################
# Copyright Theodore Chiu 2021
# theochiu.me@gmail.com 
# West Campus Best Campus!
##############################################

import requests
import time
import random
import string

# groupme access token (api access)
token = r'06lbAWJcU77H9lyCNVSSuVQfpzl4GVx32880yGAr'

# we'll use this later
announcements_groupid = r'69765237'

# constants specific to bot testing chat
groupid = r'70744704'
bot_id = r'6cce054c14e89aeea59b2315b9'

def send(endpoint, data):
	response = requests.post(endpoint, json=data, verify=False)
	return response

def send_message(message):
	
	data = {
		"bot_id": bot_id,
		"text": message
	}
	send("https://api.groupme.com/v3/bots/post", data)


def get_message():
	# gets most recent message
	response = requests.get("https://api.groupme.com/v3/groups/" + groupid + "/messages?token=" + token)
	print(response.json())

	m_time = response.json()["response"]["messages"][0]["created_at"]
	message = response.json()["response"]["messages"][0]["text"]
	sender = response.json()["response"]["messages"][0]["id"]

	return m_time, message, sender

def dm(sender, message):
	rand_string = "".join(random.choice(string.ascii_lowercase) for i in range(10))
	data = {
		"direct_message": {
			"source_guid": rand_string,
			"recipient_id": sender,
			"text": message,
		}
	}

	response = send("https://api.groupme.com/v3/direct_messages?token=" + token, data)
	print(response.text)

def main():
	m_time, message, sender = get_message()

	# get unix time
	tic = int(time.time())

	elapsed = (tic - m_time) / 60

	if elapsed <= 5 and "#announcement" not in message:
		dm(sender, "Hello, my name is Jarvis")

if __name__ == '__main__':
	main()
