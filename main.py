from cProfile import run
from playsound import playsound
from gtts import gTTS
import speech_recognition as sr
import os
import time
from datetime import date, datetime
import random
from random import choice
from pydub import AudioSegment
import webbrowser

r = sr.Recognizer()


# def speeding():
#     in_path = 'answer.mp3'
#     ex_path = 'speed.mp3'
#     sound = AudioSegment.from_file(in_path)
#     slower_sound = speed_swifter(sound, 1.3)
#     slower_sound.export(ex_path, format="mp3")

# def speed_swifter(sound, speed=1.0):
#     sound_with_altered_frame_rate = sound._spawn(sound.raw_data, overrides={"frame_rate": int(sound.frame_rate * speed)})
#     return sound_with_altered_frame_rate


def record(ask=False):
    with sr.Microphone() as source:
        if ask:
            print(ask)
        audio = r.listen(source)
        voice = ""
        try:
            voice = r.recognize_google(audio, language="tr-TR")
        except sr.UnknownValueError:
            print("Asistan: Anlayamadım")
        except sr.RequestError:
            print("Asistan: Sistem çalışmıyor")
        return voice


def response(voice):
    if "merhaba" in voice:
        speak("sana da merhaba genç")
    if "selam" in voice:
        speak("sana 2 kere selam olsun")
    if "teşekkür ederim" in voice or "teşekkürler" in voice:
        speak("rica ederim")
    if "görüşürüz" in voice:
        speak("görüşürüz canım")
        exit()

    if "hangi gündeyiz" in voice:
        today = time.strftime("%A")
        today.capitalize()
        if today == "Monday":
            today = "Pazartesi"

        elif today == "Tuesday":
            today = "Salı"

        elif today == "Wednesday":
            today = "Çarşamba"

        elif today == "Thursday":
            today = "Perşembe"

        elif today == "Friday":
            today = "Cuma"

        elif today == "Saturday":
            today = "Cumartesi"

        elif today == "Sunday":
            today = "Pazar"

        speak(today)

    if "saat kaç" in voice:
        selection = ["Saat şu an: ", "Hemen bakıyorum: "]
        clock = datetime.now().strftime("%H:%M")
        selection = random.choice(selection)
        speak(selection + clock)

    if "google'da ara" in voice:
        speak("Ne aramamı istersin?")
        search = record()
        url = "https://www.google.com/search?q={}".format(search)
        webbrowser.get().open(url)
        speak("{} içi Google'da bulabildiklerimi listeliyorum.".format(search))

    if "uygulama aç" in voice:
        speak("Hangi uygulamayı açmamı istiyorsun?")
        runApp = record()
        runApp = runApp.lower()
        if "valorant" in runApp:
            os.startfile("D:\Riot Games\Riot Client\RiotClientServices.exe")
            speak("İstediğin uygulamayı çalıştırıyorum.")
        elif "life is strange" in runApp:
            os.startfile("steam://rungameid/319630")
            speak("İstediğin uygulamayı çalıştırıyorum.")
        else:
            speak("İstediğin uygulama çalıştırma listemde yok.")

def speak(string):
    tts = gTTS(text=string, lang="tr", slow=False)
    file = "answer.mp3"
    tts.save(file)
    # speeding()
    playsound(file)
    os.remove(file)
    # os.remove("speed.mp3")

def test(wake):
    if "charlie" in wake:
        playsound("DING.mp3")
        wake = record()
        if wake != '':
            voice = wake.lower()
            print(wake.capitalize())
            response(voice)


# speak("Selam madenci")
playsound("DING.mp3")

while True:
    wake = record()
    if wake != '':
        wake = wake.lower()
        print(wake.capitalize())
        test(wake)