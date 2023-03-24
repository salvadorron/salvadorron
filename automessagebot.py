import asyncio
import time
import requests
import telegram

# configure details from chat id and telegram bot

bot_token = '5715000920:AAFTrx_erER612yrXS-96CUGDZfMgxI70tY'
bot_chatID = '1316829775'
bot = telegram.Bot(token=bot_token)

async def sendMessage(msg):
	await bot.send_message(chat_id=bot_chatID, text=msg)

# define a list of urls to check

urls = ['https://example.com','https://www.google.com','https://www.facebook.com']


while True:
	try:
		for url in urls:
			#send a request to url
			response = requests.get(url)
			
			# if response isn't succesfully (http status code 200), send message to telegram
			if response.status_code != 200:
				message = f'La URL {url} no esta disponible'
				asyncio.run(sendMessage(message))
				print(f'Se ha enviado un mensaje de telegram debido a una falla en la URL {url}.')
				
			#wait 30 seconds to send another message
			time.sleep(30)
		
	except:
		print('No se pudo obtener acceso a la pagina')
	finally:
		#wait 05 minutes before checking urls again
		time.sleep(300)





