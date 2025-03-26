import os
import requests
from bs4 import BeautifulSoup
from zipfile import ZipFile

# URL do site onde os anexos estão localizados
url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"

# Função para baixar os arquivos PDF
def baixar_pdf(url_pdf, nome_arquivo):
    response = requests.get(url_pdf)
    with open(nome_arquivo, 'wb') as f:
        f.write(response.content)
    print(f"Arquivo {nome_arquivo} baixado com sucesso!")

# Função para criar o arquivo ZIP
def compactar_arquivos(arquivos, nome_arquivo_zip):
    os.makedirs('resultados', exist_ok=True)
    with ZipFile(nome_arquivo_zip, 'w') as zipf:
        for arquivo in arquivos:
            zipf.write(arquivo, os.path.basename(arquivo))
            print(f"Arquivo {arquivo} adicionado ao zip.")
    print(f"Arquivos compactados e enviados para a pasta 'resultados' no arquivo {nome_arquivo_zip} com sucesso!")

# Acessando o site e coletando os links dos PDFs
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Procurando por links para os PDFs (Ajuste a busca conforme o site)
pdf_links = []
for link in soup.find_all('a', href=True):
    href = link['href']
    if 'pdf' in href:
        if 'Anexo I' in link.text:
            pdf_links.append(href)
        elif 'Anexo II' in link.text:
            pdf_links.append(href)

# Baixar os PDFs
arquivos_baixados = []
for i, pdf_link in enumerate(pdf_links):
    nome_arquivo = f"anexo_{i+1}.pdf"
    if not pdf_link.startswith('http'):
        pdf_link = 'https://www.gov.br' + pdf_link
    baixar_pdf(pdf_link, nome_arquivo)
    arquivos_baixados.append(nome_arquivo)

# Compactando os arquivos
compactar_arquivos(arquivos_baixados, 'resultados/anexos.zip')

# Remover os arquivos PDF originais após compactação
for arquivo in arquivos_baixados:
    os.remove(arquivo)
    print(f"Arquivo {arquivo} removido após compactação.")
