import telebot
import requests
import json
import re
from googletrans import Translator
from telebot.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

bot = telebot.TeleBot('111111111:111111111111111111111111') #BotFather
token = 'Token 1111111111111111111111111111111111111111' #F12-Networking 

markup = InlineKeyboardMarkup()
markup.add(InlineKeyboardButton(text='◀️', callback_data=f'back'),(InlineKeyboardButton(text='▶️', callback_data=f'next')))
markup2 = InlineKeyboardMarkup()
markup2.add(InlineKeyboardButton(text='Bully Maid', callback_data=f'bully'),(InlineKeyboardButton(text='Gawr Gura', callback_data=f'gura')))
markup2.add(InlineKeyboardButton(text='Astolfo', callback_data=f'astolfo'),(InlineKeyboardButton(text='Misaki', callback_data=f'misaki')))
markup2.add(InlineKeyboardButton(text='Ульяна', callback_data=f'ulyana'),(InlineKeyboardButton(text='Семён', callback_data=f'semen')))
markup2.add(InlineKeyboardButton(text='БУГУРТ', callback_data=f'bugurt'),(InlineKeyboardButton(text='Человек-анекдот', callback_data=f'anekdot')))
@bot.message_handler(commands=['setbot'])
def start_message(message):
	if current_character=='':
		bot.send_message(message.chat.id,"Персонаж не выбран", reply_markup = markup2)
	else:
		if (current_character=='bully'):
			bot.send_message(message.chat.id,"Текущий персонаж: Bully Maid", reply_markup = markup2)
		elif (current_character=='gura'):
			bot.send_message(message.chat.id,"Текущий персонаж: Gawr Gura", reply_markup = markup2)
		elif (current_character=='astolfo'):
			bot.send_message(message.chat.id,"Текущий персонаж: Astolfo", reply_markup = markup2)
		elif (current_character=='misaki'):
			bot.send_message(message.chat.id,"Текущий персонаж: Misaki", reply_markup = markup2)
		elif (current_character=='ulyana'):
			bot.send_message(message.chat.id,"Текущий персонаж: Ульяна", reply_markup = markup2)
		elif (current_character=='semen'):
			bot.send_message(message.chat.id,"Текущий персонаж: Семён", reply_markup = markup2)
		elif (current_character=='bugurt'):
			bot.send_message(message.chat.id,"Текущий персонаж: Bugurt", reply_markup = markup2)
		elif (current_character=='anekdot'):
			bot.send_message(message.chat.id,"Текущий персонаж: Человек-анекдот", reply_markup = markup2)	
@bot.message_handler(commands=['restart'])
def restart_chat(message):
	restart()
	bot.send_message(message.chat.id,"Чат перезапущен")

@bot.message_handler(commands=['start'])
def restart_chat(message):
	bot.send_message(message.chat.id,"Character AI Telegram Bot v1.0")

def restart():
	global current_tgt
	global current_character_id
	global current_history_id
	try:
		restart_json_data["character_external_id"] = current_character_id
		response_restart = requests.post('https://beta.character.ai/chat/history/create/', headers=update_headers, json=restart_json_data)
		restart_json = json.loads(response_restart.text)
		# current_tgt = restart_json['participants'][1]['user']['username']
		current_history_id = restart_json['external_id']
		print('current_character_id:', current_character_id, ',current_history_id:', current_history_id, ',current_tgt:', current_tgt)
	except Exception as e:
		print('Error: ', e)

arr = []
trs = []
x1 = ''
x2 = ''
x3 = ''
x4 = ''
data = ''
out = ''
final = ''
final2 = ''
final3 = ''
final4 = ''
msg_id = ''
msg_id2 = ''
msg_id3 = ''
msg_id4 = ''
cursor = 1
current_character = ''
current_history_id =''
current_character_id = ''
current_tgt = ''

