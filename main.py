import requests, zipfile, io
from bs4 import BeautifulSoup

blob = requests.get("https://arquivos.receitafederal.gov.br/dados/cnpj/dados_abertos_cnpj/2024-11/")

tst = blob.text

soup = BeautifulSoup(tst, 'html.parser')
links = soup.find_all('a', href=True)

listaUrl = []
for link in links:
    listaUrl.append(link['href'])

linksParaDownload = listaUrl[5:]
i = 0
teste = "https://arquivos.receitafederal.gov.br/dados/cnpj/dados_abertos_cnpj/2024-11/"+ linksParaDownload[i]
for link in linksParaDownload:
    teste = "https://arquivos.receitafederal.gov.br/dados/cnpj/dados_abertos_cnpj/2024-11/"+ linksParaDownload[i]
    r = requests.get(teste)
    z = zipfile.ZipFile(io.BytesIO(r.content), "r")
    z.extractall()
    i = i + 1 



# Esse puxa um simples arquivo.

#r = requests.get("https://arquivos.receitafederal.gov.br/dados/cnpj/dados_abertos_cnpj/2024-11/Cnaes.zip")
#z = zipfile.ZipFile(io.BytesIO(r.content), "r")
#z.extractall() 


