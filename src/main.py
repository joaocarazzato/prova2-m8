from playsound import playsound
from gtts import gTTS


def tts_function(tts_text):
    print("Transformando em aúdio...")
    tts = gTTS(tts_text, lang='pt', tld='com.br')
    print("Criando arquivo de aúdio...")
    tts.save("out.mp3")
    print("Lendo...\n")
    playsound("out.mp3")


def main():
    print("Bem vindo ao TTS! Digite a frase que queira e ele te retornará em forma de aúdio! Caso deseje sair, é só escrever 'sair'!")
    while True:
        phrase = input("Digite a frase: ")
        if phrase.lower() == "sair":
            print("Até logo!")
            exit()
        tts_function(phrase)

if __name__ == "__main__":
    main()