headers = {
	'authority': 'beta.character.ai',
	'accept': '*/*',
	'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,ja;q=0.6',
	'authorization': '',
	'content-type': 'application/json',
	'dnt': '1',
	'origin': 'https://beta.character.ai',
	# 'referer': 'https://beta.character.ai/chat?char=to2sEAWBxSW8NuGv-XiMWMHhZOlf0bRGn7amKUJjyZw',
	'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
	'sec-ch-ua-mobile': '?0',
	'sec-ch-ua-platform': '"Windows"',
	'sec-fetch-dest': 'empty',
	'sec-fetch-mode': 'cors',
	'sec-fetch-site': 'same-origin',
	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
}

json_data = {
	'history_external_id': '',
	'character_external_id': '',
	'text': '',
	'tgt': '',
	'ranking_method': 'random',
	'staging': False,
	'model_server_address': None,
	'override_prefix': None,
	'override_rank': None,
	'rank_candidates': None,
	'filter_candidates': None,
	'prefix_limit': None,
	'prefix_token_limit': None,
	'livetune_coeff': None,
	'stream_params': None,
	'enable_tti': True,
	'initial_timeout': None,
	'insert_beginning': None,
	'translate_candidates': None,
	'stream_every_n_steps': 16,
	'chunks_to_pad': 8,
	'is_proactive': False,
	'image_rel_path': '',
	'image_description': '',
	'image_description_type': '',
	'image_origin_type': '',
	'voice_enabled': False,
}
update_headers = {
	'authority': 'beta.character.ai',
	'accept': '*/*',
	'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,ja;q=0.6',
	'authorization': '',
	'content-type': 'application/json',
	'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
	'sec-ch-ua-mobile': '?0',
	'sec-ch-ua-platform': '"Windows"',
	'sec-fetch-dest': 'empty',
	'sec-fetch-mode': 'cors',
	'sec-fetch-site': 'same-origin',
	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
}
update_json_data = {
	'message_id': '',
	'reason': 'SWIPE',
}
restart_json_data = {
	'character_external_id': '',
	'override_history_set': 'null'
}
#characters
character_bully_maid = {
	'character_external_id': 'to2sEAWBxSW8NuGv-XiMWMHhZOlf0bRGn7amKUJjyZw',
	'tgt': 'internal_id:126344:0bf4f680-f254-4e11-a74e-c3be586dbc34'
}
character_gawr_gura = {
	'character_external_id': 'oL2IzOD15_wBIP_o6NAWDwiVyAnzz_3aGLu9aU7i254',
	'tgt': 'internal_id:26970:711d0776-02c0-4a30-b37d-5bbf60652d12'
}
character_astolfo = {
	'character_external_id': 'VIqELxEyIJttOJVzR_sYEDCOBq9OHuYBTmaEX97lFLw',
	'tgt': 'internal_id:129747:600f5c44-a5d5-4d26-a51e-838d513e61f6'
}
character_misaki = {
	'character_external_id': 'u3J-RtteHbbUHmFjXFMdIJ5QZO92VI5mjFnoptQJPQA',
	'tgt': 'internal_id:43476d70-6c0b-4f47-9866-91891a596307'
}
character_ulyana = {
	'character_external_id': 'QNo6qEn2GS5BjV4QDR6df0rO94WswrnHh3D4izT64zI',
	'tgt': 'internal_id:40de16be-0d55-499f-9930-6692fceb1d3b'
}
character_semen = {
	'character_external_id': 'F-lnRPcEId9nMSs8_3OQcF-6OxpTTy_zQIqTyzh9gqQ',
	'tgt': 'internal_id:32ecb04b-6f15-4282-98bb-6beb08dd780b'
}
character_bugurt = {
	'character_external_id': 'EwU8IelY2X4S9C5FKm1LN4Owrne6-JyRWljYxRPtHmY',
	'tgt': 'internal_id:e30da4e8-02cb-4d40-92f5-5b4524fc12fa'
}
character_anektod = {
	'character_external_id': 'CSHl-WkyGM6xKXjgjUHUTJ3m9lR-nYK6V8oQXZ_uwNE',
	'tgt': 'internal_id:8cbee070-b74d-4548-8057-2a57f8268c0a'
}
headers["authorization"] = token
update_headers["authorization"] = token

