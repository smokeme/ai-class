pip install openai pydub speechrecognition pyttsx3  --user
https://pypi.org/project/PyAudio/0.2.12/#files
pip install openai==0.28


```
import openai
import speech_recognition as sr
import pyttsx3
import requests

# Set up OpenAI API key
openai_api_key = ''

# Initialize the recognizer and text-to-speech engine
recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()

# Function to capture audio from the microphone and convert it to text
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print(f"Recognized: {text}")
            return text
        except sr.UnknownValueError:
            print("Could not understand the audio")
            return ""
        except sr.RequestError:
            print("Could not request results; check your network connection")
            return ""

# Function to generate text using OpenAI GPT
def generate_text(prompt):
    url = "https://api.openai.com/v1/chat/completions"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {openai_api_key}"
    }

    data = {
        "model": "gpt-4o",
        "messages": [
            {
                "role": "system",
                "content": "Your name is Skynet, you are an AI designed to reply to users, we are capturing audio from the user's microphone and converting it into text and sending the response to you, always make answers short"
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    }

    response = requests.post(url, headers=headers, json=data)
    return response.json()['choices'][0]['message']['content']

# Function to convert text to speech
def speak(text):
    tts_engine.say(text)
    tts_engine.runAndWait()

def main():
    while True:
        user_input = listen()
        if user_input:
            response = generate_text(user_input)
            print(f"Response: {response}")
            speak(response)

if __name__ == "__main__":
    main()


```
