import pandas as pd
from bs4 import BeautifulSoup as BS
import requests

# Criando uma lista vazia para salvar os dados
data = {
    "nome": [],
    "preço à vista": [],
    "preço à prazo": [],
}

# Scrapar dados do microondas 'Electrolux 27L Ms37R' na black friday no Magazine Luíza
url1 = 'https://www.magazineluiza.com.br/micro-ondas-electrolux-27l-ms37r/p/221169600/ed/mond/'
response = requests.get(url1)
html_doc = response.text
soup = BS(html_doc, 'html.parser')

# Retirando o nome do microondas da página
nome_microondas = soup.find('h1')
data['nome'] += nome_microondas

# Retirando o preço do microondas à vista da página
preco_microondas = soup.find('p', class_='sc-kpDqfm eCPtRw sc-hoLEA kXWuGr')
data['preço à vista'] += preco_microondas

# Retirando o preço do microondas à prazo da página
preco_prazo_microondas = soup.find('p', class_ = 'sc-kpDqfm iohXR sc-iSrTKI dyXeG')
data['preço à prazo'] += preco_prazo_microondas

# Scrapar dados da panela de pressão elétrica
url2 = 'https://www.magazineluiza.com.br/panela-de-pressao-eletrica-electrolux-digital-pcc20-1000w-6l-controle-de-temperatura/p/023301500/ep/eppe/'
response2 = requests.get(url2)
html_doc2 = response2.text
soup2 = BS(html_doc2, 'html.parser')

# Retirando o nome da panela de pressão
nome_panela_de_pressao = soup2.find('h1', class_ = 'sc-kpDqfm gXZPqL')
data['nome'] += nome_panela_de_pressao

# Retirando o preço à vista da panela de pressão
preco_panela_de_pressao = soup2.find('p', class_ = 'sc-kpDqfm eCPtRw sc-hoLEA kXWuGr')
data['preço à vista'] += preco_panela_de_pressao

# Retirando o preço à prazo da panela de pressão
preco_prazo_panela_de_pressao = soup2.find('p', class_ = 'sc-kpDqfm iohXR sc-iSrTKI dyXeG')
data['preço à prazo'] += preco_prazo_panela_de_pressao

# Scrapar dados de notebook (mais barato -- R$3000) na black friday
url3 = 'https://www.magazineluiza.com.br/notebook-lenovo-ideapad-3i-intel-core-i5-8gb-256gb-ssd-156-full-hd-windows-11-82md0007br/p/235631700/in/note/'
response3 = requests.get(url3)
html_doc3 = response3.text
soup3 = BS(html_doc3, "html.parser")

# Retirando o nome do notebook custo benefício
nome_notebook_cb = soup3.find('h1', class_ = 'sc-kpDqfm gXZPqL')
data['nome'] += nome_notebook_cb

# Retirando o preço do notebook custo benefício à vista
preco_notebook_cb = soup3.find('p', class_ = 'sc-kpDqfm eCPtRw sc-hoLEA kXWuGr')
data['preço à vista'] += preco_notebook_cb

# Retirando o preço do notebook custo benefício à prazo
preco_prazo_notebook_cb = soup3.find('p', class_ = 'sc-kpDqfm iohXR sc-iSrTKI dyXeG')
data['preço à prazo'] += preco_prazo_notebook_cb

# Scrapar dados de notebook (mais caro -- R$3500) na black friday
url4 = 'https://www.magazineluiza.com.br/notebook-gamer-lenovo-gaming-3i-intel-core-i5-8gb-512gb-ssd-155-fullhd-nvidia-gtx-1650-windows-11/p/235631800/in/note/'
response4 = requests.get(url4)
html_doc4 = response4.text
soup4 = BS(html_doc4, 'html.parser')

# Retirando o nome do notebook gamer
nome_notebook_gamer = soup4.find('h1', class_ = 'sc-kpDqfm gXZPqL')
data['nome'] += nome_notebook_gamer

# Retirando o preço à vista do notebook gamer
preco_notebook_gamer = soup4.find('p', class_ = 'sc-kpDqfm eCPtRw sc-hoLEA kXWuGr')
data['preço à vista'] += preco_notebook_gamer

# Retirando o preço à prazo do notebook gamer
preco_prazo_notebook_gamer = soup4.find('p', class_ = 'sc-kpDqfm iohXR sc-iSrTKI dyXeG')
data['preço à prazo'] += preco_prazo_notebook_gamer

# Scrapar dados de uma cafeteira
url5 = 'https://www.magazineluiza.com.br/cafeteira-expresso-19-bar-oster-primalatte-vermelho/p/217159000/ep/cfex/'
response5 = requests.get(url5)
html_doc5 = response5.text
soup5 = BS(html_doc5, 'html.parser')

# Retirando o nome da cafeteira
nome_cafeteira = soup5.find('h1', class_ = 'sc-kpDqfm gXZPqL')
data['nome'] += nome_cafeteira

# Retirando o preço à vista da cafeteira
preco_cafeteira = soup5.find('p', class_ = 'sc-kpDqfm eCPtRw sc-hoLEA kXWuGr')
data['preço à vista'] += preco_cafeteira

# Retirando o preço à prazo da cafeteira
preco_prazo_cafeteira = soup5.find('p', class_ = 'sc-kpDqfm iohXR sc-iSrTKI dyXeG')
data['preço à prazo'] += preco_prazo_cafeteira

