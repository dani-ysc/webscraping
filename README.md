# Webscraping de produtos de sites de e-commerce

## Sobre

Black Friday é uma ótima época para comprar produtos que a gente precisa/deseja. Porém, no Brasil, há um histórico dos websites aumentarem os preços progressivamente, para que no dia da Black Friday os preços estejam em "promoção" com o valor base que aquele produto tinha há alguns meses. Este projeto consiste em realizar webscraping de alguns produtos de meu interesse, retirar seu nome, seu valor à vista e à prazo de sites de e-commerce, e salvá-los em um arquivo CSV. Realizar a limpeza dos dados utilizando a biblioteca pandas, do python. E desenvolver uma DAG com Apache Airflow para realizar todo o workflow do projeto a cada 3 dias, consolidando a criação de uma ETL (Extract, Transform and Load).

## Pré requisitos

1. Criar um ambiente virtual Python
2. Instalar as bibliotecas que serão utilizadas no projeto no seu ambiente virtual


##  Webscraping no site da Magazine Luíza

O <a href="https://github.com/dani-ysc/webscraping/blob/main/webscraping_magalu.py">arquivo</a> contém o script com python para retirar os produtos dos sites. 
