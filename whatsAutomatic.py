#!/usr/bin/env python
# coding: utf-8
# Objetivo: ENVIAR MENSAGENS AUTOMÁTICAS NO WHATS USANDO PYTHON E SELENIUM
# Passo 01 - Importar BD contendo as colunas com os nomes, numeros (PPEECCCCCCCC) e as mensagens 
# Passo 02 - Logar no whatsapWeb no chrome
# Passo 03 - Ler e pegar os dados do BD importado e enviar a mensagem
###########################################################################################
# Passo 01 - Importar BD contendo o nome, numero e a mensagem a ser enviada

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time
import urllib #Codifica a menssagem

contatos_df = pd.read_excel("Enviar.xlsx")
#display(contatos_df)

# Passo 02 - Logar no whatsapweb

navegador = webdriver.Chrome(executable_path=r'./chromedriver.exe')
navegador.get("https://web.whatsapp.com/")

# Abrindo o QRcode do whats o usuario deverá fazer a leitura pelo phone
# Se o tamanho len() da lista de elementos "Side"  for menor do que 1,
# Quer dizer o ID “side” não foi encontrato, ou seja, não estamos logado no WhatsApp.
# Assim devera aguardar 1 segundo e fazer novamente a verificação 
# O laço é finalizado quando o o "slide" é econtrado  e  portando o login no WhatsApp for completado."

while len(navegador.find_elements_by_id("side")) < 1:
    time.sleep(1)

# com o login feito no whatsappWeb
# Passo 02 - Ler os dados do BD importado e enviar as msgs

for i, mensagem in enumerate(contatos_df['Mensagem']): # Para cada mensagem do bd faz:
    pessoa = contatos_df.loc[i, "Pessoa"] # Localiza o nome e atribui a pessoa
    numero = contatos_df.loc[i, "Número"] # Localiza o numero da pessoa e atribui a numero
    texto = urllib.parse.quote(f"Oi {pessoa}! {mensagem}") # codifica a mensagem formatada
    link = f"https://web.whatsapp.com/send?phone={numero}&text={texto}"
    navegador.get(link) # Entra na conversa do numero localizado com a msg
    while len(navegador.find_elements_by_id("side")) < 1: # Aguarda a pagina abrir completamente
        time.sleep(1)
        
    navegador.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]').send_keys(Keys.ENTER) # Envia a mensagem
    time.sleep(15)
