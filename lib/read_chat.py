import socket
import re
from dotenv import load_dotenv
import os
import chatbot

a = 0

# .env 파일 로드
load_dotenv()

token1 = os.environ.get('token')
print(token1)

def send_to_main(result):
    with open('result.txt', 'w') as file:
        file.write(result)

def read_twitch_chat(channel):
    global token1
    global a

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
            a = f'{username}: {message}'

            # a를 chatbot.process에 전달하고 결과를 main.py로 전송합니다.
            result = chatbot.process(a)
            result = chatbot.detect(result)
            send_to_main(result)
            print(result)

# 원하는 채널 이름으로 read_twitch_chat 함수를 호출합니다.
read_twitch_chat('nkc1006')