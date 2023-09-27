import speech_recognition as sr
import pyttsx3
import pywhatkit
import urllib.request
import json
import datetime
import wikipedia

name = 'cortana'
key = 'AIzaSyAeH-LPVPMhD_SG-lInnJ8ukPPsv0IHp9U'
listener = sr.Recognizer()

engine = pyttsx3.init()

voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('voice', voices[0].id)

# for voice in voices:
#     print(voice)


def talk(text):
    engine.say(text)
    engine.runAndWait()


engine.say('Buenos días')
engine.runAndWait()


def listen():
    try:
        with sr.Microphone() as source:
            print('Escuchando...')
            voice = listener.listen(source)
            rec = listener.recognize_google(voice)
            rec = rec.lower()
            if name in rec:
                # talk(rec)
                rec = rec.replace(name, '')
                print(rec)
    except:
        pass
    return rec


def run():
    rec = listen()
    if 'play' in rec:
        music = rec.replace('play', '')
        talk('Playing '+music)
        pywhatkit.playonyt(music)
    elif 'cuantos suscriptores tiene' in rec:
        name_subs = rec.replace('cuantos suscriptores tiene', '').strip()
        data = urllib.request.urlopen(
            "https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername=" +
            name_subs + '&key=' + key
        ).read()
        subs = json.loads(data)["items"][0]['statistics']['subscribeCount']
        talk(name_subs + " tiene {:,d}".format(int(subs))+' suscriptores!')

    elif 'hora' in rec:
        hora = datetime.datetime().now().strftime('%H:%M')
        talk("Son las "+hora)
    elif 'busca' in rec:
        order = rec.replace('busca', '')
        info = wikipedia.summary(order, 1)
        talk(info)
    else:
        talk("Vuelve a intentarlo")


while true:
    run()
