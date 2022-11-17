#Import
from datetime import *

#Funções do Menu Gravações
def Submenu_de_Gravacoes(DicionarioMusicas, DicionarioCantores, DicionarioGravacoes):
    # REPETIÇÃO
    opcao = 0
    while (opcao > 0) or (opcao < 7):
        print("   --- Submenu de Gravações --- ")
        print("")
        print("1. Adicionar nova Gravação")
        print("2. Alterar Gravação já Existente")
        print("3. Excluir Gravação")
        print("4. Procurar Gravação")
        print("5. Mostrar Todos as Gravações")
        print("6. Voltar ao Menu")
        opcao = int(input("\nEscolha Uma Opção: "))
        while (opcao > 6) or (opcao < 1):
            opcao = int(input("\nNumero Invalido \nEscolha Uma Opção: "))

        # ADICIONAR NOVA GRAVACAO
        if opcao == 1:
            print("===============================")
            print("\n --- Adicionar nova Gravação ---")
            Adicionar_Gravacao(
                DicionarioMusicas, DicionarioCantores, DicionarioGravacoes)
            print("\n --- Encerrando Adicionar nova Gravação ---")
            print(" --- Voltando ao Submenu de Gravações --- \n")
            print("==========================================")

        # ALTERAR GRAVACAO JA EXISTENTE
        if opcao == 2:
            print("===============================")
            print("\n --- Alterar Gravação já Existente ---")
            Alterar_Gravacao_ja_Existente(
                DicionarioGravacoes)
            print("\n --- Encerrando Alterar Gravação já Existente ---")
            print(" --- Voltando ao Submenu de Gravações --- \n")
            print("==========================================")

        # EXCLUIR GRAVACAO
        if opcao == 3:
            print("===============================")
            print("\n --- Excluir Gravação ---")
            Excluir_Gravacao(DicionarioGravacoes)
            print("\n --- Encerrando Excluir Gravação ---")
            print(" --- Voltando ao Submenu de Gravações --- \n")
            print("==========================================")

        # PROCURAR GRAVACAO
        if opcao == 4:
            print("===============================")
            print("\n --- Procurar Gravação ---")
            Procurar_Gravacao(DicionarioMusicas,
                              DicionarioCantores, DicionarioGravacoes)
            print("\n --- Encerrando Procurar Gravação ---")
            print(" --- Voltando ao Submenu de Gravações --- \n")
            print("==========================================")

        # MOSTRAR TODAS AS GRAVACOES
        if opcao == 5:
            print("===============================")
            print("\n --- Mostrar Todas as Gravações ---")
            Mostrar_Todas_as_Gravacoes(
                DicionarioMusicas, DicionarioCantores, DicionarioGravacoes)
            print("\n --- Encerrando Mostrar Todos as Gravações ---")
            print(" --- Voltando ao Submenu de Gravações --- \n")
            print("==========================================")

        # VOLTAR AO MENU
        if opcao == 6:
            print("\n --- Voltando ao Menu... --- \n")
            Salvar_Dados_Gravação(DicionarioGravacoes)
            print("==========================================")
            return

# FUNCAO ADICIONAR GRAVACAO


def Adicionar_Gravacao(DicionarioMusicas, DicionarioCantores, DicionarioGravacoes):
    DadosGravação = []
    Instrumentos = []
    Datas = []
    TituloMusica = input("Digite a Musica que deseja acrescentar a Gravação:")
    if TituloMusica not in DicionarioMusicas.keys():
        print("\nMusica Não Encontrada")
        return
    TituloCantor = input(
        "Digite o Cantor que cantará a Musica nessa Gravação:")
    if TituloCantor not in DicionarioCantores.keys():
        print("\nCantor Não Encontrado")
        return
    Data = input("Digite a Data Em Que A Gravação Foi Feita (**/**/****):")
    tupla = (TituloMusica, TituloCantor, Data)
    for tuplas in DicionarioGravacoes.keys():
        if tuplas[0] == tupla[0]:
            if tuplas[1] == tupla[1]:
                if tuplas[2] == tupla[2]:
                    print(
                        "\nA Data Da Gravação (Com A Mesma Musica Do Mesmo Cantor) Já Está Cadastrada")
                    return
    Album = input("Digite o nome do álbum da gravação:")
    DadosGravação.append(Album)
    instrumento = input(
        "Digite os instrumentos usados; digite 'fim' para parar:").lower()
    while instrumento != "fim":
        Instrumentos.append(instrumento)
        instrumento = input(
            "Digite os instrumentos usados; digite 'fim' para cancelar:").lower()
    DadosGravação.append(Instrumentos)

    print("\nGravação Adicionada Com Sucesso")
    DicionarioGravacoes[tupla] = DadosGravação
    return


