import speech_recognition as sr
from unidecode import unidecode
# from pyfirmata import Arduino, util

# Cria uma instância do reconhecedor de fala
rec = sr.Recognizer()

def verifica_categoria(texto, categorias):
    texto = unidecode(texto).lower()
    palavras = set(texto.split())
    
    for categoria, palavras_chave in categorias.items():
        if any(palavra in palavras for palavra in palavras_chave):
            return categoria
    return "Desconhecido"

# Lista com as palavras-chave para identificação de função
categorias = {
    "Acender": ["acender", "acenda", "ligar", "ligue"],
    "Desligar": ["desligue", "apague", "apagar", "desligar"],
    "Destrancar": ["abra", "abrir", "destranque", "destrancar"],
    "Trancar": ["feche", "fechar", "tranque", "trancar"]
}

funcao = {
    "Acender": "1",
    "Desligar": "2",
    "Trancar": "3",
    "Destrancar": "4"
}

try:
    with sr.Microphone(0) as mic:
        #Esse comando se refere ao microfone que você está usando, é possível mudar conforme necessidade
        rec.adjust_for_ambient_noise(mic)
        print("Pode falar que irei reconhecer")
        audio = rec.listen(mic)
        texto = rec.recognize_google(audio, language="pt-BR")
        print("Você disse:", texto)
    
    categoria_encontrada = verifica_categoria(texto, categorias)

    if categoria_encontrada != "Desconhecido":
        if categoria_encontrada in funcao:
            comando_para_arduino = funcao[categoria_encontrada]
            print(f"Comando para o Arduino: {comando_para_arduino}")
            # Enviar o comando para o Arduino (usando pyfirmata)
            # board.digital[13].write(int(comando_para_arduino))  # Exemplo: define o estado do pino 13 (LED)
        else:
            print("Categoria reconhecida, mas função não mapeada.")
    else:
        print("Comando não reconhecido.")

except sr.UnknownValueError:
    print("Google Speech Recognition não conseguiu entender o áudio.")
except sr.RequestError as e:
    print(f"Erro ao conectar com o serviço do Google Speech Recognition; {e}")
except Exception as e:
    print(f"Ocorreu um erro: {e}")

# Fechar a conexão com o Arduino (se necessário)
# board.exit()
