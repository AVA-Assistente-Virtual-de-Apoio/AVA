import os
import random
import threading
import speech_recognition as sr
import tkinter as tk
import pyautogui as pag
import PySimpleGUI as psg
import datetime
import shutil
import win32com.client
import pymsgbox
import pyperclip
import webbrowser
import google.generativeai as genai
from time import sleep
from playsound3 import playsound
from dotenv import load_dotenv

#::> CONFIGURAÇÕES DA API DO GEMINI -- PARA OBTER SUA CHAVE ACESSE O SITE: https://gemini.google.com 
load_dotenv()
GOOGLE_API_KEY = os.environ['GOOGLE_API_KEY']
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')

#::> FUNÇÃO CONTROLE TOTAL
#::> MÉTODOS RELACIONADOS AO CONTROLE DO TECLADO
def alt_tab():
    pag.keyDown('alt')
    pag.press('tab')
    pag.keyUp('alt')

def tab():
    pag.press('tab')

def alt():
    pag.press('alt')    

def enter():
    pag.press('enter')

def clicar():
    pag.sleep(0.2)
    pag.click()
    
def duplo_clique():
    pag.sleep(0.2)
    pag.click()
    pag.sleep(0.1)
    pag.click()

def copiar():
    pag.sleep(0.2)
    pag.hotkey('ctrl','c')

def recortar():
    pag.sleep(0.2)
    pag.hotkey('ctrl','x')

def colar():
    pag.sleep(0.3)
    pag.hotkey('ctrl','v')

def desfazer():
    pag.sleep(0.3)
    pag.hotkey('ctrl','z')

def refazer():
    pag.sleep(0.3)
    pag.hotkey('ctrl','y')

def trocar_janela():
    pag.hotkey('win','tab')

def area_de_trabalho():
    pag.hotkey('win','d')

def fechar_janela():
    pag.hotkey('alt','f4')

def esc():
    pag.hotkey('esc')

def selecionar():
    pag.click()

def direita():
    pag.keyDown('right')
    pag.keyUp('right')

def esquerda():
    pag.keyDown('left')
    pag.keyUp('left')

def sobe():
    pag.keyDown('up')
    pag.keyUp('up')

def desce():
    pag.keyDown('down')
    pag.keyUp('down')

def escreve(tx):
    palavras = tx.split()
    frase_modificada = " "
    for palavra in palavras[1:]:
        frase_modificada += palavra + " "
    frase_modificada = frase_modificada.strip()
    pyperclip.copy(frase_modificada)
    colar()

def teclado(texto):
    if "alt tab" in texto:
        alt_tab()
    elif "tab" in texto or "tabi" in texto:
        tab()
    elif "menu" in texto:
        alt()
    elif "voltar" in texto:
        desfazer()
    elif "refazer" in texto:
        refazer()
    elif "recortar" in texto:
        recortar()
    elif "clicar" in texto:
        clicar()
    elif "duplo click" in texto:
        duplo_clique()
    elif "escreve" in texto:
        escreve(texto)
    elif "enter" in texto:
        enter()
    elif "trocar janela" in texto:
        trocar_janela()
    elif "fechar janela" in texto:
        fechar_janela()
    elif "ask" in texto:
        esc()
    elif "de trabalho" in texto:
        area_de_trabalho()
    elif "copiar" in texto:
        copiar()
    elif "colar" in texto:
        colar()
    elif "sobe" in texto:
        n = texto.lower().count("sobe")
        for _ in range(n):
            sobe()
    elif "desce" in texto:
        n = texto.lower().count("desce")
        for _ in range(n):
            desce()
    elif "esquerda" in texto:
        n=texto.lower().count("esquerda")
        for _ in range(n):
            esquerda()
    elif "direita" in texto:
        n=texto.lower().count("direita")
        for _ in range(n):
            direita()
    else:
        pass
#::> FIM DOS MÉTODOS RELACIONADOS AO CONTROLE DO TECLADO

#::> FUNÇÃO CONTROLE TOTAL
#::> MÉTODOS RELACIONADOS AO CONTROLE DO MOUSE
resolucao_tela = pag.size()# Obter a resolução da tela como uma tupla (largura, altura)
largura_tela, altura_tela = resolucao_tela# Separar os valores de largura e altura em variáveis separadas
# define o quanto o mouse vai andar, para movimentos curtos
movx=largura_tela/50
movy=altura_tela/50

def mover_centro():
  """Move o mouse para o centro da tela."""
  x = largura_tela // 2
  y = altura_tela // 2
  pag.moveTo(x, y)

def mover_direita():
  """Move o mouse para o centro da vertical e para a direita (terço da tela)."""
  x = largura_tela * 3 // 4
  y = altura_tela // 2
  pag.moveTo(x, y)

