import subprocess
import pyttsx3
import json
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import winshell
import pyjokes
import smtplib
import ctypes
import time
import shutil
from twilio.rest import Client
from clint.textui import progress
from ecapture import ecapture as ec
from urllib.request import urlopen
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    assname = ("your medbuddy!")
    speak("I am your Assistant")
    speak(assname)


def username():
    speak("What should i call you!")
    uname = takeCommand()
    speak("Welcome My friend")
    speak(uname)
    columns = shutil.get_terminal_size().columns

    print("#####################".center(columns))
    print("Welcome Friend", uname.center(columns))
    print("#####################".center(columns))

    speak("How can i Help you, my friend")
   


def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Unable to Recognize your voice.")
        speak("Unable to Recognize your voice.")
        return "None"

    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()

    # Enable low security in gmail
    server.login('your email id', 'your email password')
    server.sendmail('your email id', to, content)
    server.close()
# Define a function to collect user data
def collect_user_data():
    speak("Let's start by collecting some information about your health.")
    speak("What is your age?")
    age =int  (takeCommand())
    
    speak("What is your gender?")
    gender = str (takeCommand())
    
    speak("Do you have any existing health conditions or medical history?")
    medical_history =str (takeCommand())
    
    return {"age": age, "gender": gender, "medical_history": medical_history}
# Define a function to recommend food based on user's health data
def recommend_food(health_data):
    age = health_data.get('age', None)
    gender = health_data.get('gender', None)
    medical_history = health_data.get('medical_history', None)
    fitness_level = health_data.get('fitness_level', None)
    health_goals = health_data.get('health_goals', [])

    recommended_food = []

    if age is None or gender is None or medical_history is None:
        speak ("Unable to recommend food without complete health data.")
        return "Unable to recommend food without complete health data."

    # Age-based food recommendations
    if age < 30:
        recommended_food.append(["Lean proteins (chicken, fish)", "Leafy greens", "Whole grains"])
    elif 30 <= age < 50:
        recommended_food.append(["Nuts and seeds", "Avocado", "Berries"])
    else:
        recommended_food.append(["Calcium-rich foods (milk, yogurt)", "Salmon", "Olive oil"])

    # Gender-based food recommendations
    if gender == 'male':
        recommended_food.append("Lean red meat (in moderation)")
    elif gender == 'female':
        recommended_food.append("Iron-rich foods (spinach, lentils)")
    elif gender == "other" or gender == "trans gender" :  
        recommended_food.append("Iron-rich foods (spinach, lentils), Lean red meat (in moderation)")

    # Medical history-based food recommendations
    if "diabetes" in medical_history:
        recommended_food.append("Low glycemic index foods (sweet potatoes, quinoa)")
    if "high cholesterol" in medical_history:
        recommended_food.append("Oatmeal")
    if "hypertension" in medical_history:
        recommended_food.append("Potassium-rich foods (bananas, oranges)")

   
    

    return recommended_food
    # Add logic to recommend food based on user's health data
    return "Here are some healthy food recommendations for you: ..."
