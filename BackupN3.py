def backup():
    # O def backup faz uma cópia do cadastro_n3 para o backup_cadastro_n3.
    # Uso um modo 'r' para ler o que tem no arquivo e em seguido um 'w' para escreve as linhas do arquivo original dentro do novo.
    original = open('cadastro_n3.txt', 'r')
    novo = open('backup_cadastro_n3', 'w')
    for linha in original:
        novo.write(linha)
    original.close()
    novo.close()