def mover_esquerda():
  """Move o mouse para o centro da vertical e para a esquerda (terço da tela)."""
  x = largura_tela // 4
  y = altura_tela // 2
  pag.moveTo(x, y)

def mover_primeiro_quadrante():
  """Move o mouse para o centro do primeiro quadrante (superior direito)."""
  x = largura_tela * 3 // 4
  y = altura_tela // 4
  pag.moveTo(x, y)

def mover_segundo_quadrante():
  """Move o mouse para o centro do segundo quadrante (superior esquerdo)."""
  x = largura_tela // 4
  y = altura_tela // 4
  pag.moveTo(x, y)

def mover_terceiro_quadrante():
  """Move o mouse para o centro do terceiro quadrante (inferior esquerdo)."""
  x = largura_tela // 4
  y = altura_tela  * 3 // 4
  pag.moveTo(x, y)

def mover_quarto_quadrante():
  """Move o mouse para o centro do quarto quadrante (inferior direito)."""
  x = largura_tela* 3 // 4
  y = altura_tela * 3 // 4
  pag.moveTo(x, y)

def mover_d():
  """Move o mouse para a direita."""
  posicao_mouse = pag.position()
  x, y = posicao_mouse

  pag.moveTo(x+movx, y)
  
def mover_e():
  """Move o mouse para a direita."""
  posicao_mouse = pag.position()
  x, y = posicao_mouse

  pag.moveTo(x-movx, y)

def mover_cima():
  """Move o mouse para a direita."""
  posicao_mouse = pag.position()
  x, y = posicao_mouse

  pag.moveTo(x, y-movy)
 
def mover_baixo():
  """Move o mouse para a direita."""
  posicao_mouse = pag.position()
  x, y = posicao_mouse

  pag.moveTo(x, y+movy)

def mouse(proxima_posicao):
    # Chame a função de movimento do mouse correspondente
    if proxima_posicao.lower() == "centro":
        mover_centro()
    elif proxima_posicao.lower() == "centro direita":
        mover_direita()
    elif proxima_posicao.lower() == "centro esquerda":
        mover_esquerda()
    elif "mouse direita" in proxima_posicao.lower():
            n = proxima_posicao.lower().count("mouse direita")
            for _ in range(n):
                mover_d()

    elif "mouse esquerda" in proxima_posicao.lower():
            n = proxima_posicao.lower().count("mouse esquerda")
            for _ in range(n):
                mover_e()
        
    elif "subir" in proxima_posicao.lower():
            n = proxima_posicao.lower().count("subir")
            for _ in range(n):
                mover_cima()

    elif "descer" in proxima_posicao.lower():
            n = proxima_posicao.lower().count("descer")
            for _ in range(n):
                mover_baixo()

    elif proxima_posicao.lower() == "primeiro quadrante":
        mover_primeiro_quadrante()
    elif proxima_posicao.lower() == "segundo quadrante":
        mover_segundo_quadrante()
    elif proxima_posicao.lower() == "terceiro quadrante":
        mover_terceiro_quadrante()
    elif proxima_posicao.lower() == "quarto quadrante":
        mover_quarto_quadrante()
#::>  FIM DOS MÉTODOS RELACIONADOS AO CONTROLE DO MOUSE

#::>  FUNÇÃO TOCAR -- MÚSICA NO YOUTUBE
#::>  MÉTODOS RELACIONADOS AO YOUTUBE
def youtube(texto,voz):# abre uma página no youtube e pesquisa o que o usuário deseja assistir
  try:
    url=(f"https://www.youtube.com/results?search_query={texto}")
    webbrowser.open(url)
  except webbrowser.OpenerError:
    # Se o navegador padrão não for encontrado, exiba uma mensagem de erro
        playsound(f'./voz/{voz}/{'outros'}/{'verifique'}.mp3')

def play():
    pag.sleep(2),
    mover_segundo_quadrante()
    pag.sleep(1)
    pag.click()
#::>  FIM DOS MÉTODOS RELACIONADOS AO YOUTUBE

#::>  FUNÇÃO ABRIR
#::>  MÉTODOS RELACIONADOS AO COMANDO ABRIR
def abrir_link(http,texto,voz): # se a requisição for para abrir uma rede social, o caminho http já está pronto
    if http != 'vazio':         # do contrário, é usado o caminho do google para efeturar a pesquisa
        url=http
    else:
        url = (f"https://www.google.com/search?q={texto}")
    try:
        # Tente abrir a URL usando o navegador padrão
        webbrowser.open(url)
        sleep(2)
    except webbrowser.OpenerError:
        # Se o navegador padrão não for encontrado, exiba uma mensagem de erro
        playsound(f'./voz/{voz}/{'outros'}/{'verifique'}.mp3')
