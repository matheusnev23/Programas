import speech_recognition as sr

def listar_microfones():
    microfones = sr.Microphone.list_microphone_names()
    
    if not microfones:
        print("Nenhum microfone encontrado.")
    else:
        print("Microfones disponíveis:")
        for i, nome in enumerate(microfones):
            print(f"Índice {i}: {nome}")

if __name__ == "__main__":
    listar_microfones()
