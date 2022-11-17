#Import
from datetime import *
from MenuGravações import *

# FUNCAO DO SUBMENU DE MUSICAS
def Submenu_de_Musicas(DicionarioMusicas, DicionarioGravacoes):
    # REPETIÇÃO
    opcao = 0
    while (opcao > 0) or (opcao < 7):
        print("   --- Submenu de Músicas --- ")
        print("")
        print("1. Adicionar nova Música")
        print("2. Alterar Música já Existente")
        print("3. Excluir Música")
        print("4. Procurar Música")
        print("5. Mostrar Todas as Músicas")
        print("6. Voltar ao Menu")
        opcao = int(input("\n--- Escolha Uma Opção: "))
        while (opcao > 6) or (opcao < 1):
            opcao = int(input("\nNumero Invalido \nEscolha Uma Opção: "))

        # ADICIONAR NOVA MUSICA

        if opcao == 1:
            print("=================================")
            print("   --- Adicionar nova Música ---")
            Adicionar_Musica(DicionarioMusicas)
            print("\n --- Encerrando Adicionar nova Música ---")
            print(" --- Voltando ao Submenu de Musicas --- \n")
            print("==========================================")

        # ALTERAR MUSICA JÀ EXISTENTE
        if opcao == 2:
            print("=================================")
            print("   --- Alterar Música já Existente ---")
            Alterar_Musica_ja_Existente(
                DicionarioMusicas, DicionarioGravacoes)
            print("\n --- Encerrando Alterar Música já Existente ---")
            print(" --- Voltando ao Submenu de Musicas --- \n")
            print("==========================================")

        # EXCLUIR MUSICA
        if opcao == 3:
            print("=================================")
            print("   --- Excluir Música ---")
            Excluir_Musica(
                DicionarioMusicas, DicionarioGravacoes)
            print("\n --- Encerrando Excluir Música ---")
            print(" --- Voltando ao Submenu de Musicas --- \n")
            print("==========================================")

        # PROCURAR MUSICA
        if opcao == 4:
            print("=================================")
            print("   --- Procurar Música ---")
            Procurar_Musica(DicionarioMusicas)
            print("\n --- Encerrando Procurar Música ---")
            print(" --- Voltando ao Submenu de Musicas --- \n")
            print("==========================================")

        # MOSTRAR TODAS AS MUSICAS
        if opcao == 5:
            print("=================================")
            print("   --- Mostrar Todas as Músicas ---")
            Mostrar_Todas_as_Musicas(DicionarioMusicas)
            print("\n --- Encerrando Mostrar Todas as Músicas ---")
            print(" --- Voltando ao Submenu de Musicas --- \n")
            print("============================================")

        # VOLTAR AO MENU
        if opcao == 6:
            print("\n   --- Voltando ao Menu... ---")
            Salvar_Dados_Musica(DicionarioMusicas)
            print("==========================================")
            return

# FUNCAO ADICIONAR MUSICA


def Adicionar_Musica(DicionarioMusicas):
    DadosMusica = []
    Titulo = input("\nDigite o Titulo da Musica:")
    for chave in DicionarioMusicas.keys():
        if Titulo.strip().lower().replace(" ", "") == chave.strip().lower().replace(" ", ""):
            print("\nTitulo Da Musica Já Está Cadastrado")
            return
    DadosMusica.append(input("Digite a Data Em Que A Musica Foi Feita (**/**/****):"))
    DadosMusica.append(input("Digite o Estilo da Musica:"))
    DadosMusica.append(int(input("Digite a Duração da Musica(em segundos):")))
    DadosMusica.append(input("Digite o Compositor da Musica:"))
    DicionarioMusicas[Titulo] = DadosMusica
    print("\nMusica Adicionada Com Sucesso")
    return

# FUNCAO ALTERAR MUSICA JA EXISTENTE


def Alterar_Musica_ja_Existente(DicionarioMusicas, DicionarioGravacoes):
    cont = 0
    if len(DicionarioMusicas) == 0:
        print("\nNenhuma Musica Registrada Até o Momento")
        return
    update = input("\nDigite o Titulo da Musica na qual você deseja alterar:")
    if update not in DicionarioMusicas.keys():
        print("\nMusica Não Encontrada")
        return
    else:
        print("\n --- Digite Os Novos Dados Da Musica --- \n")
        DadosMusica = []
        DadosMusica.append(input("Digite a Data Em Que A Musica Foi Feita (**/**/****):"))
        DadosMusica.append(input("Digite o Estilo da Musica:"))
        DadosMusica.append(
            int(input("Digite a Duração da Musica(em segundos):")))
        DadosMusica.append(input("Digite o Compositor da Musica:"))
        for tupla in DicionarioGravacoes.keys():
            if tupla[0] == update:
                cont += 1
        if cont == 1:
            confirmar = input(
                    "A Musica Que Você Deseja Alterar está registrada em uma gravação, deseja continuar? (S/N):").strip().upper().replace(" ", "")
            if confirmar == "N":
                return
            else:
                for tupla in DicionarioGravacoes.keys():
                    if tupla[0] == update:
                        dados = DicionarioGravacoes[tupla]
                        tupla = tupla
                del DicionarioGravacoes[tupla]
                novatupla = (update, tupla[1], tupla[2])
                DicionarioGravacoes[novatupla] = dados
        elif cont > 1:
            confirmar = input(
                    "A Musica Que Você Deseja Alterar está registrada em mais de uma gravação, deseja continuar? (S/N):").strip().upper().replace(" ", "")
            if confirmar == "N":
                return
            else:
                cont1 = 0
                while cont1 < cont:
                    for tupla in DicionarioGravacoes.keys():
                        if tupla[0] == update:
                            dados = DicionarioGravacoes[tupla]
                            tupla = tupla
                    del DicionarioGravacoes[tupla]
                    novatupla = (update, tupla[1], tupla[2])
                    DicionarioGravacoes[novatupla] = dados
                    cont1 += 1
        DicionarioMusicas[update] = DadosMusica
        Salvar_Dados_Gravação(DicionarioGravacoes)
        print("\nMusica Alterada Com Sucesso")
        return