# FUNCAO ALTERAR GRAVACAO JA EXISTENTE
def Alterar_Gravacao_ja_Existente(DicionarioGravacoes):
    achou = False
    if len(DicionarioGravacoes) == 0:
        print("\nNenhuma Gravação Foi Registrada Até O Momento")
        return
    musica = input("\nDigite a musica da gravação a ser atualizada:")
    while achou == False:
        for chave, dados in DicionarioGravacoes.items():
            if musica == chave[0]:
                cantor = input(
                    "\nDigite o cantor da Gravação a ser atualizada:")
                if cantor == chave[1]:
                    Data = input("Digite a Data Da Gravação a ser atualizada (**/**/****):")
                    if Data == chave[2]:
                        achou = True
                        tupla = chave
        if achou == False:
            print("\nGravação Não Encontrada")
            return
    print("\n --- Digite Os Novos Dados Da Gravação --- \n")
    Instrumentos = []
    DadosGravação = []
    Datas = []
    Album = input("Digite o nome do álbum da gravação:")
    DadosGravação.append(Album)
    instrumento = input(
        "Digite os instrumentos usados; digite 'fim' para parar:").lower()
    while instrumento != "fim":
        Instrumentos.append(instrumento)
        instrumento = input(
            "Digite os instrumentos usados; digite 'fim' para cancelar:").lower()
    DadosGravação.append(Instrumentos)
    print("\nGravação Alterada Com Sucesso")
    DicionarioGravacoes[tupla].update(DadosGravação)
    return

# FUNCAO EXCLUIR GRAVACAO


def Excluir_Gravacao(DicionarioGravacoes):
    achou = False
    if len(DicionarioGravacoes) == 0:
        print("\nNenhuma Gravação Foi Registrada Até O Momento")
        return
    musica = input("\nDigite a musica da gravação a ser excluída:")
    while achou == False:
        for chave, dados in DicionarioGravacoes.items():
            if musica == chave[0]:
                cantor = input("\nDigite o cantor da Gravação a ser excluída:")
                if cantor == chave[1]:
                    Data = input("Digite a Data Da Gravação a ser excluída (**/**/****):")
                    if Data == chave[2]:
                        achou = True
                        tupla = chave
        if achou == False:
            print("\nGravação Não Encontrada")
            return
    del DicionarioGravacoes[tupla]
    print("\nGravação Excluída Com Sucesso")
    return

# FUNCAO PROCURAR GRAVACAO


def Procurar_Gravacao(DicionarioMusicas, DicionarioCantores, DicionarioGravacoes):
    achou = False
    if len(DicionarioGravacoes) == 0:
        print("\nNenhuma Gravação Foi Registrada Até O Momento")
        return
    musica = input("\nDigite a musica da gravação a ser Mostrada:")
    while achou == False:
        for chave, dados in DicionarioGravacoes.items():
            if musica == chave[0]:
                cantor = input("\nDigite o cantor da Gravação a ser Mostrada:")
                if cantor == chave[1]:
                    Data = input("Digite a Data Da Gravação a ser Mostrada (**/**/****):")
                    if Data == chave[2]:
                        achou = True
                        tupla = chave
        if achou == False:
            print("\n --- Gravação Não Encontrada ---")
            return

    TituloMusica = tupla[0]
    TituloCantor = tupla[1]
    DataGravação = tupla[2]
    DadosGravação = DicionarioGravacoes[tupla]
    cont = 1
    print(f"\nGravação Encontrada \n")
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
    return

# FUNCAO MOSTRAR TODAS AS GRAVACOES


def Mostrar_Todas_as_Gravacoes(DicionarioMusicas, DicionarioCantores, DicionarioGravacoes):
    cont1 = 1
    cont = 1
    if len(DicionarioGravacoes) == 0:
        print("\nNenhuma Gravação Foi Registrada Até O Momento")
        return
    for chave, dados in DicionarioGravacoes.items():
        tupla = chave
        DadosGravação = dados
        TituloMusica = tupla[0]
        TituloCantor = tupla[1]
        DataGravação = tupla[2]
        print(f"\n{cont1}º Gravação \n")
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
        print("\n ----------------------")
        cont += 1
        cont1 += 1
    return

#Verificador de datas
def SegundosMinutos(Tempo):
    minutos = Tempo//60
    segundos = Tempo % 60
    return(segundos, minutos)

def Salvar_Dados_Gravação(DicionarioGravacoes):
    gravacao = open("gravacoes.txt", "w")
    for k, v in DicionarioGravacoes.items():
        tupla = k
        Titulo = tupla[0]
        NomeArtistico = tupla[1]
        Data = tupla[2]
        DadosGravação = v
        Album = DadosGravação[0]
        Instrumentos = DadosGravação[1]
        nova = ""
        for instrumento in Instrumentos:
            nova += (f" {instrumento}")
        linha = (f"{Titulo}|{NomeArtistico}|{Data}|{Album}|{nova}\n")
        gravacao.write(linha)
    gravacao.close()

