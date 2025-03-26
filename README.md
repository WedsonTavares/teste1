# Documentação - Web Scraping e Processamento dos Anexos da ANS

## Objetivo

Este repositório contém um código Python para realizar web scraping no site da Agência Nacional de Saúde Suplementar (ANS). O script acessa a página específica da ANS, faz o download dos **Anexos I e II** em formato PDF, e os compacta em um único arquivo ZIP. O código foi projetado para automatizar a coleta de dados e melhorar a eficiência do processo.

## Funcionalidades

- **Acesso à página da ANS:** O código acessa a página de atualização do Rol de Procedimentos da ANS.
- **Download dos Anexos I e II:** Baixa os PDFs diretamente do site.
- **Compactação dos arquivos PDF:** Compacta os PDFs em um único arquivo ZIP.
- **Estrutura de Pastas:** Todos os arquivos são salvos e organizados automaticamente em pastas como `anexos` e `resultados`.
- **Extração e modificação:** O script também permite extrair dados dos PDFs, criar um CSV com as informações e modificar as abreviações das colunas conforme necessário.

---

## Como Usar

### Passo 1: Clonar o Repositório

Passo 1. Abra o terminal e execute o seguinte comando para clonar o repositório:

```bash
git clone https://github.com/WedsonTavares/teste1.git
```
Navegue para o diretório do repositório clonado:

```bash
cd teste1
```

Passo 2: Criar e Ativar o Ambiente Virtual (Recomendado)
Criar o ambiente virtual:

```bash
python -m venv venv
```
Ativar o ambiente virtual:

```bash
.\venv\Scripts\Activate
```

Passo 3: Instalar as Dependências

```bash
pip install requests pdfplumber pandas
```

Passo 4: Executar o Código

Este comando vai:

Acessar o site da ANS.

Baixar os arquivos PDF Anexo I e Anexo II.

Compactá-los em um arquivo ZIP.

Salvar todos o aquivo zipado na pasta resultados.