# EXCLUIR MUSICA


def Excluir_Musica(DicionarioMusicas, DicionarioGravacoes):
    cont = 0
    if len(DicionarioMusicas) == 0:
        print("\nNenhuma Musica Registrada Até o Momento!")
        return
    excluir = input("\nDigite o Titulo da Musica na qual você deseja excluir:")
    if excluir not in DicionarioMusicas.keys():
        print("\nMusica Não Encontrada")
        return
    else:
        for tupla in DicionarioGravacoes.keys():
            if tupla[0] == excluir:
                cont += 1
    if cont == 1:
        confirmar = input(
                    "A Musica Que Você Deseja Excluir está registrada em uma gravação, deseja continuar? (S/N):").strip().upper().replace(" ", "")
        if confirmar == "N":
            return
        else:
            for tupla in DicionarioGravacoes.keys():
                if tupla[0] == excluir:
                    tupladel = tupla       
            del DicionarioGravacoes[tupladel]
    if cont > 1:
        confirmar = input(
                    "A Musica Que Você Deseja Excluir está registrada em mais de uma gravação, deseja continuar? (S/N):").strip().upper().replace(" ", "")
        if confirmar == "N":
            return
        else:
            cont1 = 0
            while cont1 < cont:
                for tupla in DicionarioGravacoes.keys():
                    if tupla[0] == excluir:
                        tupladel = tupla
                del DicionarioGravacoes[tupladel]
                cont1 += 1
    del DicionarioMusicas[excluir]
    print("\nMusica Excluída Com Sucesso")
    Salvar_Dados_Gravação(DicionarioGravacoes)
    return

# PROCURAR MUSICA


def Procurar_Musica(DicionarioMusicas):
    if len(DicionarioMusicas) == 0:
        print("\nNenhuma Musica Registrada Até o Momento")
        return
    search = input("\nDigite o Titulo da Musica na qual você deseja Procurar:")
    if search not in DicionarioMusicas:
        print("\nMusica Não Encontrada")
        return
    else:
        DadosMusica = DicionarioMusicas[search]
        Tempo = DadosMusica[2]
        segundos, minutos = SegundosMinutos(Tempo)
        print("\nMusica Encontrada \n")
        print(f"Titulo - {search}")
        print(f"Data - {DadosMusica[0]}")
        print(f"Estilo - {DadosMusica[1]}")
        if minutos == 0:
            print(f"Tempo - {segundos} segundos")
        else:
            print(f"Tempo - {minutos} minutos e {segundos} segundos")
        print(f"Compositor - {DadosMusica[3]}")
        return

# MOSTRAR TODAS AS MUSICAS


def Mostrar_Todas_as_Musicas(DicionarioMusicas):
    cont = 1
    if len(DicionarioMusicas) == 0:
        print("\nNenhuma Musica Registrada Até o Momento")
        return
    for key in DicionarioMusicas.keys():
        DadosMusica = DicionarioMusicas[key]
        Tempo = DadosMusica[2]
        segundos, minutos = SegundosMinutos(Tempo)
        print(f"\nMusica {cont} \n")
        print(f"Titulo - {key}")
        print(f"Data - {DadosMusica[0]}")
        print(f"Estilo - {DadosMusica[1]}")
        if minutos == 0:
            print(f"Tempo - {segundos} segundos")
        else:
            print(f"Tempo - {minutos} minutos e {segundos} segundos")
        print(f"Compositor - {DadosMusica[3]}")
        print("============================================")
        cont += 1
    return

#CALCULADORA DE MINUTOS E SEGUNDOS
def SegundosMinutos(Tempo):
    minutos = Tempo//60
    segundos = Tempo % 60
    return(segundos, minutos)

#Salvando Dados
def Salvar_Dados_Musica(DicionarioMusicas):
    musica = open("musicas.txt", "w")
    for k, v in DicionarioMusicas.items():
        Titulo = k
        DadosMusica = v
        DataMusica = DadosMusica[0]
        Estilo = DadosMusica[1]
        Duração = DadosMusica[2]
        Compositor = DadosMusica[3]
        linha = (f"{Titulo}|{DataMusica}|{Estilo}|{Duração}|{Compositor}\n")
        musica.write(linha)
    musica.close()
