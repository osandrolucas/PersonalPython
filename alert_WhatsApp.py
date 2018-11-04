import time
from datetime import datetime
from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'AC01b4a24a759e05f75c0a100c03663d7f'
auth_token = 'a4ddc80414cd93d0e241e1baf19ea609'
client = Client(account_sid, auth_token)

def envia_notificacao(a, s):
    message = client.messages.create(
        body='*ALERTA:* bla bla bla.... Agora é {}, programa será encerrado em {} segundos!'.format(a, s),
        from_='whatsapp:+14155238886',
        to='whatsapp:+555184373078'
    )
    print(message.sid)

def alerta_15(second_stop):
    print('ATENÇÃO: Faltam {} segundos encerrar!'.format(int(second_stop) - int(datetime.now().second)))

print('Page of tests')

print('Start Project: {}h\n'.format(time.strftime("%H:%M:%S")))

hour_stop = input('Hour you want to stop the program (Ex.: 15): ')
minute_stop = input('Minute you want to stop the program (Ex.: 47): ')
second_stop = input('Second you want to stop the program (Ex.: 00): ')
stop_program = hour_stop + ':' + minute_stop + ':' + second_stop

print('\nStop Program at: {}h'.format(stop_program))

print('\nExact time for now: {}h'.format(time.strftime("%H:%M:%S")))

print('\nStart of monitoring time...')

while True:
    print(time.strftime("%H:%M:%S"))
    time.sleep(1)
    if (int(hour_stop) - int(datetime.now().hour)) == 0 and (int(minute_stop) - int(datetime.now().minute)) == 0 and (int(second_stop) - int(datetime.now().second)) == int(15):
        alerta_15(second_stop)
        envia_notificacao(time.strftime("%H:%M:%S"), int(second_stop) - int(datetime.now().second))
    if time.strftime("%H:%M:%S") == stop_program:
        print('END...\nClosing Program... Now is {}h.'.format(stop_program))
        break
