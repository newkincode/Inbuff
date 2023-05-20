from lib import chatbot
from lib import gamebot

def read_result_from_file():
    with open('result.txt', 'r') as file:
        result = file.read()
    return result

# main.py에서 결과 파일을 읽어옴
result = read_result_from_file()
print(result)
