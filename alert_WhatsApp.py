from datetime import datetime
from time import sleep, strftime

from twilio.rest import Client

# Your Account Sid and Auth Token
account_sid = '######'
auth_token = '#######'
client = Client(account_sid, auth_token)

def envia_notificacao(a, s):
    message = client.messages.create(
        body='*ALERTA:* bla bla bla.... Agora é {}, o programa será encerrado em {} segundos!'.format(a, s),
        from_='whatsapp:+14155238886',
        to='whatsapp:+555184373078'
    )
    print(message.sid)

def alerta_15(second_stop):
    print('ATENÇÃO: Faltam {} segundos encerrar!'.format(int(second_stop) - int(datetime.now().second)))

print('Start Project: {}h\n'.format(strftime("%H:%M:%S")))

hour_stop = input('Hour you want to stop the program (Ex.: 15): ')
minute_stop = input('Minute you want to stop the program (Ex.: 47): ')
second_stop = input('Second you want to stop the program (Ex.: 00): ')
stop_program = hour_stop + ':' + minute_stop + ':' + second_stop

print('\nStop Program at: {}h'.format(stop_program))

print('\nExact time for now: {}h'.format(strftime("%H:%M:%S")))

print('\nStart of monitoring time...')

while True:
    print(strftime("%H:%M:%S"))
    sleep(1)
    if (int(hour_stop) - int(datetime.now().hour)) == 0 and (int(minute_stop) - int(datetime.now().minute)) == 0 and (int(second_stop) - int(datetime.now().second)) == int(15):
        alerta_15(second_stop)
        envia_notificacao(strftime("%H:%M:%S"), int(second_stop) - int(datetime.now().second))
    if strftime("%H:%M:%S") == stop_program:
        print('END...\nClosing Program... Now is {}h.'.format(stop_program))
        break
