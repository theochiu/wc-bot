##############################################
# Copyright Theodore Chiu 2021
# theochiu.me@gmail.com 
# West Campus Best Campus!
##############################################

import requests
import time
import random
import string 
import datetime

# silence stupid warnings
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# groupme access token (api access)
token = r'06lbAWJcU77H9lyCNVSSuVQfpzl4GVx32880yGAr'
processed = []

# we'll use this later
announcements_groupid = r'69765237'

# constants specific to bot testing chat
groupid = r'70744704'
bot_id = r'6cce054c14e89aeea59b2315b9'
start_time = int(time.time())

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
	while response.status_code != 200:			# request until valid
		response = requests.get("https://api.groupme.com/v3/groups/" + groupid + "/messages?token=" + token)

	
	m_time = response.json()["response"]["messages"][0]["created_at"]
	message = response.json()["response"]["messages"][0]["text"]
	sender = response.json()["response"]["messages"][0]["sender_id"]
	m_id = response.json()["response"]["messages"][0]["id"]
	name = response.json()["response"]["messages"][0]["name"]

	return m_time, message, sender, m_id, name

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

def main():
	global processed
	m_time, message, sender, m_id, name = get_message()

	if m_id not in processed:
		print("\nnew message: \n{}: {}".format(name, message))
		processed.append(m_id)

	# get unix time
	tic = int(time.time())

	elapsed = (tic - m_time) / 60

	if elapsed <= 5 and "#announcement" not in message and m_id not in processed and m_time > start_time and sender != "system":
		print("violation detected: sending DM to {}".format(name))
		dm(sender, "This is an automated response. Are you sure that was an announcement? Include #announcement in the future. If the message was sent in the wrong chat by mistake, kindly delete it")
		processed.append(m_id)
		if (len(processed) > 100):
			processed = processed[50:]

if __name__ == '__main__':
	print("Jarvis is running\n")
	while(1):
		main()	
