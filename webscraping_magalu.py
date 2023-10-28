import pandas as pd
from bs4 import BeautifulSoup as BS
import requests
from datetime import datetime as dt


# Data que foi realizada o scraping de dados
today = dt.today()
current_date = today.date()

# Criando uma lista vazia para salvar os dados
data = {
    "nome": [],
    "preço à vista": [],
    "preço à prazo": [],
}

# Criar funções para reter a informação dos produtos de uma forma mais organizada
def nome_produto(tag, atributo):
    nome_item = soup.find(tag, class_ = atributo)
    data["nome"] += nome_item

def preco_avista_produto(tag, atributo): 
    preco_avista_item = soup.find(tag, class_ = atributo)
    data["preço à vista"] += preco_avista_item

def preco_prazo_produto(tag, atributo): 
    preco_prazo_item = soup.find(tag, class_ = atributo)
    data["preço à prazo"] += preco_prazo_item

# Scrapar dados do microondas 'Electrolux 27L Ms37R' na black friday no Magazine Luíza
url1 = 'https://www.magazineluiza.com.br/micro-ondas-electrolux-27l-ms37r/p/221169600/ed/mond/'
response = requests.get(url1)
html_doc = response.text
soup = BS(html_doc, 'html.parser')

nome_produto('h1')
preco_avista_produto('p', 'sc-kpDqfm eCPtRw sc-hoLEA kXWuGr')
preco_prazo_produto('p', 'sc-kpDqfm iohXR sc-iSrTKI dyXeG')

# Scrapar dados da panela de pressão elétrica
url2 = 'https://www.magazineluiza.com.br/panela-de-pressao-eletrica-electrolux-digital-pcc20-1000w-6l-controle-de-temperatura/p/023301500/ep/eppe/'
response2 = requests.get(url2)
html_doc2 = response2.text
soup = BS(html_doc2, 'html.parser')

nome_produto('h1', 'sc-kpDqfm gXZPqL')
preco_avista_produto('p', 'sc-kpDqfm eCPtRw sc-hoLEA kXWuGr')
preco_prazo_produto('p', 'sc-kpDqfm iohXR sc-iSrTKI dyXeG')

# Scrapar dados de notebook (mais barato -- R$3000) na black friday
url3 = 'https://www.magazineluiza.com.br/notebook-lenovo-ideapad-3i-intel-core-i5-8gb-256gb-ssd-156-full-hd-windows-11-82md0007br/p/235631700/in/note/'
response3 = requests.get(url3)
html_doc3 = response3.text
soup = BS(html_doc3, "html.parser")

nome_produto('h1', 'sc-kpDqfm gXZPqL')
preco_avista_produto('p', 'sc-kpDqfm eCPtRw sc-hoLEA kXWuGr')
preco_prazo_produto('p', 'sc-kpDqfm iohXR sc-iSrTKI dyXeG')

# Scrapar dados de notebook (mais caro -- R$3500) na black friday
url4 = 'https://www.magazineluiza.com.br/notebook-gamer-lenovo-gaming-3i-intel-core-i5-8gb-512gb-ssd-155-fullhd-nvidia-gtx-1650-windows-11/p/235631800/in/note/'
response4 = requests.get(url4)
html_doc4 = response4.text
soup = BS(html_doc4, 'html.parser')

nome_produto('h1', 'sc-kpDqfm gXZPqL')
preco_avista_produto('p', 'sc-kpDqfm eCPtRw sc-hoLEA kXWuGr')
preco_prazo_produto('p', 'sc-kpDqfm iohXR sc-iSrTKI dyXeG')

# Scrapar dados de uma cafeteira
url5 = 'https://www.magazineluiza.com.br/cafeteira-expresso-19-bar-oster-primalatte-vermelho/p/217159000/ep/cfex/'
response5 = requests.get(url5)
html_doc5 = response5.text
soup = BS(html_doc5, 'html.parser')

nome_produto('h1', 'sc-kpDqfm gXZPqL')
preco_avista_produto('p', 'sc-kpDqfm eCPtRw sc-hoLEA kXWuGr')
preco_prazo_produto('p', 'sc-kpDqfm iohXR sc-iSrTKI dyXeG')

# Scrapar dados de um iPhone 14 Pro
url6 = 'https://www.magazineluiza.com.br/apple-iphone-14-pro-256gb-dourado-61-48mp/p/235923800/te/i14p/'
response6 = requests.get(url6)
html_doc6 = response6.text
soup = BS(html_doc6, 'html.parser')

nome_produto('h1', 'sc-kpDqfm gXZPqL')
preco_avista_produto('p', 'sc-kpDqfm eCPtRw sc-hoLEA kXWuGr')
preco_prazo_produto('p', 'sc-kpDqfm iohXR sc-iSrTKI dyXeG')


# Scrapar dados de um Apple Watch Series 8
url7 = 'https://www.magazineluiza.com.br/apple-watch-series-8-41mm-gps-cellular-caixa-estelar-aluminio-pulseira-esportiva/p/235931400/te/smtw/'
response7 = requests.get(url7)
html_doc7 = response7.text
soup = BS(html_doc7, 'html.parser')

nome_produto('h1', 'sc-kpDqfm gXZPqL')
preco_avista_produto('p', 'sc-kpDqfm eCPtRw sc-hoLEA kXWuGr')
preco_prazo_produto('p', 'sc-kpDqfm iohXR sc-iSrTKI dyXeG')

# Scrapar dados do Samsung Galaxy S23 Ultra
url8 = 'https://www.magazineluiza.com.br/smartphone-samsung-galaxy-s23-ultra-256gb-preto-5g-12gb-ram-68-cam-quadrupla-selfie-12mp/p/232855300/te/s23u/'
response8 = requests.get(url8)
html_doc8 = response8.text
soup = BS(html_doc8, 'html.parser')

nome_produto('h1', 'sc-kpDqfm gXZPqL')
preco_avista_produto('p', 'sc-kpDqfm eCPtRw sc-hoLEA kXWuGr')
preco_prazo_produto('p', 'sc-kpDqfm iohXR sc-iSrTKI dyXeG')

# Scrapar dados da lavadora de roupas
url9 = 'https://www.magazineluiza.com.br/lavadora-de-roupas-consul-12kg-16-programas-de-lavagem-branca-cwh12bb/p/236161100/ed/lava/'
response9 = requests.get(url9)
html_doc9 = response9.text
soup = BS(html_doc9, 'html.parser')

nome_produto('h1', 'sc-kpDqfm gXZPqL')
preco_avista_produto('p', 'sc-kpDqfm eCPtRw sc-hoLEA kXWuGr')
preco_prazo_produto('p', 'sc-kpDqfm iohXR sc-iSrTKI dyXeG')

# Scrapar dados de uma televisão
url10 = 'https://www.magazineluiza.com.br/smart-tv-55-4k-oled-samsung-qn55s90ca-144hz-wi-fi-bluetooth-com-alexa-4-hdmi-2-usb/p/237449500/et/tv4k/'
response10 = requests.get(url10)
html_doc10 = response10.text
soup = BS(html_doc10, 'html.parser')

nome_produto('h1', 'sc-kpDqfm gXZPqL')
preco_avista_produto('p', 'sc-kpDqfm eCPtRw sc-hoLEA kXWuGr')
preco_prazo_produto('p', 'sc-kpDqfm iohXR sc-iSrTKI dyXeG')

# Criando um DataFrame
df = pd.DataFrame(data)
# Salvando o DataFrame em um formato .CSV
df.to_csv(f'dados_{current_date}.csv', sep=',', index=True)
