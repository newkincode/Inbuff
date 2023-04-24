from langdetect import detect
import gtts
import os
import shutil

def recreate_folder(path): # by chatGPT
    # 경로에 폴더가 없으면 폴더 생성
    if not os.path.exists(path):
        os.makedirs(path)
    # 경로에 폴더가 이미 존재하면 폴더 삭제 후 다시 생성
    else:
        shutil.rmtree(path)
        os.makedirs(path)

def create(text: str):
    texts = list(text.split())
    count = 0
    recreate_folder("ttsfile")
    for i in texts:
        count+=1
        gtts.gTTS(i, detect(i)).save(f"ttsfile/{count}.mp3")

gtts.gTTS("안녕", "ko").save(f"ttsfile/test.mp3")