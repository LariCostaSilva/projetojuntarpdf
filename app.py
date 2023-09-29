"""Criar Solução para juntar PDF"""
import os
from PyPDF2 import PdfReader, PdfWriter

# Pasta para buscar os arquivos originais
PASTA_ORIGEM = 'C:/Users/larissa/Desktop/origem'

# Pasta contento o arquivo base que será mergeado ao arquivo principal
PASTA_JUNTAR = 'C:/Users/larissa/Desktop/juntarPDF'

# Pasta de destino aonde o arquivo final ficará guardado
PASTA_DESTINO = 'C:/Users/larissa/Desktop/resultado'

# Verifica se a pasta de destino exista, se não, crie-a
if not os.path.exists(PASTA_DESTINO):
    os.makedirs(PASTA_DESTINO)

# Lista dos nomes dos arquivos PDF na pasta de origem
arquivos_na_pasta_origem = os.listdir(PASTA_ORIGEM)

# Loop pelos arquivos na pasta de origem
for arquivo_na_pasta_origem in arquivos_na_pasta_origem:
    # É um arquivo PDF?
    if arquivo_na_pasta_origem.endswith('.pdf'):
        # Caminho completo para o arquivo PDF na pasta de origem
        caminho_arquivo_origem = os.path.join(PASTA_ORIGEM, arquivo_na_pasta_origem)
        
        # Caminho completo para o arquivo PDF na pasta de destino
        caminho_arquivo_destino = os.path.join(PASTA_DESTINO, arquivo_na_pasta_origem)
        
        # Abre o arquivo PDF 
        pdf_origem = PdfReader(caminho_arquivo_origem)
        
        # Abre o arquivo PDF da pasta de junção
        pdf_juntar = PdfReader(os.path.join(PASTA_JUNTAR, 'arquivo_para_juntar.pdf'))
        
        # Cria um novo arquivo na pasta resultado
        pdf_resultante = PdfWriter()
        
        # Adiciona todas as páginas do arquivo da pasta de origem ao arquivo resultante
        for pagina in pdf_origem.pages:
            pdf_resultante.add_page(pagina)  # Usa o  add_page em vez de addPage para isso
        
        # Adiciona todas as páginas do arquivo da pasta de junção ao arquivo resultante
        for pagina in pdf_juntar.pages:
            pdf_resultante.add_page(pagina)  # Usa o add_page em vez de addPage para isso
        
        # Salva o arquivo final (mergeado) PDF resultante na pasta de destino
        with open(caminho_arquivo_destino, 'wb') as arquivo_resultante:
            pdf_resultante.write(arquivo_resultante)
