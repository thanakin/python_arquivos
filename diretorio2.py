# !/usr/bin/python3
import os

#renomeia a pasta "nova_pasta" para "nova_pasta2"
    #os.rename("nova_pasta", "nova_pasta2")

#remove a "pasta nova_pasta2", se estiver vazia
    #os.rmdir("nova_pasta2")

#remove arquivos "exemplo.txt"
    #os.remove("exemplo.txt")

#retorna para pasta anterior
    #os.chdir("..")

print(os.getcwd())
'''
#laço para exibição "mais organizada" de arquivos e pastas
for arquivooupasta in os.listdir("."):
    print(arquivooupasta)
'''

for arquivooupasta in os.listdir("."):
    if os.path.isdir(arquivooupasta):
        print("Diretorio.:", arquivooupasta)
    elif os.path.isfile(arquivooupasta):
        print("Arquivo.:", arquivooupasta)