        TRABALHO DE GRADUAÇÃO DO CURSO DE ANÁLISE E DESENVOLVIMENTO DE SISTEMAS DA FATEC CARAPICUIBA

TÍTULO: AVA (ASSISTENTE VIRTUAL DE APOIO) - PESQUISA E DESENVOLVIMENTO DO SOFTWARE

ALUNOS:
        Ana Caroline Neves da Silva 
        Fabio Celestino dos Reis 
        Lincoln Alexandre Paulino da Silva 
ORIENTADOR:
        Luiz Sergio De Souza

OBJETIVO: DESENVOLVER UM SOFTWARE QUE FUNCIONE COMO UMA ASSISTENTE VIRTUAL COMANDADA POR VOZ

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
LINGUAGEM: PARA ESSE PROJETO USAMOS Python 3.12.3
BIBLIOTECAS:
import os
import random
import threading
import speech_recognition as sr			SpeechRecognition==3.10.4	gTTS==2.5.1
import tkinter as tk
import PySimpleGUI as psg				PySimpleGUI==5.0.5			
import pyautogui as pag					PyAutoGUI==0.9.54
import datetime
import shutil							psutil==6.0.0
import win32com.client					pypiwin32==223
import pymsgbox							PyMsgBox==1.0.9
import pyperclip						pyperclip==1.8.2
import webbrowser
import google.generativeai as genai		google-generativeai==0.5.4
from time import sleep
from playsound3 import playsound		playsound3==2.2.1		PyAudio==0.2.14
from dotenv import load_dotenv			python-dotenv==1.0.1
	

ATIVAÇÃO:
Para fazer um pedido a AVA, use a palavra de ativação AVA.
Se preferir ouvir uma voz masculina, use a palavra LÉO.

FUNÇÕES QUE A AVA PODE REALIZAR:

ABRIR PROGRAMAS> 
WORD, EXCEL, POWERPOINT, CHROME, INTERNET EXPLORER, WORDPAD, BLOCO DE NOTAS, NOTEPAD ++, CALCULADORA, LUPA, GERENCIADOR DE ARQUIVOS, PAINTBRUSH, GERENCIADOR DE TAREFAS, WINDOWS MWDIA PLAYER E FERRAMENTA DE CAPTURA
Exemplos de como pedir: 
		Abre o Word.
		Abrir Excel
		Abra a calculadora e o gerenciador de tarefas pra mim.

ABRIR REDES SOCIAS> 
YOUTUBE, FACEBOOK, INSTAGRAM, TWITTER, LINKEDIN, REDDIT, PINTEREST, SNAPCHAT', TIKTOK, WHATSAPP, CHAT-GPT
Exemplos de como pedir: 
		Abre o Facebook e o Twitter.
		Abrir Excel, Tiktok e Whatsapp.
		Abra Snapchat por favor.

FAZER PESQUISA>
NO GOOGLE
NO GEMINI
NO YOUTUBE
Exemplos de como pedir: 
		Pesquise no Google quem é o presidente do Brasil.
		Pesquisa pra mim quantos anos tem a Microsoft
		Pesquisar no Gemini exemplos de listas em Python
		Pesquisar no youtube como programar em java.
Usando o comando Me dê:
		Me dê um código em java que acesse um banco de dados./>a pesquisa será feita no GEMINI

FAZER CONTAS SIMPLES>
ADIÇÃO, SUBTRAÇÃO, MULTIPLICAÇÃO E DIVISÃO
Exemplos de como pedir: 
		Use a palavra chave QUANTO
		Quanto é 4x5?
		Quanto é 1022+37?

ORGANIZAR ARQUIVOS EM PASTAS POR TIPO DE EXTENSÃO DO ARQUIVO>
Exemplos de como pedir: 
		Organize meus downloads.
		Organiza meu documentos.
		Orgazia essa pasta.
		Organiza a pasta receitas.

TOCAR MÚSICAS NO YOUTUBE>
Exemplos de como pedir: 
		Tocar Believer de Imagine Dragons.
		Tocar Aquarela
		Tocar o hino do São Paulo

CONTROLAR TECLADO E MOUSE>
Exemplos de como pedir: 
		Primeiro diga: CONTROLE TOTAL
		A partir daí existem varios comando para movimentar mouse e teclado:
			teclado:>
					1. alt tab
					2. tab
					3. menu
					4. voltar
					5. refazer
					6. recortar
					7. clicar
					8. duplo click
					9. escreve	...e diga o que deseja escrever
					10. enter
					11. trocar janela
					12. fechar janela
					13. esc
					14. área de trabalho
					15. copiar
					16. colar
					17. sobe
					18. desce
					19. esquerda
					20. direita
			mouse:>
					1. centro
					2. centro direita
					3. centro esquerda
					4. mouse direita
					5. mouse esquerda
					6. subir
					7. descer
					8. primeiro quadrante
					9. segundo quadrante
					10. terceiro quadrante
					11. quarto quadrante
					
LER>
	NO MODO CONTROLE TOTAL USE A FUNÇÃO LEIA PARA LER O TEXTO SELECIONADO
		DIGA: LEIA
	PARA TEXTOS GRANDES USE A FUNÇÃO LER
		DIGAR: LER
		VOCÊ PODE INTERROMPER A LEITURA DIZENDO UMA DAS PALAVRAS:
		['pare','para','tá bom','pode parar','chega']
		

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
			ATENÇÃO!!!
PARA USAR A API DO GEMINI É PRECISO FAZER UM CADASTRO NO SITE E SOLICITAR UMA CHAVE DE ACESSO E SALVÁ-LA NA SUA VARIÁVEL DE AMBIENTE
PARA UTILIZAR A BIBLIOTECA PySimpleGUI RESPONSÁVEL PELA TELA PRINCIPAL, É NECESSÁRIO UM CADASTRO NO SITE DOS CRIADORES PARA PEGAR CHAVE DE ACESSO.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
A AVA É FRUTO DO TRABALHO DE GRADUAÇÃO E ESTÁ LIBERA PELOS AUTORES PARA REPRODUÇÃO E MELHORIAS.
		
