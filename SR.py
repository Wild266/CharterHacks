import speech_recognition as sr
import azure.cognitiveservices.speech as speechsdk
import spacy
from spacy.matcher import Matcher
from nlpmethods import *

from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import twitter_samples, stopwords
from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize
from nltk import FreqDist, classify, NaiveBayesClassifier

import re, string, random
from sentiments import *
nlp = spacy.load('en_core_web_sm')
print("type ctrl c to stop")

transcript = []



classifier = g()
   




#converts speech to text
def listen():
   r = sr.Recognizer()
   mic = sr.Microphone(device_index=0)
   with mic as source:
       audio = r.listen(source)
   text = r.recognize_google(audio)
   print(text)
   return text

# import pyttsx
# engine = pyttsx.init()
# engine.say('Good morning.')
# engine.runAndWait()
#
# import win32com.client as wincl
# speak = wincl.Dispatch("SAPI.SpVoice")
# speak.Speak(text)
# 
# from tts_watson.TtsWatson import TtsWatson
# 
# ttsWatson = TtsWatson('watson_user', 'watson_password', 'en-US_AllisonVoice') 
# ttsWatson.play(text)

#converts response to speech
def talk(text):
   speech_key, service_region = "", "eastus"
   speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
   
   speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)
   
   result = speech_synthesizer.speak_text_async(text).get()
   
   # Checks result.
   if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
       print("Speech synthesized to speaker for text [{}]".format(text))
   elif result.reason == speechsdk.ResultReason.Canceled:
       cancellation_details = result.cancellation_details
       print("Speech synthesis canceled: {}".format(cancellation_details.reason))
       if cancellation_details.reason == speechsdk.CancellationReason.Error:
           if cancellation_details.error_details:
               print("Error details: {}".format(cancellation_details.error_details))
       print("Did you update the subscription info?")
       
       
       
       
#main chatbot loop       
print("Hello! I'm SARA")
while True:
   text = (listen())
   transcript.append(text)
   matcher = Matcher(nlp.vocab)
   doc = nlp(text)
#    print(sanalysis(text, classifier))
#    print("full name", extract_full_name(doc))
#    print("base", give_base(doc))
#    print("subjects", give_subjects(doc))
#    print("direct objects", give_directobj(doc))
#    print("root", give_ROOT(doc))
#    print("noun chunks", give_nounchunks(doc))
#    print("named entities", give_namedentities(doc))
   talk(respond(text, transcript, sanalysis(text, classifier)))