def send_msg():
	try:
		global arr
		global trs
		global x1,x2,x3,x4
		global final,final2,final3,final4
		global msg_id,msg_id2,msg_id3,msg_id4
		global cursor
		global current_character_id
		global current_history_id
		global current_tgt
		json_data['history_external_id'] = current_history_id
		json_data['character_external_id'] = current_character_id
		json_data['tgt'] = current_tgt
		if (current_character_id!='' and current_history_id!='' and current_tgt!=''):
			cursor = 1
			response = requests.post('https://beta.character.ai/chat/streaming/', headers=headers, json=json_data)

			print('Response:', response.status_code)
			f = response.text
			log = open('response.txt', 'w')
			log.write(f)
			log.close()

			for matched in re.findall(r'{\"text\": \"(.*?)}', f):
				arr.append(matched)
			str = '{"text": "' + arr[-1] + '}'
			str2 = '{"text": "' + arr[-2] + '}'
			str3 = '{"text": "' + arr[-3] + '}'
			str4 = '{"text": "' + arr[-4] + '}'
			try:
				data = json.loads(str)
			except Exception as e:
				print("Some error occured while loading json")
			try:	
				data2 = json.loads(str2)
			except Exception as e:
				print("Some error occured while loading json")
			try:
				data3 = json.loads(str3)
			except Exception as e:
				print("Some error occured while loading json")
			try:
				data4 = json.loads(str4)
			except Exception as e:
				print("Some error occured while loading json")
			try:
				final = data['text']
				msg_id = data['id']
			except Exception as e:
				print("Some error occured while parsing json")
			try:
				final2 = data2['text']
				msg_id2 = data2['id']
			except Exception as e:
				print("Some error occured while parsing json")
			try:
				final3 = data3['text']
				msg_id3 = data3['id']
			except Exception as e:
				print("Some error occured while parsing json")
			try:
				final4 = data4['text']
				msg_id4 = data4['id']
			except Exception as e:
				print("Some error occured while parsing json")
			
			# if (msg_id!=''):
			# 	update_json_data["message_id"] = msg_id
		else:
			print('Something empty')
	except Exception as e:
		print("Some another error occured while sending message")
		
def set_character():
	global current_character
	global current_character_id
	global current_tgt
	if current_character=='bully':
		current_character_id = character_bully_maid["character_external_id"]
		current_tgt = character_bully_maid["tgt"]
		restart()
	elif current_character=='gura':
		current_character_id = character_gawr_gura["character_external_id"]
		current_tgt = character_gawr_gura["tgt"]
		restart()
	elif current_character=='astolfo':
		current_character_id = character_astolfo["character_external_id"]
		current_tgt = character_astolfo["tgt"]
		restart()
	elif current_character=='misaki':
		current_character_id = character_misaki["character_external_id"]
		current_tgt = character_misaki["tgt"]
		restart()
	elif current_character=='ulyana':
		current_character_id = character_ulyana["character_external_id"]
		current_tgt = character_ulyana["tgt"]
		restart()
	elif current_character=='semen':
		current_character_id = character_semen["character_external_id"]
		current_tgt = character_semen["tgt"]
		restart()
	elif current_character=='bugurt':
		current_character_id = character_bugurt["character_external_id"]
		current_tgt = character_bugurt["tgt"]
		restart()
	elif current_character=='anekdot':
		current_character_id = character_anektod["character_external_id"]
		current_tgt = character_anektod["tgt"]
		restart()

