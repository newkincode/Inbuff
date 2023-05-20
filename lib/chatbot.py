import json
# 프로세스 함수
def process(text):
    result = text
    print(result)
    return result

# 욕설 감지
def detect(text):
    # 욕설 사전을 불러옵니다.
    with open('profanity_list.json', 'r') as file:
        data = json.load(file)

    swear_words = []
    for key, value in data.items():
        if "excludes" in value:
            swear_words.extend(value["excludes"])
        if "words" in value:
            swear_words.extend(value["words"])
    result = text
    if result in swear_words:
        result = "필터링됨"
    return result