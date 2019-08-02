def cabecalho():
    # def cabecalho printa no início do código as informações do aluno, disciplina, data e hora.
    from datetime import datetime
    hoje = datetime.now()
    datahora = hoje.strftime("%d/%m/%y %H:%M")
    print('*'*35)
    print('*ALUNO: Nome                      *')
    print('*DISCIPLINA: ADS                  *')
    print(f'*DATA e HORA: {datahora}      *')
    print('*'*35)


