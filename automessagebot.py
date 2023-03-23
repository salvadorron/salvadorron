import time
import requests

# configure details from chat id and telegram bot

bot_token = '5715000920:AAFTrx_erER612yrXS-96CUGDZfMgxI70tY'
bot_chatID = '1316829775'
api_URL = f'https://api.telegram.org/bot{bot_token}/sendMessage'

# define a list to checkout urls

#urls = ['https://example.com','https://www.google.com','https://www.facebook.com']
urls = ['http://localhost:4000/shapes']


while True:
	try:
		for url in urls:
			#send a request to url
			response = requests.get(url)
			
			# if response isn't succesfully (http status code 200), send message to telegram
			if response.status_code != 200:
				message = f'La URL {url} no esta disponible'
				requests.post(api_URL, json={'chat_id': bot_chatID, 'text': message})
				print(f'Se ha enviado un mensaje de telegram debido a una falla en la URL {url}.')
				
			#waiting for 30 seconds before to resend another message
			time.sleep(30)
		
	except:
		print('No se pudo obtener acceso a la pagina')
	finally:
		#waiting 05 minutes before checkout to URLs again
		time.sleep(300)