#::>  FIM DOS MÉTODOS RELACIONADOS AO COMANDO ABRIR

#::>  FUNÇÃO PESQUISAR
#::>  MÉTODOS RELACIONADOS A PESQUISA
def gemini(texto):# faz pesquisa na IA GEMINI através de API
    response = model.generate_content(texto)
    if response is not None:
        return response.text
    else:
        response = "erro"
        return response.text
    
def popup(pergunta,resposta):# As respostas do GEMINI são apresentadas nessa janela
    root = tk.Tk()
    root.title(pergunta)
    corpo = tk.Text(root)
    corpo.pack()
    corpo.insert(tk.END, resposta)
    root.mainloop()
#::>  FIM DOS MÉTODOS RELACIONADOS A PESQUISA

#::>  FUNÇÃO ORGANIZAR
#::>  MÉTODOS RELACIONADOS A ORGANIZAÇÃO DE PASTAS
def organizar(pasta,voz):# organiza os arquivos de uma pasta, separando-os por tipo em pastas 

    # listas que separam as extensões de arquivos mais comuns por tipo
    texto = [".docx", ".txt", ".pdf", ".rtf", ".odt"]
    planilha = [".xlsx", ".csv", ".ods"]
    apresentacao = [".pptx", ".key", ".odp"]
    imagem = [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"]
    audio = [".mp3", ".wav", ".aac", ".flac", ".wma"]
    video = [".mp4", ".avi", ".mov", ".wmv", ".mkv"]
    zip = [".zip", ".rar", ".7z"]
    executavel = [".exe", ".dmg", ".deb", ".rpm"]
    programa = [".py", ".java", ".c", ".cpp", ".cs", ".html", ".css", ".js", ".php", ".swift", ".rb", ".pl", ".sh", ".bat"]
    # Nome das pastas para guardar os arquivos
    pastas = ["texto", "planilha", "apresentacao", "imagem", "audio", "video", "zip", "executavel", "programa", "outros"]

    for categoria in pastas:# Analisa se a pasta para guardas os arquivos já existe, se não existir ela será criada.
        if not os.path.exists(os.path.join(pasta, categoria)):
            print(pasta+categoria)
            os.makedirs(os.path.join(pasta, categoria))

    for arquivo in os.listdir(pasta):# analisa cada arquivo do diretório escolhido   
        if arquivo == ".":# se o arquivo for o próprio diretório será ignorado  
            continue
        tipo = os.path.splitext(arquivo)[1]
        if tipo == "":# se o aquivo for uma pasta será ignorado
            pass
        else:#etiqueta cada arquivo com o nome da pasta correspondente.
            tipo = os.path.splitext(arquivo)[1]#separa a extensão do arquivo para verificar a qual pasta pertence
            etiqueta = None
            if tipo in texto:
                etiqueta = "texto"
            elif tipo in planilha:
                etiqueta = "planilha"
            elif tipo in apresentacao:
                etiqueta = "apresentacao"
            elif tipo in imagem:
                etiqueta = "imagem"
            elif tipo in audio:
                etiqueta = "audio"
            elif tipo in video:
                etiqueta = "video"        
            elif tipo in zip:
                etiqueta = "zip"
            elif tipo in executavel:
                etiqueta = "executavel"
            elif tipo in programa:
                etiqueta = "programa"
            else:
                etiqueta = "outros"
            
            caminho=os.path.join(pasta, arquivo)
            novo_caminho = os.path.join(pasta, etiqueta, arquivo)# Move o arquivo para a pasta apropriada
            if os.path.exists(novo_caminho):
                novo_nome, ext = os.path.splitext(arquivo)# Se um arquivo com o mesmo nome existe, renomeie o novo arquivo
                agora = datetime.datetime.now()
                hora_formatada = agora.strftime("%Y%m%d%H%M%S")
                novo_nome = f"{novo_nome}_{hora_formatada}{ext}"  
                novo_caminho = os.path.join(pasta, etiqueta, novo_nome)
                print(novo_caminho)
                try:
                    shutil.move(caminho, novo_caminho)
                # Se o arquivo estiver aberto por outro processo, dispara uma aviso, e não move o arquivo
                except PermissionError:
                    playsound(f'./voz/{voz}/{'outros'}/{'o arquivo'}.mp3')
                    speaker = win32com.client.Dispatch("SAPI.SpVoice")
                    speaker.Speak(arquivo)
                    playsound(f'./voz/{voz}/{'outros'}/{'usado'}.mp3')

            else:
                try:
                    shutil.move(caminho, novo_caminho)
                except PermissionError:
                    playsound(f'./voz/{voz}/{'outros'}/{'o arquivo'}.mp3')
                    speaker = win32com.client.Dispatch("SAPI.SpVoice")
                    speaker.Speak(arquivo)
                    playsound(f'./voz/{voz}/{'outros'}/{'usado'}.mp3')

def pasta(tx,voz):# pega o caminho da pasta a ser organizada
    pasta=tx
    # se a pasta é downloads ou documentos, temos os caminhos abaixo
    if pasta == 'downloads':
        caminho = r"C:\Users\Fabio\Downloads"
    elif pasta=='documentos':
        caminho = r"C:\Users\Fabio\Documents"
    else:
        # caso contrario, faz uma busca no HD pela pasta
        caminhos = encontrar_pasta(pasta)
        caminho=''
        resultados = []
        if caminhos:
            if len(caminhos) == 1:
                print("Caminho da pasta encontrada:", caminhos[0])
                caminho=caminhos[0]
            else:
                # caso mais de uma pasta como mesmo nome for encontrada, o usuário escolhe qual pasta organizar
                playsound(f'./voz/{voz}/{'outros'}/{'mais de uma pasta'}.mp3')
                for i,caminho in enumerate(caminhos):
                    resultados.append(str(i)+"---"+caminho)
                resultado_final = "\n".join(resultados)
                pymsgbox.alert(resultado_final, "escolha um caminho:")
                escolha = pymsgbox.prompt( resultado_final,'Escolha um caminho ou digite cancelar:')
                if escolha == 'vazio':
                    escolha='cancela'
                if escolha == 'cancela' or escolha == 'cancelar':
                    playsound(f'./voz/{voz}/{'outros'}/{'cancelada'}.mp3')
                    return
                else:
                    escolha=int(escolha)
                    if escolha>(len(caminhos)-1):
                        print("Escolha inválida, operação cancelada")
                        playsound(f'./voz/{voz}/{'outros'}/{'invalida'}.mp3')
                        playsound(f'./voz/{voz}/{'outros'}/{'cancelada'}.mp3')
                        return
                    else:
                        caminho=caminhos[escolha]
                        

    # com base no caminho escolhido a pasta é organizada
    organizar(caminho)
    playsound(f'./voz/{voz}/{'outros'}/{'sucesso'}.mp3')

def pegar_caminho():# pega o caminho da pasta a ser orgarniza quando o usuário diz: Organize essa pasta
    sleep(2)
    pag.moveTo(1248, 68)
    pag.sleep(0.2)
    pag.click()
    pag.sleep(0.2)
    pag.hotkey('ctrl','c')
    pag.sleep(0.2)

def encontrar_pasta(nome_pasta):# faz a busca de uma pasta iniciando no diretório raiz
    diretorio_inicial='C:\\'
    resultados = []
    for raiz, diretorios, arquivos in os.walk(diretorio_inicial):
        if nome_pasta in diretorios:
            resultados.append(os.path.join(raiz, nome_pasta))
    return resultados if resultados else None
#::>  FIM DOS MÉTODOS RELACIONADOS A ORGANIZAÇÃO DE PASTAS

#::>  FUNÇÃO LER
#::>  MÉTODOS RELACIONADOS A LEITURA
def leia(text):# código inicial para inicializar o speaker que fará a leitura do texto
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Speak(text)

def ler(texto):
    event = threading.Event()
    def ouvindo():
        microfone = sr.Recognizer()

        with sr.Microphone() as source:
            microfone.adjust_for_ambient_noise(source, duration=1)
            print("ouvindo...")
            audio = microfone.listen(source)
            
        try:
            frase = microfone.recognize_google(audio, language = 'pt-BR')
            
            if frase is None:
                frase = 'não entendi'
                return frase
            else: 
                print(frase)
                return frase.lower()

        except sr.UnknownValueError:
            frase = "vazio"
            return frase
        except sr.RequestError:
            frase ="vazio"
            return frase

    def speak_text(text):
        # código inicial para inicializar o speaker que fará a leitura do texto
        speaker = win32com.client.Dispatch("SAPI.SpVoice")

        # Loop de fala com verificação de sinalização para parar a reprodução caso necessário
        for line in text.splitlines():
            while event.is_set():
                event.clear()  # Redefinir o evento após a interrupção
                return

            speaker.Speak(line)

        # metodo para monitorar a fala do usuário em paralelo com a leitura
    def monitor_playback():
        stopwords=['pare','para','tá bom','ta bom','pode parar','chega']
        while event.is_set:
            # ouve o usuário através do método ouvir()
            input_text=ouvindo()
            for item in stopwords:
                if (item in input_text):
                    event.set()# altera o status do evento, interrompendo a leitura

    thread = threading.Thread(target=monitor_playback, daemon=True)
    thread.start()
    speak_text(texto)
#::>  FIM DOS MÉTODOS RELACIONADOS A LEITURA


