#Imports
from datetime import *
from MenuGravações import *

# FUNCAO DO SUBMENU DE CANTORES
def Submenu_de_Cantores(DicionarioCantores, DicionarioGravacoes):
    # REPETIÇÃO
    opcao = 0
    while (opcao > 0) or (opcao < 7):
        print("   --- Submenu de Cantores --- ")
        print("")
        print("1. Adicionar novo Cantor")
        print("2. Alterar Cantor já Existente")
        print("3. Excluir Cantor")
        print("4. Procurar Cantor")
        print("5. Mostrar Todos os Cantores")
        print("6. Voltar ao Menu")
        opcao = int(input("\nEscolha Uma Opção: "))
        while (opcao > 6) or (opcao < 1):
            opcao = int(input("\nNumero Invalido \nEscolha Uma Opção: "))

        # ADICIONAR NOVO CANTOR
        if opcao == 1:
            print("=================================")
            print("\n --- Adicionar novo Cantor ---")
            Adicionar_Cantor(DicionarioCantores)
            print("\n --- Encerrando Adicionar novo Cantor ---")
            print(" --- Voltando ao Submenu de Cantores --- \n")
            print("==========================================")

        # ALTERAR CANTOR JA EXISTENTE
        if opcao == 2:
            print("=================================")
            print("\n --- Alterar Cantor já Existente ---")
            Alterar_Cantor_ja_Existente(
                DicionarioCantores, DicionarioGravacoes)
            print("\n --- Encerrando Alterar Cantor já Existente ---")
            print(" --- Voltando ao Submenu de Cantores --- \n")
            print("==========================================")

        # EXCLUIR CANTOR
        if opcao == 3:
            print("=================================")
            print("\n --- Excluir Cantor ---")
            Excluir_Cantor(
                DicionarioCantores, DicionarioGravacoes)
            print("\n --- Encerrando Excluir Cantor ---")
            print(" --- Voltando ao Submenu de Cantores --- \n")
            print("==========================================")

        # PROCURAR CANTOR
        if opcao == 4:
            print("=================================")
            print("\n --- Procurar Cantor ---")
            Procurar_Cantor(DicionarioCantores)
            print("\n --- Encerrando Procurar Cantor ---")
            print(" --- Voltando ao Submenu de Cantores --- \n")
            print("==========================================")

        # MOSTRAR TODOS OS CANTORES
        if opcao == 5:
            print("=================================")
            print("\n --- Mostrar Todos os Cantores ---")
            Mostrar_Todos_os_Cantores(DicionarioCantores)
            print("\n --- Encerrando Mostrar Todos os Cantores ---")
            print(" --- Voltando ao Submenu de Cantores --- \n")
            print("==========================================")

        # VOLTAR AO MENU
        if opcao == 6:
            print("\n --- Voltando ao Menu... --- \n")
            Salvar_Dados_Cantor(DicionarioCantores)
            print("==========================================")
            return

# FUNCAO ADICIONAR CANTOR


def Adicionar_Cantor(DicionarioCantores):
    DadosCantor = []
    NomeArtistico = input("\nDigite o Nome Artistico do Cantor:")
    for chave in DicionarioCantores.keys():
        if NomeArtistico.strip().lower().replace(" ", "") == chave.strip().lower().replace(" ", ""):
            print("\nNome Artistico Do Cantor Já Está Cadastrado")
            return
    DadosCantor.append(input("Digite O Nome Real Do Cantor:"))
    DadosCantor.append(input("Digite A Data De Nascimento Do Cantor:"))
    DadosCantor.append(input("Digite O Email Do Cantor:"))
    DadosCantor.append(input("Digite o Telefone Do Cantor:"))
    DicionarioCantores[NomeArtistico] = DadosCantor
    print("\nCantor Adicionado Com Sucesso")
    return

# FUNCAO ALTERAR CANTOR JA EXISTENTE


