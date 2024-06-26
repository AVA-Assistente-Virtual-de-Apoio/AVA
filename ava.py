"""
        TRABALHO DE GRADUAÇÃO DO CURSO DE ANÁLISE E DESENVOLVIMENTO DE SISTEMAS DA FATEC CARAPICUIBA

TÍTULO: AVA (ASSISTENTE VIRTUAL DE APOIO) - PESQUISA E DESENVOLVIMENTO DO SOFTWARE

ALUNOS:
        Ana Caroline Neves da Silva 
        Fabio Celestino dos Reis 
        Lincoln Alexandre Paulino da Silva 
ORIENTADOR:
        Luiz Sergio De Souza

OBJETIVO: DESENVOLVER UM SOFTWARE QUE FUNCIONE COMO UMA ASSISTENTE VIRTUAL COMANDADA POR VOZ

FUNÇÕES QUE A AVA PODE REALIZAR: ABRIR O ARQUIVO LEIA.TXT

"""
from metodos import *

# variáveis de configuração
voz="feminino"              #voz em execução
ligar=threading.Event()  #impede programa de rodar sem interface
ligar.set()

# variáveis de execução
cr=0 # contagem de requisições
nad=0 # número de acessos no dia

# listas
lsp1=['ola','oie','eai']#lista de saudações possíveis primeiro acesso do dia
lsp=['como posso ajudar hoje','que saudades o que vc precisa','bora trabalhar']
ls = ['oi', 'fala', 'diga','pois nao', 'que', 'eu']#lista de saudações
ls2 = ['diga','fala', 'o que', 'to ouvindo', 'manda','pode falar', 'sou toda ouvidos','o q mais vc precisa']#lista de saudações
comandos = ['word','excel','power point','powerpoint','navegador','chrome','internet explorer',
'wordpad','bloco de notas','notepad++','notepad mais mais','calculadora','lupa','gerenciador de arquivos','paint','pente',
'gerenciador de tarefas','player','captura']#programas que podem ser abertos
executavel = ['winword','excel','powerpnt','powerpnt','chrome','chrome','iexplore',
'wordpad','notepad','notepad++','notepad++','calc','magnify','explorer','mspaint','mspaint','taskmgr',
'wmplayer','snippingtool']#executavel dos programas que podem ser abertos
lrr = ['blz', 'ok', 'demoro', 'ta', 'ce que manda','fecho', 'ta bom entao', 'claro', 'show']#lista de resposas as requisições
desculpas = ['foi mal', 'entao', 'sabe o que e', 'desculpa', 'me perdoa', 'perdao']
justificativa = ['nao achei esse comando', 'nao sei o que vc quer', 'nao tenho ideia de como fazer isso', 'nao entendi']
justificativa2 = ['nao ouvi', 'nao entendi']
pergunta = ['ajudo em algo mais', 'quer mais alguma coisa', 'precisa de mim ainda']
rr = ['sim sim','sim', 'acho que sim', 'a hã', 'por favor', 'claro', 'sim meu amor', 'sim ava', 'preciso', 'ajuda', 'quero', 'quero sim', 'claro que quero']#respostas requisições
rr2 = ['sim','a hã','por favor','claro','preciso','precisa', 'ajuda', 'quero']#respostas requisições
ss = ['se precisar to aqui', 'quando quiser me chama', 'qualquer mao me chama', 'qualquer coisa me fala']
negativas = ['não não','não', 'nao', 'noupe', 'não obrigado', 'nao vlw', 'nao, valeu', 'nada', 'só', 'é só isso']
duvida = ['acho que não', 'não sei direito', 'talvez', 'sei lá', 'não sei']
operadores = ['mais','menos','dividido','vezes','+','-','x','/']
# todas as palavras chave que indicam algum comando possível de ser executado
chave=['pesquise', 'pesquisar', 'pesquisa','abre', 'abra', 'abrir',
       'organizar a pasta', 'organize a pasta', 'organiza a pasta',
       'organiza meus downloads','organize meus downloads', 
       'organiza meus documentos','organize meus documentos',
       'organiza essa pasta','controle total','tocar','quanto','me dê','leia','ler']
