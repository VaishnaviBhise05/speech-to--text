import speech_recognition as sr
r=sr.Recognizer()
with sr.Microphone() as source:
    print("Adjusting for background noise...")
    r.adjust_for_ambient_noise(source, duration=2)
    print("Speak Now...")
    try:
        audio = r.listen(source, timeout=15)
        print("Recognizing...")
        
        text=r.recognize_google(audio)
        
        print("You said: ", text)
                                                                                                                                                                                                                                                            
    except sr.WaitTimeoutError:
        print("No speech Detected.")
        
    except sr.UnknownValueError:
        print("could not understand the audio.")
        
    except sr.RequestError:
        print("Internet connection error.")
   