# Define a function to recommend exercise based on user's health data
def recommend_exercise(health_data):
    age = health_data.get('age', None)
    gender = health_data.get('gender', None)
    medical_history = health_data.get('medical_history', None)

    # Logic to recommend exercises based on age, gender, and medical history
    if age is None or gender is None:
        return "Unable to recommend exercises without complete health data."

    recommended_exercises = []

    if age < 40:
        recommended_exercises.append("Walking")
        recommended_exercises.append("Cycling")
    elif age >= 40:
        recommended_exercises.append("Swimming")
        recommended_exercises.append("Yoga")

    if "heart condition" in medical_history:
        recommended_exercises.append("Low-impact aerobics")
        
    if "heart condition" in medical_history:
        recommended_exercises.append("Low-impact aerobics")
    if "joint pain" in medical_history:
        recommended_exercises.append("Swimming")    
        
    if "sugar" in medical_history:
        recommended_exercises.append("1. Walking 2. Yoga 3. Swimming 4. Dancing 5. Bicycling")
    if "cancer" in medical_history:
        speak("just check the stage of the cancer.")
    elif "cancer" or "cancer stage 1" in medical_history:
        speak ("if you have cancer first stage. then you can follow these exercises.")    
        recommended_exercises.append("Aerobic Exercise like :walking, jogging, or cycling. These help strengthen the heart and lungs. Aim for 150-300 minutes of moderate-intensity aerobic activity each week or 75-150 minutes of vigorous-intensity activity Strength Training: Include resistance training exercises at least 2 days per week. These can involve lifting weights or using resistance bands to build and maintain muscle strength . Regularly perform stretching exercises at least 2 days each week. Stretching helps maintain flexibility and range of motion")
        speak ("note: only exercise will not cure the cancer . you must do consult with doctor.")
    elif "cancer stage 2" or "cancer stage 3" in medical_history:
    
        speak("if you have cancer stage 2 or stage 3 you must consult with the doctor who is expert in cancer treatement.")
    else :
        speak("i can't able to understand just tell me once.")     

           
    return recommended_exercises
     
    # Add logic to recommend exercise based on user's health data
    return "Here are some exercise recommendations for you: ..."



