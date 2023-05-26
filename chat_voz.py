import speech_recognition as sr
import pyttsx3

# Inicializa o mecanismo de síntese de fala
engine = pyttsx3.init()
engine.setProperty('rate', 100)  # Valor padrão: 200

# Função para reconhecimento de fala
def ouvir_microfone():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Diga algo...")
        audio = r.listen(source)

    try:
        texto = r.recognize_google(audio, language='en')
        print("Você disse: " + texto)
        return texto
    except sr.UnknownValueError:
        print("Não foi possível entender o áudio")
    except sr.RequestError as e:
        print("Erro ao tentar reconhecer a fala; {0}".format(e))

# Função para gerar a resposta em voz
def falar(resposta):
    engine.say(resposta)
    engine.runAndWait()

# Loop principal do chat de voz
while True:
    comando = ouvir_microfone()

    if comando == "hello":
        resposta = "Hello! How can I help you?"
    elif comando == "goodbye":
        resposta = "Goodbye! Have a great day!"
    elif comando == "stop":
        resposta = "Stopping the voice chat..."
        falar(resposta)
        break
    else:
        resposta = "Sorry, I didn't understand that."
    
    print("Chatbot: " + resposta)
    falar(resposta)