# palavras de ativação aceitas
ava=['ava','asa','tava','abba','aba','havan','hava','léo']
pesquisar=['pesquise', 'pesquisar', 'pesquisa']
abrir=['abre', 'abra', 'abrir']
teclados=["escreve","alt tab","tabi","menu","clicar","duplo click","enter","trocar janela","fechar janela","ask","de trabalho","copiar",
           "colar","sobe","desce","esquerda","direita",'voltar','refazer','recortar',]
organize=['organiza essa pasta','organizar a pasta', 'organize a pasta', 'organiza meus downloads','organize meus downloads',
          'organiza meus documentos','organize meus documentos']
mouses=['centro','centro direita','centro esquerda','mouse direita','mouse esquerda', 'subir', 'descer','primeiro quadrante',
       'segundo quadrante','terceiro quadrante','quarto quadrante']
redes_sociais = {
    'youtube': 'https://www.youtube.com',
    'facebook': 'https://www.facebook.com',
    'instagram': 'https://www.instagram.com',
    'twitter': 'https://www.twitter.com',
    'linkedin': 'https://www.linkedin.com',
    'reddit': 'https://www.reddit.com',
    'pinterest': 'https://www.pinterest.com',
    'snapchat': 'https://www.snapchat.com',
    'tik tok': 'https://www.tiktok.com',
    'whatsApp': 'https://web.whatsapp.com/',
    'chat GPT': 'https://openai.com/chatgpt/'
}
rs=['youtube', 'facebook', 'instagram', 'twitter', 'linkedin', 'reddit', 'pinterest', 'snapchat', 'tik tok', 'whatsapp','chat GPT']

# interface grafica----------------------------------------
psg.theme('DarkPurple4')

layout = [

    [psg.Text('Gênero da voz: '),psg.Button('feminino'),psg.Button('masculino')],
    [psg.Text(text_color='gold',font=('century',32),key='-RES-')],
    [psg.Image(filename='./imagem/ava.png', key='-IMG-'),psg.Image(filename='./imagem/micgray.png', key='-IMG2-')]
]

janela = psg.Window(
    ':: A V A ::',
    #size=(280,370),
    size=(340,440),
    alpha_channel=0.8,
    layout=layout
    )

def window():
    
    while True:
        global voz
        evento, valor = janela.read()
        if evento == 'feminino':
            janela['-IMG-'].update(filename='./imagem/ava.png')
            voz='feminino'
        if evento == 'masculino':
            janela['-IMG-'].update(filename='./imagem/leo.png')
            voz='masculino'
        if  evento == psg.WIN_CLOSED:
            ligar.clear()
            janela.close()
            break
        print(voz)
#fim interface grafica--------------------------------------
#função ouvir usuario, retorna string
def ouvir():
    microfone = sr.Recognizer()

    with sr.Microphone() as source:
        microfone.adjust_for_ambient_noise(source, duration=1)
        print("ouvindo...")
        janela['-IMG2-'].update(filename='./imagem/micgreen.png')
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

#função play da voz ava, recebe os dados de localização da voz
def playVoz(voz,pasta,audio):
    playsound(f'./voz/{voz}/{pasta}/{audio}.mp3')

#verifica se os valores de uma lista se encontram no que o usuario disse
def verificar(lista,tx):
    for item in lista:
        if (item in tx):
            return item
    return 'vazio'

#dividir texto, tira de um texto uma palavra especifica
def dividir_texto(texto, palavra):
    partes = texto.split(palavra, 1)  # Dividir apenas uma vez
    print(partes)
    resultado = partes[1].strip() if len(partes) > 1 else ''
    print(resultado)
    return resultado

#procedimento para quando nao reconhecer palavra chave
def nao_reconhecido(voz,tx):
    janela['-IMG2-'].update(filename='./imagem/micred.png')
    parecido = ['ana', 'axa', 'ala', 'vava', 'a vá']
    espanto = ['ta zuando ne', 'ta tirando com minha cara', 'ei esqueceu meu nome']
    if (tx in parecido):
        playVoz(voz,'espanto',rand(espanto))
    elif(tx=='desligar'):
        print('Desligando...')
    else:
        print("ouvindo...")

