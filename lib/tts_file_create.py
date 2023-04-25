from langdetect import detect
import gtts
import os
import shutil
import playsound


def recreate_folder(path): # by chatGPT
    # 경로에 폴더가 없으면 폴더 생성
    if not os.path.exists(path):
        os.makedirs(path)
    # 경로에 폴더가 이미 존재하면 폴더 삭제 후 다시 생성
    else:
        shutil.rmtree(path)
        os.makedirs(path)

def create(text: str):
    recreate_folder("ttsfile")
    gtts.gTTS(text, "us").save(f"ttsfile/text.mp3")
def say():
    playsound.playsound('ttsfile/text.mp3')