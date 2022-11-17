#Imports
from datetime import *

# SUBMENU DE RELATORIOS
def Submenu_de_Relatorios(DicionarioMusicas, DicionarioCantores, DicionarioGravacoes):
    # REPETIÇÃO
    opcao = 0
    while (opcao > 0) or (opcao < 3):
        print("   --- Submenu de Relatórios --- ")
        print("")
        print("1. Inserir Datas")
        print("2. Retornar Ao Menu Principal")
        opcao = int(input("\n Escolha Uma Opção: "))
        while (opcao > 2) or (opcao < 1):
            opcao = int(input("\nNumero Invalido \nEscolha Uma Opção: "))

        # ADICIONAR NOVA GRAVACAO
        if opcao == 1:
            print("\n --- Imprimindo Relatorio ---")
            Relatorio(DicionarioMusicas, DicionarioCantores,
                      DicionarioGravacoes)
            print("\n --- Encerrando Relatorio ---")
            print(" --- Voltando ao Submenu de Relatorios --- \n")
            print("============================================")

        # ALTERAR GRAVACAO JA EXISTENTE
        if opcao == 2:
            print("\n --- Voltando ao Menu... --- \n")
            print("============================================")
            return


def Relatorio(DicionarioMusicas, DicionarioCantores, DicionarioGravacoes):
    Data1 = []
    Data2 = []
    ListaChavesVerificadas = []
    if len(DicionarioGravacoes) == 0:
        print("\nNenhuma Gravação Foi Registrada Até O Momento")
        return
    print("\n Insira a Data de início:\n")
    Data1= input("Digite A 1º Data (**/**/****):")
    Data2= input("Digite A 2º Data (**/**/****):")
    DicionarioGravacoesCopia = DicionarioGravacoes.copy()
    for num in range(0, len(DicionarioGravacoesCopia)):
        ListaChavesVerificadas, DicionarioGravacoesCopia = VerificadorDatasRelatorio(
            Data1, Data2, DicionarioGravacoesCopia, ListaChavesVerificadas)
    cont1 = 1
    cont = 1
    print("============================================")
    for chave in ListaChavesVerificadas:
        for tupla, dados in DicionarioGravacoes.items():
            if tupla == chave:
                tupla = chave
                DadosGravação = dados
                TituloMusica = tupla[0]
                TituloCantor = tupla[1]
                DataGravação = tupla[2]
                print(f"{cont1}º Gravação \n")
                print("Dados da Gravação \n")
                print(f"Nome do Álbum - {DadosGravação[0]}")
                for ind in DadosGravação[1]:
                    print(f"{cont}º instrumento - {ind}")
                    cont = cont+1
                print(
                    f"Data Da Gravação: {DataGravação}")
                print('\nDados Da Musica \n')
                DadosMusica = DicionarioMusicas[TituloMusica]
                Tempo = DadosMusica[2]
                segundos, minutos = SegundosMinutos(Tempo)
                print(f"Titulo - {TituloMusica}")
                print(f"Data - {DadosMusica[0]}")
                print(f"Estilo - {DadosMusica[1]}")
                if minutos == 0:
                    print(f"Tempo - {segundos} segundos")
                else:
                    print(f"Tempo - {minutos} minutos e {segundos} segundos")
                print(f"Compositor - {DadosMusica[3]} \n")

                print("\nDados Do Cantor \n")
                DadosCantor = DicionarioCantores[TituloCantor]
                print(f"Nome Artístico - {TituloCantor}")
                print(f"Nome Real - {DadosCantor[0]}")
                print(f"Data de Nascimento - {DadosCantor[1]}")
                print(f"E-mail - {DadosCantor[2]}")
                print(f"Telefone - {DadosCantor[3]}")
                print("============================================")
                cont += 1
                cont1 += 1
    return


def VerificadorDatasRelatorio(Data1, Data2, DicionarioGravacoes, ListaChavesVerificadas):
    Data1 = datetime.strptime(Data1, "%d/%m/%Y").date()
    Data2 = datetime.strptime(Data2, "%d/%m/%Y" ).date()
    for chave in DicionarioGravacoes.keys():
        DadosDaGravação = DicionarioGravacoes[chave]
        Data = chave[2]
        Data = datetime.strptime(Data, "%d/%m/%Y").date()
        if Data >= Data1:
            if Data <= Data2:
                ListaChavesVerificadas.append(chave)
                del DicionarioGravacoes[chave]
                return(ListaChavesVerificadas, DicionarioGravacoes)

    return(ListaChavesVerificadas, DicionarioGravacoes)


#Verificador de datas
def SegundosMinutos(Tempo):
    minutos = Tempo//60
    segundos = Tempo % 60
    return(segundos, minutos)