def Alterar_Cantor_ja_Existente(DicionarioCantores, DicionarioGravacoes):
    cont = 0
    if len(DicionarioCantores) == 0:
        print("\nNenhum Cantor Registrado Até o Momento")
        return
    update = input(
        "\nDigite o Nome Artistico do Cantor no qual você deseja alterar:")
    if update not in DicionarioCantores.keys():
        print("\nCantor Não Encontrado")
        return
    else:
        print("\n --- Digite Os Novos Dados Do Cantor --- \n")
        DadosCantor = []
    DadosCantor.append(input("Digite O Nome Real Do Cantor:"))
    DadosCantor.append(input("Digite A Data De Nascimento Do Cantor:"))
    DadosCantor.append(input("Digite O Email Do Cantor:"))
    DadosCantor.append(input("Digite o Telefone Do Cantor:"))
    for tupla in DicionarioGravacoes.keys():
            if tupla[1] == update:
                cont += 1
    if cont == 1:
        confirmar = input(
                "O Cantor Que Você Deseja Alterar está registrado em uma gravação, deseja continuar? (S/N):").strip().upper().replace(" ", "")
        if confirmar == "N":
            return
        else:
            for tupla in DicionarioGravacoes.keys():
                if tupla[1] == update:
                    dados = DicionarioGravacoes[tupla]
                    tupla = tupla
            del DicionarioGravacoes[tupla]
            novatupla = (tupla[0], update, tupla[2])
            DicionarioGravacoes[novatupla] = dados
    elif cont > 1:
        confirmar = input(
                "O Cantor Que Você Deseja Alterar está registrado em mais de uma gravação, deseja continuar? (S/N):").strip().upper().replace(" ", "")
        if confirmar == "N":
            return
        else:
            cont1 = 0
            while cont1 < cont:
                for tupla in DicionarioGravacoes.keys():
                    if tupla[1] == update:
                        dados = DicionarioGravacoes[tupla]
                        tupla = tupla
                del DicionarioGravacoes[tupla]
                novatupla = (tupla[0], update, tupla[2])
                DicionarioGravacoes[novatupla] = dados
                cont1 += 1
    DicionarioCantores[update] = DadosCantor
    print("\nCantor Alterado Com Sucesso")
    Salvar_Dados_Gravação(DicionarioGravacoes)
    return

# FUNCAO EXCLUIR CANTOR


def Excluir_Cantor(DicionarioCantores, DicionarioGravacoes):
    cont = 0
    if len(DicionarioCantores) == 0:
        print("\nNenhum Cantor Registrado Até o Momento!")
        return
    excluir = input(
        "\nDigite o Nome Artistico do Cantor no qual você deseja excluir:")
    if excluir not in DicionarioCantores.keys():
        print("\nCantor Não Encontrado")
        return
    else:
        for tupla in DicionarioGravacoes.keys():
            if tupla[1] == excluir:
                cont += 1
    if cont == 1:
        confirmar = input(
                    "O Cantor Que Você Deseja Excluir está registrado em uma gravação, deseja continuar? (S/N):").strip().upper().replace(" ", "")
        if confirmar == "N":
            return
        else:
            for tupla in DicionarioGravacoes.keys():
                if tupla[1] == excluir:
                    tupladel = tupla       
            del DicionarioGravacoes[tupladel]
    if cont > 1:
        confirmar = input(
                    "O Cantor Que Você Deseja Excluir está registrado em mais de uma gravação, deseja continuar? (S/N):").strip().upper().replace(" ", "")
        if confirmar == "N":
            return
        else:
            cont1 = 0
            while cont1 < cont:
                for tupla in DicionarioGravacoes.keys():
                    if tupla[1] == excluir:
                        tupladel = tupla
                del DicionarioGravacoes[tupladel]
                cont1 += 1
    del DicionarioCantores[excluir]
    Salvar_Dados_Gravação(DicionarioGravacoes)
    print("\nCantor Excluído Com Sucesso")
    return

# FUNCAO PROCURAR CANTOR


def Procurar_Cantor(DicionarioCantores):
    if len(DicionarioCantores) == 0:
        print("\nNenhum Cantor Registrado Até o Momento")
        return
    search = input(
        "\nDigite o Nome Artistico do Cantor no qual você deseja Procurar:")
    if search not in DicionarioCantores.keys():
        print("\nCantor Não Encontrado")
        return
    else:
        DadosCantor = DicionarioCantores[search]
        print("\nCantor Encontrado \n")
        print(f"Nome Artistico - {search}")
        print(f"Nome Real - {DadosCantor[0]}")
        print(f"DataNascimento - {DadosCantor[1]}")
        print(f"Email - {DadosCantor[2]}")
        print(f"Telefone - {DadosCantor[3]}")
        return

# FUNCAO MOSTRAR TODOS OS CANTORES


def Mostrar_Todos_os_Cantores(DicionarioCantores):
    cont = 1
    if len(DicionarioCantores) == 0:
        print("\nNenhum Cantor Registrado Até o Momento")
        return
    else:
        for key in DicionarioCantores.keys():
            DadosCantor = DicionarioCantores[key]
            print(f"\n{cont}º Cantor \n")
            print(f"Nome Artistico - {key}")
            print(f"Nome Real - {DadosCantor[0]}")
            print(f"DataNascimento - {DadosCantor[1]}")
            print(f"Email - {DadosCantor[2]}")
            print(f"Telefone - {DadosCantor[3]}")
            cont += 1
    return

def Salvar_Dados_Cantor(DicionarioCantores):
    cantor = open("cantores.txt", "w")
    for k, v in DicionarioCantores.items():
        NomeArtistico = k
        DadosCantor = v
        NomeReal = DadosCantor[0]
        DataNascimento = DadosCantor[1]
        Email = DadosCantor[2]
        Telefone = DadosCantor[3]
        linha = (f"{NomeArtistico}|{NomeReal}|{DataNascimento}|{Email}|{Telefone}\n")
        cantor.write(linha)
    cantor.close()
