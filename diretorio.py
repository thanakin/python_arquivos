# !/usr/bin/python3
import os
#exibe caminho até o diretorio atual
print(os.getcwd())

#exibe arquivos e pastas no diretorio atual
print(os.listdir("."))

#exibe conteudo de uma pasta "teste_pasta"
print(os.listdir("teste_pasta"))

#criando pasta "nova_pasta"
os.mkdir("nova_pasta")

#entra na pasta informada "nova_pasta"
os.chdir("nova_pasta")
print(os.getcwd())
print(os.listdir("."))

#abre(cria se não existir) o arquivo "teste.txt" em modo escrita "w" e o fecha em seguida
open("teste.txt", "w").close()

#cria subpastas "outro_teste/teste2/teste3"
os.makedirs("outro_teste/teste2/teste3")