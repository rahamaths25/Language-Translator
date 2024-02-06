import speech_recognition as sr
from google_trans_new import google_translator


r = sr.Recognizer()
translator=google_translator()
with sr.Microphone() as source:
    print("speak now")
    audio=r.listen(source)
    try:
         speech_text=r.recognize_google(audio)
         print(speech_text)
    except sr.UnknownValueError:
        print("Could not understand")
    except sr.RequestError:
        print("Could not request result")

translated_text=translator.translate(speech_text,lang_tgt='fr:French')
print(translated_text)