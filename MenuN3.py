def menu():
    from time import sleep
    print(f'\033[32m{"MENU":-^26}')
    print('''[1]Cadastrar Nome/Telefone
[2]Listar Cadastro
[3]Apagar Cadastro
[4]Consultar Menu
[0]Sair''')
    print('-' * 26)
    # No começo do arquivo texto vai ter uma formação para indicar o cadastro, ela foi feita com o modo 'w' para escrever dentro.
    # Abro o arquivo texto antes de executar o menu, assim se o usuário digitar 2 antes de cadastrar alguma coisa o programa mostra o cadastro vazio.
    print('\033[m')
    arquivo_menu = open('cadastro_n3.txt', 'w')
    arquivo_menu.write(f'{"CADASTRO":-^64}\n')
    arquivo_menu.close()

    while True:
        # Começo o código fazendo um tratamento de exceção dentro da variável opcao.
        opcao = ' '
        try:
            opcao = int(input('Digite a opção desejada: '))
            print()
        except ValueError:
            print('\033[31mAVISO: Para selecionar uma opção é necessário digitar um número, conforme menu!\033[m')
        if opcao == 1:
            print('\033[32m[1]Cadastrar Nome/Telefone\033[m')
            sleep(0.4)
            # A primeira opcao vai fazer o cadastro com as variáveis nome e telefone, que serão guardadas dentro de um arquivo texto.
            # Uso um modo 'a', pois quero adicionar essas informações o quanto precisar e não apagar o que já está dentro.
            try:
                arquivo_cadastro = open('cadastro_n3.txt', 'a')
                print('\033[32mDigite o nome completo.\033[m')
                nome = str(input('Digite o nome: ')).lower()
                sleep(0.2)
                print('\033[32mMODELO: (área)= xx\033[m')
                area = int(input('Digite o código de área: '))
                print('\033[32mMODELO: (telefone)= xxxxxxxxx(9 dígitos)\033[m')
                telefone = int(input('Digite o telefone: '))
                arquivo_cadastro.write(f'NOME: {nome:<30}      TELEFONE:{area}-{telefone:<40}\n')
                arquivo_cadastro.close()
            except ValueError:
                print('\033[31mAVISO: Essa opção apenas aceita números, tente novamente!\033[m')
        if opcao == 2:
            print('\033[32m[2]Listar Cadastro\033[m')
            sleep(0.4)
            # Na segunda opcao mostra as informções que já foram armazenadas, se já foi armazenado algo.
            # Uso um modo 'r', pois apenas vou ler o que já está no arquivo texto.
            arquivo_cadastro = open('cadastro_n3.txt', 'r')
            # Uso um rstrip() para tirar as linhas em branco no print.
            for linha in arquivo_cadastro:
                linha = linha.rstrip()
                print(linha)
            print()
            print('-' * 64)
            arquivo_cadastro.close()
        if opcao == 3:
            print('\033[32m[3]Apagar Cadastro\033[m')
            sleep(0.4)
            # A terceira opcao deleta o cadastro que for colocado na variável apagar.
            print('\033[32mAVISO: Certifique-se de que o nome está digitado conforme a listagem, caso contrário, não será deletado!\033[m')
            apagar = input('Digite o nome completo que você quer deletar: ').lower()
            # Abro esse arquivo com with, assim não preciso fechar, e uso o r+ para poder ler e editar o texto.
            with open("cadastro_n3.txt", "r+") as arquivo:
                novo_arquivo = arquivo.readlines()
                # seek(0) para começar a ler no início do arquivo.
                arquivo.seek(0)
                # O pragrama conferi linha a linha e se a variável apagar não estiver na linha ele copia ela, e se ela estiver ocorre um truncate e a o cadastro é apagado.
                for linha in novo_arquivo:
                    if apagar not in linha:
                        arquivo.write(linha)
                arquivo.truncate()
        if opcao == 4:
            print('\033[32m[4]Consultar Menu\033[m')
            sleep(0.4)
            print(f'\033[32m{"MENU":-^26}')
            print('''[1]Cadastrar Nome/Telefone
[2]Listar Cadastro
[3]Apagar Cadastro
[4]Consultar Menu 
[0]Sair''')
            print('-' * 26)
            print('\033[m')
        if opcao == 0:
            print('\033[32m[0]Sair\033[m')
            # Na opcao 0 o programa e finaliza, salvando o conteúdo no arquivo cadastro_n3.
            break
    print('\033[32mEncerrando cadastramento...\033[m')
    sleep(1)
    arquivo_menu = open('cadastro_n3.txt', 'a')
    arquivo_menu.write('-' * 64)
    arquivo_menu.close()


