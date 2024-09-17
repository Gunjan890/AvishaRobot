from pyrogram import Client, filters
from gtts import gTTS
from AvishaRobot import pbot as app

@app.on_message(filters.command('tts'))
def text_to_speech(client, message):
    text = message.text.split(' ', 1)[1]
    tts = gTTS(text=text, lang='hi')
    tts.save('avisha.mp3')
    client.send_audio(message.chat.id, 'avisha.mp3')
  
__mod_name__ = "ɢᴛᴛs"

__help__ = """

⬤ /tts ➥ hello, how are you today.
"""