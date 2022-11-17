#Import 
from datetime import *
from MenuCantores import *
from MenuMúsicas import *
from MenuGravações import *
from MenuRelatório import *

# FUNÇÕES
# VERIFICAÇÂO DE ARQUIVOS
def Informações(DicionarioMusicas, DicionarioCantores, DicionarioGravacoes):
    ExisteMusica = Verificação_Musicas("musicas.txt")
    ExisteCantor = Verificação_Cantores("cantores.txt")
    ExisteGravação = Verificação_Gravações("gravacoes.txt")
    if ExisteMusica == True:
        DicionarioMusicas = DadosMusica(DicionarioMusicas)
    if ExisteCantor == True:
        DicionarioCantores = DadosCantor(DicionarioCantores)
    if ExisteGravação == True:
        DicionarioGravacoes = DadosGravação(DicionarioGravacoes)
        
    return

    
#Verificação do Arquivo de Musicas
def Verificação_Musicas(nome):
    import os
    if os.path.exists(nome):
        return True
    else:
        return False

#Verificação do Arquivo de Cantores
def Verificação_Cantores(nome):
    import os
    if os.path.exists(nome):
        return True
    else:
        return False

#Verificação do Arquivo de Gravações
def Verificação_Gravações(nome):
    import os
    if os.path.exists(nome):
        return True
    else:
        return False

#SALVANDO DADOS DA MUSICA
def DadosMusica(DicionarioMusicas):
    musica = open("musicas.txt", "r")
    linha = musica.readline()
    while (linha != ""):
        DadosMusica = []
        linha = linha[:len(linha)-1]
        dados = linha.split("|")
        Titulo = dados[0]
        Data = dados[1]
        estilo = dados[2]
        duracao = dados[3]
        duracao = int(duracao)
        compositor = dados[4]
        DadosMusica.append(Data)
        DadosMusica.append(estilo)
        DadosMusica.append(duracao)
        DadosMusica.append(compositor)
        DicionarioMusicas[Titulo] = DadosMusica
        linha = musica.readline()
    musica.close()
    return

#Salvando Dados Do Cantor
def DadosCantor(DicionarioCantores):
    cantor = open("cantores.txt", "r")
    linha = cantor.readline()
    while (linha != ""):
        DadosCantor = []
        linha = linha[:len(linha)-1]
        dados = linha.split("|")
        NomeArtistico = dados[0]
        NomeReal = dados[1]
        Data = dados[2]
        Email = dados[3]
        numero = dados[4]
        DadosCantor.append(NomeReal)
        DadosCantor.append(Data)
        DadosCantor.append(Email)
        DadosCantor.append(numero)
        DicionarioCantores[NomeArtistico] = DadosCantor
        linha = cantor.readline()
    cantor.close()
    return

#Salvando Dados Das Gravações
def DadosGravação(DicionarioGravacoes):
    gravacao = open("gravacoes.txt", "r")
    linha = gravacao.readline()
    while (linha != ""):
        DadosGravação = []
        linha = linha[:len(linha)-1]
        dados = linha.split("|")
        Titulo = dados[0]
        NomeArtistico = dados[1]
        Data = dados[2]
        album = dados[3]
        instrumentos = dados[4]
        instrumentos = instrumentos.split()
        tupla = (Titulo, NomeArtistico, Data)
        DadosGravação.append(album)
        DadosGravação.append(instrumentos)
        DicionarioGravacoes[tupla] = DadosGravação
        linha = gravacao.readline()
    gravacao.close()
    return
    

#PROGRAMA PRINCIPAL
def Menu_Principal():
    
    # VARIAVEIS
    DicionarioMusicas = {}
    DicionarioCantores = {}
    DicionarioGravacoes = {}
    Informações(DicionarioMusicas, DicionarioCantores, DicionarioGravacoes)

    # REPETIÇÃO
    opcao = 0
    while (opcao > 0) or (opcao < 6):
        print("--- Bem-vindo ao StudioMusics ---\n")
        print("1. Submenu de Músicas")
        print("2. Submenu de Cantores")
        print("3. Submenu de Gravações")
        print("4. Submenu Relatórios")
        print("5. Sair")
        opcao = int(input("\n--- Escolha uma opção: "))
        while (opcao > 5) or (opcao < 1):
            opcao = int(input("\nNumero Invalido! \nEscolha uma opção: "))

        # SUBMENU DE MUSICAS
        if opcao == 1:
            print("=================================")
            Submenu_de_Musicas(
                DicionarioMusicas, DicionarioGravacoes)

        # SUBMENU DE CANTORES
        if opcao == 2:
            print("=================================")
            Submenu_de_Cantores(
                DicionarioCantores, DicionarioGravacoes)

        # SUBMENU DE GRAVAÇÕES
        if opcao == 3:
            print("=================================")
            Submenu_de_Gravacoes(
                DicionarioMusicas, DicionarioCantores, DicionarioGravacoes)

        # SUBMENU DE RELATORIOS
        if opcao == 4:
            print("=================================")
            Submenu_de_Relatorios(
                DicionarioMusicas, DicionarioCantores, DicionarioGravacoes)

        # SAIR DO PROGRAMA
        if opcao == 5:
            print("\n --- Encerrando Programa --- ")
            return

# CALCULADORA DE MINUTOS E SEGUNDOS

def SegundosMinutos(Tempo):
    minutos = Tempo//60
    segundos = Tempo % 60
    return(segundos, minutos)

# PROGRAMA PRINCIPAL
Menu_Principal()
