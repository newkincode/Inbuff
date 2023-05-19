import socket
import re
from dotenv import load_dotenv
import os 

# load .env
load_dotenv()

token1 = os.environ.get('token')
print(token1)
def read_twitch_chat(channel):
    global token1
    server = 'irc.chat.twitch.tv'
    port = 6667
    token = token1
    nickname = channel

    irc = socket.socket()
    irc.connect((server, port))
    irc.send(f'PASS {token}\n'.encode('utf-8'))
    irc.send(f'NICK {nickname}\n'.encode('utf-8'))
    irc.send(f'JOIN #{channel}\n'.encode('utf-8'))

    chat_regex = re.compile(r'^:\w+!\w+@\w+\.tmi\.twitch\.tv PRIVMSG #\w+ :')

    while True:
        response = irc.recv(2048).decode('utf-8')
        if response.startswith('PING'):
            irc.send('PONG\n'.encode('utf-8'))
        else:
            username = re.search(r'\w+', response).group(0)
            message = chat_regex.sub('', response)
            print(f'{username}: {message}')

# 트위치 채널 이름을 지정하여 호출합니다.
read_twitch_chat('nkc1006')