#procura e executa comandos pre definidos
def executar_comando(voz,comando,tx):
    if comando in pesquisar:
        if 'no gemini' in tx:
            tx=dividir_texto(tx,'no gemini')
            tx = ''.join(tx).strip()
            if tx=="":
                playVoz(voz,'justificativa2',rand(justificativa2))
            else:
                resultado=gemini(tx)
                if resultado == 'erro':
                    playVoz(voz,'pesquisa','nao foi possivel concluir a pesquisa')  
                else:  
                    resultado = resultado.replace('*', '')
                    popup(tx,resultado)

        elif 'no google' in tx:
            tx=dividir_texto(tx,'no google')
            tx = ''.join(tx).strip()
            if tx=="":
                playVoz(voz,'justificativa2',rand(justificativa2))
            else:
                abrir_link('vazio',tx,voz)

        elif 'no youtube' in tx:
            tx=dividir_texto(tx,'no youtube')
            tx = ''.join(tx).strip()
            if tx=="":
                playVoz(voz,'justificativa2',rand(justificativa2))
            else:    
                youtube(tx,voz)
        elif 'para mim' in tx:
            tx=dividir_texto(tx,'para mim')
            tx = ''.join(tx).strip()
            if tx=="":
                playVoz(voz,'justificativa2',rand(justificativa2))
            else:
                abrir_link('vazio',tx,voz)
        else:
            tx=dividir_texto(tx,comando)
            tx = ''.join(tx).strip()
            if tx=="":
                playVoz(voz,'justificativa2',rand(justificativa2))
            else:
                abrir_link('vazio',tx,voz)
    
    elif(comando == 'me dê'):
            resultado=gemini(tx)
            if resultado == 'erro':
                playVoz(voz,'pesquisa','nao foi possivel concluir a pesquisa')  
            else:  
                resultado = resultado.replace('*', '')
                popup(tx,resultado)       

    elif(comando == 'quanto'):
            r=0
            tx=tx.split()
            for item in operadores:
                if (item in tx):
                    if (item !='dividido'):
                        primeiro=tx.index(item)-1
                        segundo=tx.index(item)+1
                        n1=int(tx[primeiro])
                        n2=int(tx[segundo])
                        print(str(n1) +" e "+ str(n2))
                        if(item == '+' or item == 'mais'): 
                            r=(n1 + n2)
                                               
                        elif(item == '-' or item == 'menos'):
                            r=(n1 - n2)
                           
                        elif(item == 'x' or item =='vezes'):
                            r=(n1 * n2)
                        
                        elif(item == '/'):
                            r=(n1 / n2) 

                    elif(item == 'dividido'):
                        primeiro=tx.index('por')-1
                        segundo=tx.index('por')+2
                        n1=int(tx[primeiro])
                        n2=int(tx[segundo])
                        r=(n1 / n2)

                    else:
                        pass
            janela['-RES-'].update(r)
            speaker = win32com.client.Dispatch("SAPI.SpVoice")
            speaker.Speak(str(r))

    elif(comando in abrir):
        v=verificar(rs,tx)
        if v!='vazio':
            print(v)
            for item in rs:
                if item in tx:
                    abrir_link(redes_sociais.get(item),"vazio",voz)
        else:
            v=verificar(comandos,tx)
            if v!='vazio':
                for item in comandos:
                    if (item in tx):
                        h = comandos.index(item)
                        print(h)
                        os.system(f"start {executavel[h]}.exe")
                        print(executavel[h])
                        sleep(1)
            else:
                playVoz(voz,"outros","nao achei esse comando")
                
    elif comando == 'tocar':
        palavras = tx.split()
        frase_modificada = " "
        for palavra in palavras[1:]:
            frase_modificada += palavra + " "
        frase_modificada = frase_modificada.strip()
        youtube(frase_modificada,voz)
        play()
        playVoz(voz,"outros","tocando")

    elif comando == "leia":
        pag.sleep(0.2)
        pag.hotkey('ctrl','c')
        texto=pyperclip.paste()
        leia(texto)
    
    elif comando == "ler":
        pag.sleep(0.2)
        pag.hotkey('ctrl','c')
        texto=pyperclip.paste()
        ler(texto)

    elif comando == 'controle total':
        playVoz(voz,"outros","controle")
        while tx!='sair do controle':
            tx=ouvir()
            v=verificar(mouses,tx)
            if v!='vazio':
                mouse(tx)
            else:
                v=verificar(teclados,tx)
                if v!='vazio':
                    teclado(tx)
                else:
                    if "leia" in tx:
                        pag.sleep(0.2)
                        pag.hotkey('ctrl','c')
                        texto=pyperclip.paste()
                        leia(texto)
                    elif "ler" in tx:
                        pag.sleep(0.2)
                        pag.hotkey('ctrl','c')
                        ler(texto)
                    else: 
                        print('comando inválido')
        playVoz(voz,"outros","controle desativado")

    elif comando in organize:
        if comando == 'organiza meus downloads'or comando == 'organize meus downloads':
            pasta('downloads',voz)
        if comando == 'organiza meus documentos'or comando == 'organize meus documentos':
            pasta('documentos',voz)
        if comando == 'organiza essa pasta'or comando == 'organiza essa pasta para mim':
            pegar_caminho()
            caminho=pyperclip.paste()
            sleep(1)
            organizar(caminho)
        if comando == 'organizar a pasta' or comando == 'organize a pasta' or comando == 'organiza a pasta':
            playVoz(voz,'outros','isso pode demorar um pouco')
            palavra=dividir_texto(tx, comando)
            pasta(palavra,voz)
        else:pass
    
    else:
        playVoz(voz,'desculpas',rand(desculpas))
        playVoz(voz,'justificativa','nao achei esse comando')
        