@bot.callback_query_handler(func=lambda call:True)
def callback_query(call):
	try:
		req = call.data.split('_')
		print('button is pressed')
		global cursor
		global current_character
		current_msg = ''
		if req[0] == 'back' or req[0] == 'next':
			#Обработка кнопки - вперед
			if req[0] == 'back':
						cursor = cursor - 1
						if cursor < 1:
							cursor = 4
						print('back is pressed')
			#Обработка кнопки - назад
			elif req[0] == 'next':
						cursor = cursor + 1
						if cursor > 4:
							cursor = 1
						print('next is pressed')
			if cursor == 1:
				current_msg = final
				update_json_data["message_id"] = msg_id
				response_update = requests.post('https://beta.character.ai/chat/msg/update/primary/', headers=update_headers, json=update_json_data)
				print('Primary:', response_update.text)
				print(msg_id)
			elif cursor == 2:
				current_msg = final2
				update_json_data["message_id"] = msg_id2
				response_update = requests.post('https://beta.character.ai/chat/msg/update/primary/', headers=update_headers, json=update_json_data)
				print('Primary:', response_update.text)
				print(msg_id2)
			elif cursor == 3:
				current_msg = final3
				update_json_data["message_id"] = msg_id3
				response_update = requests.post('https://beta.character.ai/chat/msg/update/primary/', headers=update_headers, json=update_json_data)
				print('Primary:', response_update.text)
				print(msg_id3)
			elif cursor == 4:
				current_msg = final4
				update_json_data["message_id"] = msg_id4
				response_update = requests.post('https://beta.character.ai/chat/msg/update/primary/', headers=update_headers, json=update_json_data)
				print('Primary:', response_update.text)
				print(msg_id4)
			bot.edit_message_text(current_msg, reply_markup = markup, chat_id=call.message.chat.id, message_id=call.message.message_id)
		elif req[0] == 'bully':
			current_character = 'bully'
			set_character()
			bot.send_message(call.message.chat.id, 'Новый персонаж создан. Напиши сообщение.')
		elif req[0] == 'astolfo':
			current_character = 'astolfo'
			set_character()
			bot.send_message(call.message.chat.id, 'Новый персонаж создан. Напиши сообщение.')
		elif req[0] == 'misaki':
			current_character = 'misaki'
			set_character()
			bot.send_message(call.message.chat.id, 'Новый персонаж создан. Напиши сообщение.')
		elif req[0] == 'ulyana':
			current_character = 'ulyana'
			set_character()
			bot.send_message(call.message.chat.id, 'Новый персонаж создан. Напиши сообщение.')
		elif req[0] == 'gura':
			current_character = 'gura'
			set_character()
			bot.send_message(call.message.chat.id, 'Новый персонаж создан. Напиши сообщение.')
		elif req[0] == 'semen':
			current_character = 'semen'
			set_character()
			bot.send_message(call.message.chat.id, 'Новый персонаж создан. Напиши сообщение.')
		elif req[0] == 'bugurt':
			current_character = 'bugurt'
			set_character()
			bot.send_message(call.message.chat.id, 'Новый персонаж создан. Напиши сообщение.')
		elif req[0] == 'anekdot':
			current_character = 'anekdot'
			set_character()
			bot.send_message(call.message.chat.id, 'Новый персонаж создан. Напиши сообщение.')
	except Exception as e:
		print('Error while swiping: ', e)

@bot.message_handler(content_types=["text"])
def handle_text(message):
	try:
		global json_data
		global x1,x2,x3,x4
		global out
		json_data["text"] = message.text
		print('Message: ', message.text)
		if current_character=='':
			bot.send_message(message.chat.id,'Выберите персонажа', reply_markup = markup2)
		else:
			send_msg()
			try:
				bot.send_message(message.chat.id,final, reply_markup = markup)
			except Exception as e:
				print("Some error occured while sending message: ", e)
	except Exception as e:
		print("Some error occured while sending message: ", e)

bot.polling(none_stop=True, interval=0, timeout=600)

