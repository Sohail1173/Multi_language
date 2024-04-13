import speech_recognition as sr
import google.generativeai as genai
from dotenv import load_dotenv
import os
from gtts import gTTS

print("perfect!!")
load_dotenv()
GOOGLE_API_KEY=os.getenv("GOOGLE_API_KEY")
os.environ["GOOGLE_API_KEY"]=GOOGLE_API_KEY


def voice_input():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        audio=r.listen(source)
    try:
        text=r.recognise_google(audio)
        print("you said:",text)
        return text
    except sr.UnknownValueError:
        print("sorry,could not understand the audio")
    except sr.RequestError as e:
        print("could not request result from google speech recognition service:{0}".format(e))
# print(voice_input())

def text_to_speech(text):
    tts=gTTS(text=text,lang="eng")
    tts.save("speech.mp3")
def llm_model_object(user_text):
    genai.configure(api_key=GOOGLE_API_KEY)
    model=genai.GenerateModel("gemini-pro")
    response=model.generate_content(user_text)
    result=response.text
    return result

if __name__ == "__main__":
    text=voice_input()
    text_to_speech(text)
    result=llm_model_object(text)
    print(result)