#escolher item aleatoria de uma lista
def rand(lista):
    n = random.choice(lista)
    return n

#inicia uma execução paralela da interface gráfica
interface = threading.Thread(target = window, daemon=True)
interface.start()

tx = ''     #variavel importante para o looping principal
#looping principal>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
while (tx != 'desligar' and ligar.is_set()) :
    tx = ouvir() #entrada de texto usuario
    janela['-IMG2-'].update(filename='./imagem/micgray.png')
    v=verificar(ava,tx)
    if (v!='vazio'): # se palavra de ativação esta correta 
        if v=='léo':
            voz='masculino'
            janela['-IMG-'].update(filename='./imagem/leo.png')
        else:
            voz='feminino'
            janela['-IMG-'].update(filename='./imagem/ava.png')
        if (nad==0):
            playVoz(voz,'lsp1',rand(lsp1))
            playVoz(voz,'lsp',rand(lsp))#saudar usuário

        else:
            playVoz(voz,'ls',rand(ls))
        janela['-RES-'].update(" ")
        nad+=1
        txr='sim'
        r=''
        #looping secundário>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        while (txr=='sim'and ligar.is_set()):
            tx = ouvir()#fazer requisição
            janela['-IMG2-'].update(filename='./imagem/micgray.png')
            print(tx)  
            comando = verificar(chave,tx) 
            if(tx == 'desligar'):
                txr = tx
                break

            elif(tx=='vazio'):
                playVoz(voz,'desculpas',rand(desculpas))
                playVoz(voz,'justificativa','nao ouvi')

            elif(comando != 'vazio'):
                executar_comando(voz,comando,tx)
                
            else:
                playVoz(voz,'desculpas',rand(desculpas))
                playVoz(voz,'justificativa',rand(justificativa))
                
            playVoz(voz,'pergunta',rand(pergunta))  
            sleep(1)
            txr = ouvir()
            janela['-IMG2-'].update(filename='./imagem/micgray.png')
            testar=verificar(rr2,txr)
            negar=verificar(negativas,txr)
            
            if (negar != 'vazio'):
                r= rand(lrr)
                print('...')
            
            elif (testar != 'vazio'):
                playVoz(voz,'ls2',rand(ls2))
                txr = 'sim'

            elif (txr in duvida):
                r = ("entao vai pensando ai")

            elif (txr=='desligar'):
                tx=txr

            elif (txr=='vazio'):
                r='nao ouvi'

            else:
                r= ('vou entender como um nao mas')
        
        if(tx=='desligar'):
            playVoz(voz,'negativas','ok')
    
        else:
            playVoz(voz,'negativas',r)
            playVoz(voz,'ss',rand(ss))  

    if(tx=='desligar'):
       break
        

    else:
        nao_reconhecido(voz,tx)

playVoz(voz,'desligando','desligando')
