from lib import tts_file_create as tfc
from lib import chatbot
from lib import gamebot
import minecraft_launcher_lib as mll

def startGame(gameName: str):
    tfc.create("I will play now")
    tfc.say()
    gamebot.game(gameName)