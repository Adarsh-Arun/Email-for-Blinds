import speech_recognition as sr
import easyimap as e
import pyttsx3
import smtplib

unm = "*@gmail.com"
pwd = "*"

r = sr.Recognizer()

engine = pyttsx3.init()
voice = engine.getProperty('voices')
engine.setProperty('voice', voice[1].id)
engine.setProperty('rate',150)

def speak(str):
    print(str)
    engine.say(str)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        # r.adjust_for_ambient_noice(source)
        str = "Speak Now"
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            return text
        except:
            str = "sorry we could not recognize what you said"
            speak(str)


def sendmail():

    rec = "@gmail.com"

    str = "please speak the budy of your email"
    speak(str)
    msg = listen()

    str = "you have spoken the message"
    speak(str)
    speak(msg)

    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login(unm, pwd)
    server.sendmail(unm, rec, msg)
    server.quit()

    str = "the mail has been sent"
    speak(str)


def readmail():
    server = e.connect("imap.email.com", unm, pwd)
    server.listids()

    str = " please say the serial number of the email you want to read stating fron latest"
    speak(str)

    a = listen()
    if( a == "tu"):
        a="2"

    b = int(a)-1

    email = server.mail(server.listids()[b])

    str = "the mail is from: "
    speak(str)
    speak(email.from_addr)
    str = "the subject of the email is : "
    speak(str)
    speak(email.title)
    str = "the body of email is :"
    speak(str)
    speak(email.body)

str = "welcome to voice controlled email service"
speak(str)



while(1):
    
    str = "what do you want to do?"
    speak(str)

    str = "speak sent to send email    speak read to read inbox   speak exit to exit"
    speak(str)

    ch = listen()

    if (ch == 'sent'):
        str = "you have chosen to sent an email"
        speak(str)
        sendmail()
    
    elif (ch == 'read'):
        str = " you have chosen to read email"
        speak(str)
        readmail()

    elif (ch== 'exit'):
        str = "you have chosen to exit, bye"
        speak(str)
        exit(1)

    else:
        str = "invalid choice, you said:"
        speak(str)
        speak(ch)