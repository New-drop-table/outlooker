import requests
    
token = "6931652129:AAEjipnLIJI3t_bA3pezCnkxUCE52RbbqL0"    

response = requests.post(
        url='https://api.telegram.org/bot{0}/{1}'.format(token, "sendMessage"),
        data={'chat_id': 1215459744, 'text': 'hello friend'}
    ).json()