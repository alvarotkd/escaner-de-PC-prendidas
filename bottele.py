import requests

def telegram_bot_sendtext(bot_message):
    
    bot_token = '5237828344:AAFB9Whbwa5ZEzd8cPlNZhLkxSK_KnpVYI8'
    bot_chatID = '762005398'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()
    

