#python package supporting common text to speech engines
import pyttsx3
  
#for understanding speech 
import speech_recognition as sr

#for fetching the answers to computational queries
import wolframalpha

#for fetching wikipedia articles
import wikipedia 

#function to searh the query that is either entered or apoken by the user

def search(query):
    try:
        app_id = "your wolframalpha app ID here"
        client = wolframalpha.Client(app_id)
        res = client.query(query)
        answer = next(res.results).text
        print(answer)
        SpeakText('your answer is' + answer)
    #if the query cannot be satisfied by using wolframalpha then it is searched in wikipedia
    except:

        query = query.split(' ')
        query = " ".join(query[0:])
        SpeakText("i am searching for" + query)

        print(wikipedia.summary(query, sentences= 3))
        
        SpeakText(wikipedia.summary(query,sentences = 3))

#funtion to convert text to speech

def SpeakText(command):
    #initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

#Driver's code
r = sr.Recognizer()
#uses the default in microphone as the source to record voice
with sr.Microphone() as source:
    print('say something')

    #reduces the background disturbances and noise for two seconds
    r.adjust_for_ambient_noise(source, 2)

    #listening to source
    audio = r.listen(source)



try:
    speech = r.recognize_google(audio)
    search(speech)
except sr.UnknownValueError:
    print ("google speech recognition did not understand that")

except sr.RequestError as e:
    print('could not request results from google \
        speech recognition service; {0}'.format(e))
else:
    print('run program again')



