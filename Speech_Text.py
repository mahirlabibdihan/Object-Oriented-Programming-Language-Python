# Python program to translate 
# speech to text and text to speech 
 
import time  
import sys
import speech_recognition as sr 
import pyttsx3  
  
# Initialize the recognizer  
r = sr.Recognizer()  
  
# Function to convert text to 
# speech 
def SpeakText(command): 
      
    # Initialize the engine 
    engine = pyttsx3.init() 
    engine.say(command)  
    engine.runAndWait() 
      
      
# Loop infinitely for user to 
# speak 
  
while(1):     
      
    # Exception handling to handle 
    # exceptions at the runtime 
    try: 
          
        # use the microphone as source for input. 
        with sr.Microphone() as source2: 
              
            # wait for a second to let the recognizer 
            # adjust the energy threshold based on 
            # the surrounding noise level  
            r.adjust_for_ambient_noise(source2, duration=0.1) 
              

            print("Speak : ")
            #listens for the user's input  
            audio2 = r.listen(source2) 
              
            # Using ggogle to recognize audio 
            MyText = r.recognize_google(audio2) 
            MyText = MyText.lower() 
            Text=MyText
            if(MyText == "exit"): 
                Text="Exiting..."
                SpeakText(Text)
                time.sleep(1)
                sys.exit(0)
            elif(MyText== "how are you"):
                Text="I am fine"
            elif(MyText=="hello"):
                Text="Hi"
            elif(MyText=="thank you"):
                Text="Welcome"
            elif(MyText=="what are you doing"):
                Text="Talking to you"


            print(Text) 
            SpeakText(Text) 
              
    except sr.RequestError as e: 
        print("Could not request results; {0}".format(e)) 
          
    except sr.UnknownValueError: 
        print("unknown error occured") 