# Scrapar dados de um iPhone 14 Pro
url6 = 'https://www.magazineluiza.com.br/apple-iphone-14-pro-256gb-dourado-61-48mp/p/235923800/te/i14p/'
response6 = requests.get(url6)
html_doc6 = response6.text
soup6 = BS(html_doc6, 'html.parser')

# Retirando o nome do iPhone
nome_iphone = soup6.find('h1', class_ = 'sc-kpDqfm gXZPqL')
data['nome'] += nome_iphone

# Retirando o preço à vista do iPhone
preco_iphone = soup6.find('p', class_ = 'sc-kpDqfm eCPtRw sc-hoLEA kXWuGr')
data['preço à vista'] += preco_iphone

# Retirando o preço à prazo do iPhone
preco_prazo_iphone = soup6.find('p', class_ = 'sc-kpDqfm iohXR sc-iSrTKI dyXeG')
data['preço à prazo'] += preco_prazo_iphone

# Scrapar dados de um Apple Watch Series 8
url7 = 'https://www.magazineluiza.com.br/apple-watch-series-8-41mm-gps-cellular-caixa-estelar-aluminio-pulseira-esportiva/p/235931400/te/smtw/'
response7 = requests.get(url7)
html_doc7 = response7.text
soup7 = BS(html_doc7, 'html.parser')

# Retirando o nome do Apple Watch
nome_applewatch = soup7.find('h1', class_ = 'sc-kpDqfm gXZPqL')
data['nome'] += nome_applewatch

# Retirando o preço à vista do Apple Watch
preco_applewatch = soup7.find('p', class_ = 'sc-kpDqfm eCPtRw sc-hoLEA kXWuGr')
data['preço à vista'] += preco_applewatch

# Retirando o preço à prazo do Apple Watch
preco_prazo_applewatch = soup7.find('p', class_ = 'sc-kpDqfm iohXR sc-iSrTKI dyXeG')
data['preço à prazo'] += preco_prazo_applewatch

# Scrapar dados do Samsung Galaxy S23 Ultra
url8 = 'https://www.magazineluiza.com.br/smartphone-samsung-galaxy-s23-ultra-256gb-preto-5g-12gb-ram-68-cam-quadrupla-selfie-12mp/p/232855300/te/s23u/'
response8 = requests.get(url8)
html_doc8 = response8.text
soup8 = BS(html_doc8, 'html.parser')

# Retirando o nome do S23 Ultra
nome_s23ultra = soup8.find('h1', class_ = 'sc-kpDqfm gXZPqL')
data['nome'] += nome_s23ultra

# Retirando o preço à vista do S23 Ultra
preco_s23ultra = soup8.find('p', class_ = 'sc-kpDqfm eCPtRw sc-hoLEA kXWuGr')
data['preço à vista'] += preco_s23ultra

# Retirando o preço à prazo do S23 Ultra
preco_prazo_s23ultra = soup8.find('p', class_ = 'sc-kpDqfm iohXR sc-iSrTKI dyXeG')
data['preço à prazo'] += preco_prazo_s23ultra

# Scrapar dados da lavadora de roupas
url9 = 'https://www.magazineluiza.com.br/lavadora-de-roupas-consul-12kg-16-programas-de-lavagem-branca-cwh12bb/p/236161100/ed/lava/'
response9 = requests.get(url9)
html_doc9 = response9.text
soup9 = BS(html_doc9, 'html.parser')

# Retirando o nome da lavadora de roupas
nome_lavadora = soup9.find('h1', class_ = 'sc-kpDqfm gXZPqL')
data['nome'] += nome_lavadora

# Retirando o preço à vista da lavadora de roupas
preco_lavadora = soup9.find('p', class_ = 'sc-kpDqfm eCPtRw sc-hoLEA kXWuGr')
data['preço à vista'] += preco_lavadora

# Retirando o preço à prazo da lavadora de roupas
preco_prazo_lavadora = soup9.find('p', class_ = 'sc-kpDqfm iohXR sc-iSrTKI dyXeG')
data['preço à prazo'] += preco_prazo_lavadora

# Scrapar dados de uma televisão
url10 = 'https://www.magazineluiza.com.br/smart-tv-55-4k-oled-samsung-qn55s90ca-144hz-wi-fi-bluetooth-com-alexa-4-hdmi-2-usb/p/237449500/et/tv4k/'
response10 = requests.get(url10)
html_doc10 = response10.text
soup10 = BS(html_doc10, 'html.parser')

# Retirando o nome da televisão
nome_tv = soup10.find('h1', class_ = 'sc-kpDqfm gXZPqL')
data['nome'] += nome_tv

# Retirando o preço à vista da televisão
preco_tv = soup10.find('p', class_ = 'sc-kpDqfm eCPtRw sc-hoLEA kXWuGr')
data['preço à vista'] += preco_tv

# Retirando o preço à prazo da televisão
preco_prazo_tv = soup10.find('p', class_ = 'sc-kpDqfm iohXR sc-iSrTKI dyXeG')
data['preço à prazo'] += preco_prazo_tv


# Criando um DataFrame
df = pd.DataFrame(data)
# Salvando o DataFrame em um formato .CSV
df.to_csv('dados.csv', sep=',', index=True)
