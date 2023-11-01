# Webscraping de produtos de sites de e-commerce

## Sobre

Black Friday é uma ótima época para comprar produtos que a gente precisa/deseja. Porém, no Brasil, há um histórico dos websites aumentarem os preços progressivamente, para que no dia da Black Friday os preços estejam em "promoção" com o valor base que aquele produto tinha há alguns meses. Este projeto consiste em realizar webscraping de alguns produtos de meu interesse, retirar seu nome, seu valor à vista e à prazo de sites de e-commerce, e salvá-los em um arquivo CSV. Realizar a limpeza dos dados utilizando a biblioteca pandas, do python. E desenvolver uma DAG com Apache Airflow para realizar todo o workflow do projeto a cada 3 dias, consolidando a criação de uma ETL (Extract, Transform and Load).

## Pré requisitos

1. Criar um ambiente virtual Python
2. Instalar as bibliotecas que serão utilizadas no projeto no seu ambiente virtual
3. Usar o método request GET para verificar se o site permite a retirada dos dados dele

### Criando um ambiente virtual em Python
Utilizando o comando abaixo, trocando os <> pelo nome do diretório em que ficará o ambiente virtual.

```
python -m venv <nome do diretório do ambiente virtual>
```

Ao realizar esse script no terminal, a versão mais recente de Python no seu computador será instalado no ambiente virtual. O próximo passo será a ativação do ambiente virtual, que pode ser feito através desse comando no terminal caso você esteja numa máquina com OS Windows:

```
\<diretório do ambiente virtual>\Scripts\Activate
```

O próximo passo será a instalação das bibliotecas que serão utilizadas para realização deste projeto.

### Instalando as bibliotecas no ambiente virtual
Para a instalação das bibliotecas necessárias para a realização do projeto, é recomendado a criação de um arquivo requirements.txt com as biliotecas necessárias e a versão delas. Verifique se o arquivo está na mesma pasta do ambiente virtual e digite o seguinte comando no terminal:

```
pip install -r requirements.txt
```

Caso você não saiba qual a versão das bibliotecas você possui no seu computador, vá ao terminal (sem estar com a máquina virtual ativada) e digite:
```
pip freeze
```
Como output, o terminal mostrará todos os pacotes instalados no seu computador e a versão utilizada.

##  Webscraping no site da Magazine Luíza

O arquivo <a href="https://github.com/dani-ysc/webscraping/blob/main/webscraping_magalu.py">webscraping_magalu.py</a> contém o script escrito em python para retirar os produtos dos sites. Os dados desses produtos com o nome, preço à vista e à prazo são salvos em um python dictionary e transformados num DataFrame usando a biblioteca pandas. Em seguida, esses dados são transformados em um arquivo .csv. Abaixo contém um pequeno esquema da tabela.

| nome | preço à vista | preço à prazo |
| --- | --- | --- |
| Micro-ondas Electrolux 27L MS37R | R$ 768,55 | R$ 809,00 |