if __name__ == '__main__':
    clear = lambda: os.system('cls')

    # This Function will clean any
    # command before execution of this python file
    clear()
    wishMe()
    username()

    while True:

        query = takeCommand().lower()

        # All the commands said by user will be
        # stored here in 'query' and will be
        # converted to lower case for easily
        # recognition of command
        if "yes" in query or "yeah"in query:
            user_data = collect_user_data()
            speak("Thank you for providing your information.")
        elif "hi!" in query or "hello !" in query :
            speak("hello ! how can i asist you ?")
        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query,5)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif "allergy"  or "allergic reacctions" in query:
            speak("Allergy symptoms, which depend on the substance involved, can affect your airways, sinuses and nasal passages, skin, and digestive system. Allergic reactions can range from mild to severe. In some severe cases, allergies can trigger a life-threatening reaction known as anaphylaxis and causes are Sneezing,Itching of the nose, eyes or roof of the mouth ,Runny, stuffy nose,Watery, red or swollen eyes (conjunctivitis) and other  food allergy can cause:Tingling in the mouth,Swelling of the lips, tongue, face or throat,Hives,Anaphylaxis.")
            print("Allergy symptoms, which depend on the substance involved, can affect your airways, sinuses and nasal passages, skin, and digestive system. Allergic reactions can range from mild to severe. In some severe cases, allergies can trigger a life-threatening reaction known as anaphylaxis and causes are Sneezing,Itching of the nose, eyes or roof of the mouth ,Runny, stuffy nose,Watery, red or swollen eyes (conjunctivitis) and other  food allergy can cause:Tingling in the mouth,Swelling of the lips, tongue, face or throat,Hives,Anaphylaxis .")
            speak("i hope It is easy to understand")
            speak(" do you want any other information?")
        elif "pink eye" or "madras eye"or"conjunctivitis" in query:
            speak("Conjunctivitis, commonly known as pink eye, is inflammation of the eye's outer layer, causing redness, pain, and itchiness. It can be viral or allergic. Viral conjunctivitis, often linked with upper respiratory infections, presents with watery discharge and may spread between eyes. Allergic conjunctivitis results from allergens, leading to redness, swelling, itching, and increased tear production.")
            print("Conjunctivitis, commonly known as pink eye, is inflammation of the eye's outer layer, causing redness, pain, and itchiness. It can be viral or allergic. Viral conjunctivitis, often linked with upper respiratory infections, presents with watery discharge and may spread between eyes. Allergic conjunctivitis results from allergens, leading to redness, swelling, itching, and increased tear production.")
            speak("i hope It is easy to understand")
            speak(" do you want any other information?")
        elif "diarrhoea" in query:
            speak("Diarrhea involves frequent, loose bowel movements leading to dehydration. Symptoms include skin elasticity loss, irritability, decreased urination, pale skin, increased heart rate, and reduced responsiveness. In exclusively breastfed babies, loose stools are normal. The World Health Organization defines diarrhea as three or more loose or liquid stools per day.")
            print("Diarrhea involves frequent, loose bowel movements leading to dehydration. Symptoms include skin elasticity loss, irritability, decreased urination, pale skin, increased heart rate, and reduced responsiveness. In exclusively breastfed babies, loose stools are normal. The World Health Organization defines diarrhea as three or more loose or liquid stools per day.")
            speak("i hope it is easy to understand")
            speak("do you want any other information?")
        elif "headache" in query:
            speak("Headache, also known as cephalalgia, is the symptom of pain in the face, head, or neck. It can occur as a migraine, tension-type headache, or cluster headache. There is an increased risk of depression in those with severe headaches.")
            print("Headache, also known as cephalalgia, is the symptom of pain in the face, head, or neck. It can occur as a migraine, tension-type headache, or cluster headache. There is an increased risk of depression in those with severe headaches.")
            speak("i hope it is easy to understand")
            speak("do you want any other information?")
        elif "music" in query:
            speak("Here you go with mus")
            # music_dir = "G:\\Song"
            music_dir = "E:\\song"
            songs = os.listdir(music_dir)
            print(songs)
            random = os.startfile(os.path.join(music_dir, songs[1]))

        elif 'time' in query:
            time = datetime.datetime.now().strftime('%I:%M %p')
            speak('Current time is ' + time)

        elif 'email to me' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "Receiver email address"
                sendEmail(to, content)
                speak("Email has been sent !")
            except Exception as e:
                print(e)
                speak("I am not able to send this email")

        elif 'send a mail' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                speak("whom should i send")
                to = input()
                sendEmail(to, content)
                speak("Email has been sent !")
            except Exception as e:
                print(e)
                speak("I am not able to send this email")

        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, my friend")

        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")

        elif "change my name to" in query:
            query = query.replace("change my name to", "")
            assname = query

        elif "change name" in query:
            speak("What would you like to call me, my friend ")
            assname = takeCommand()
            speak("Thanks for naming me")

        elif "what's your name" in query or "What is your name" in query:
            speak("My friends call me")
            speak("hey buddy!")
            print("My friends call me hey buddy!")

        elif 'no' in query or ' thank you' in query  or 'nothing' in query:
            speak("Thanks for giving me your time")
            exit()

        elif "who made you" in query or "who created you" in query:
            speak("I have been created by You.")

        elif 'joke' in query:
            speak(pyjokes.get_joke())

        elif 'search' in query or 'play' in query:

            query = query.replace("search", "")
            query = query.replace("play", "")
            webbrowser.open(query)

        elif "who i am" in query:
            speak("If you talk then definitely your human.")

        elif "why you came to world" in query:
            speak("Thanks to my creator. further It's a secret")


        elif 'is love' in query:
            speak("It is 7th sense that destroy all other senses")

        elif "who are you" in query:
            speak("I am your virtual assistant")

        elif 'reason for you' in query:
            speak("I was created as a Minor project ")

        elif 'change background' in query:
            ctypes.windll.user32.SystemParametersInfoW(20,
                                                       0,
                                                       "Location of wallpaper",
                                                       0)
            speak("Background changed successfully")



        elif 'news' in query:

            try:
                jsonObj = urlopen(
                    '''https://www.bing.com/search?pglt=41&q=times+of+india&cvid=b971eb00bc444f039070cfda7609d3a8&gs_lcrp=EgZjaHJvbWUqBggBEAAYQDIGCAAQRRg5MgYIARAAGEAyBggCEC4YQDIGCAMQABhAMgYIBBAAGEAyBggFEAAYQDIGCAYQABhAMgYIBxAAGEAyBggIEC4YQNIBCDM5NjNqMGoxqAIAsAIA&FORM=ANNTA1&PC=U531''')
                data = json.load(jsonObj)
                i = 1

                speak(' Here are some top news from the times of india')
                print('''=============== TIMES OF INDIA ============''' + '\n')

                for item in data['articles']:
                    print(str(i) + '. ' + item['title'] + '\n')
                    print(item['description'] + '\n')
                    speak(str(i) + '. ' + item['title'] + '\n')
                    i += 1
            except Exception as e:

                print(str(e))
        elif 'are you single' in query:
            speak('I am in a relationship with wifi')


        elif 'lock window' in query:
            speak("locking the device")
            ctypes.windll.user32.LockWorkStation()

        elif 'shutdown system' in query:
            speak("Hold On a Sec ! Your system is on its way to shut down")
            subprocess.call('shutdown / p /f')

        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
            speak("Recycle Bin Recycled")

        elif "don't listen" in query or "stop listening" in query:
            speak("for how much time you want to stop jarvis from listening commands")
            a = int(takeCommand())
            time.sleep(a)
            print(a)

        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.nl / maps / place/" + location + "")

        elif "camera" in query or "take a photo" in query:
            ec.capture(0, "Jarvis Camera ", "img.jpg")

        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])

        elif "hibernate" in query or "sleep" in query:
            speak("Hibernating")
            subprocess.call("shutdown / h")

        elif "log off" in query or "sign out" in query:
            speak("Make sure all the application are closed before sign-out")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])

        elif "write a note" in query:
            speak("What should i write, sir")
            note = takeCommand()
            file = open('jarvis.txt', 'w')
            speak("Friend, Should i include date and time")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("% H:% M:% S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)

        elif "show note" in query:
            speak("Showing Notes")
            file = open("jarvis.txt", "r")
            print(file.read())
            speak(file.read(6))

        

      
        elif "hey buddy!" in query:

            wishMe()
            speak("MED BUDDY! 1 point o in your service Mister")
            speak(assname)


        elif "send message " in query:
            # You need to create an account on Twilio to use this service
            account_sid = 'Account Sid key'
            auth_token = 'Auth token'
            client = Client(account_sid, auth_token)

            message = client.messages \
                .create(
                body=takeCommand(),
                from_='Sender No',
                to='Receiver No'
            )

            print(message.sid)

        elif "wikipedia.com" in query:
            webbrowser.open("wikipedia.com")

        elif "Good Morning" in query:
            speak("A warm" + query)
            speak("How are you Mister")
            speak(assname)

        # most asked question from google Assistant
        elif "cold and flu" in query or "cold" in query:
            speak("Cold is gradual in onset and flu is abrupt in onset. Cold rarely is accompanied by fever, chills, fatigue and feeling of weakness, while flu is usually accompanied by fever, chills, fatigue, body ache, joint pain and weakness. You might experience a stuffy nose and watery eyes when you have a cold, while it's not that common with the flu. You experience sore throat with a cold and rarely when it's the flu. Sneezing and coughing are more common in cold than with the flu and The symptoms include:Fever,Headache,Runny nose,Sneezing,Reduced sense of smell,Metallic taste in mouth,Chills,cough,Body pain or muscle pain,Sore throat")

        elif "how are you" in query:
            speak("I'm fine, glad you me that")

        elif "i love you" in query:
            speak("It's hard to understand")
        elif "recommend food" in query:
            if user_data:
                food_recommendation = recommend_food(user_data)
                speak(food_recommendation)
            else:
                speak("Please provide your health data .")
        elif "recommend exercise" in query:
            if user_data:
                exercise_recommendation = recommend_exercise(user_data)
                speak(exercise_recommendation)
            else:
                speak("Please provide your health data .")    
        elif "cancer" in query:
            speak("Cancer is a disease in which some of the body's cells grow uncontrollably and spread to other parts of the body. It can start almost anywhere in the human body, which is made up of trillions of cells. Definition: Cancer is characterized by the abnormal growth of cells with the potential to invade nearby tissues or spread to other parts of the body. Unlike benign tumors, which do not spread, cancerous tumors can invade surrounding tissues and metastasize to distant locations. Cell Behavior Differences: Cancer cells differ from normal cells in several ways:They grow even in the absence of signals telling them to do so, whereas normal cells only grow when they receive such signals. 2.Cancer cells ignore signals that normally tell cells to stop dividing or undergo programmed cell death (apoptosis). 3.They invade nearby areas and spread to other parts of the body, unlike most normal cells. 4.Cancer cells manipulate blood vessels to grow toward tumors, supplying them with oxygen and nutrients. 5.They evade the immune system, sometimes convincing immune cells to protect the tumor instead of attacking it. 6.Accumulate multiple changes in their chromosomes, leading to abnormal behaviors.")    
            print("Cancer is a disease in which some of the body's cells grow uncontrollably and spread to other parts of the body. It can start almost anywhere in the human body, which is made up of trillions of cells. Definition: Cancer is characterized by the abnormal growth of cells with the potential to invade nearby tissues or spread to other parts of the body. Unlike benign tumors, which do not spread, cancerous tumors can invade surrounding tissues and metastasize to distant locations. Cell Behavior Differences: Cancer cells differ from normal cells in several ways:They grow even in the absence of signals telling them to do so, whereas normal cells only grow when they receive such signals. 2.Cancer cells ignore signals that normally tell cells to stop dividing or undergo programmed cell death (apoptosis). 3.They invade nearby areas and spread to other parts of the body, unlike most normal cells. 4.Cancer cells manipulate blood vessels to grow toward tumors, supplying them with oxygen and nutrients. 5.They evade the immune system, sometimes convincing immune cells to protect the tumor instead of attacking it. 6.Accumulate multiple changes in their chromosomes, leading to abnormal behaviors.")
            speak("I hope it is easy to understand.")
            print("I hope it is easy to understand.")
            speak("do you want any other information?") 
            print("do you want any other information?")  
        elif "asthma" in query:
            speak("Asthma is a chronic respiratory condition characterized by inflammation of the airways, leading to wheezing, shortness of breath, chest tightness, and coughing.")
            print("Asthma is a chronic respiratory condition characterized by inflammation of the airways, leading to wheezing, shortness of breath, chest tightness, and coughing.")
            speak ("I hope it is easy to understand.")
            print("do you want any other iformation?")
        elif  "diabetes" or "sugar" in query:
            speak("Diabetes is a chronic condition that affects how your body metabolizes sugar (glucose). It's caused by insufficient insulin production or inefficient use of insulin by the body.")
            print("Diabetes is a chronic condition that affects how your body metabolizes sugar (glucose). It's caused by insufficient insulin production or inefficient use of insulin by the body.")
            speak("I hope it is easy understand")
            speak("do you want any other information?")
            print("do you want any other information?")
        elif "allergy " in query:
            speak("Allergy symptoms, which depend on the substance involved, can affect your airways, sinuses and nasal passages, skin, and digestive system. Allergic reactions can range from mild to severe. In some severe cases, allergies can trigger a life-threatening reaction known as anaphylaxis and causes are Sneezing,Itching of the nose, eyes or roof of the mouth ,Runny, stuffy nose,Watery, red or swollen eyes (conjunctivitis) and other  food allergy can cause:Tingling in the mouth,Swelling of the lips, tongue, face or throat,Hives,Anaphylaxis and i hope it will understand you.")
            print("Allergy symptoms, which depend on the substance involved, can affect your airways, sinuses and nasal passages, skin, and digestive system. Allergic reactions can range from mild to severe. In some severe cases, allergies can trigger a life-threatening reaction known as anaphylaxis and causes are Sneezing,Itching of the nose, eyes or roof of the mouth ,Runny, stuffy nose,Watery, red or swollen eyes (conjunctivitis) and other  food allergy can cause:Tingling in the mouth,Swelling of the lips, tongue, face or throat,Hives,Anaphylaxis and i hope it will understand you.")
            
            speak("I hope it is easy understand") 
            speak("do you want any other information?")     
        