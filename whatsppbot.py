#importar as bibliotecas
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

# Google Chrome
driver = webdriver.Chrome(ChromeDriverManager().install())

#Navegar até whatsapp web
driver.get('https://web.whatsapp.com/')

# Tempo de espera para ler QrCode
time.sleep(5)

#Definir Grupos e contatos a serem buscados.
#Para buscar mais de um contato ou grupo passa nome entre virtula ex: ['Grupo de teste','Maria', 'Pedro']
contatos = ['Grupo de teste']
mensagem = 'Olá tudo bem? seja bem vindo ao grupo de teste'

#Tempo de espera.
timePause = 2;

# Função para buscar contato ou grupo
def buscar_contatos(contato):
    campo_pesquisa = driver.find_element_by_xpath('//div[contains(@class, "copyable-text selectable-text")]')
    campo_pesquisa.click()
    time.sleep(timePause)
    
    campo_pesquisa.send_keys(contato)
    time.sleep(timePause)
    campo_pesquisa.send_keys(Keys.ENTER)

# Enviando mensagem após selecionar o contato
def enviar_mensagem(mensagem):
    campo_mensagem = driver.find_elements_by_xpath('//div[contains(@class, "copyable-text selectable-text")]')
    campo_mensagem[1].click()
    time.sleep(timePause)
    
    campo_mensagem[1].send_keys(mensagem)
    time.sleep(timePause)
    
    campo_mensagem[1].send_keys(Keys.ENTER)
    time.sleep(timePause)

#Repedir para cada contato passado
for contato in contatos :
    buscar_contatos(contato)
    enviar_mensagem(mensagem)