import json
from korcen import korcen

# 프로세스 함수
def process(text):
    result = text
    print(result)
    return result

# 욕설 감지
def detect(text):
    if korcen.check(text):
        result = "filter"
    else:
        result = text
    return result