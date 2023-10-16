from log_.pegar_data_hora import pegar_horario
import os

# file = 'W:\\Contabil\\Controle\\Equipe\\Grupos\\LabKom\\log_app_jmoc_folha_pagamento\\'
# 'W:\Contabil\Controle\Equipe\Grupos\LabKom\log_app_jmoc_folha_pagamento\log_app_jmoc_folha_pagamento.txt'
file = 'W:\\Publico\\LabKom\\log_app_jmoc_folha_pagamento.txt'

def registrar_logs_execucao(texto):

    with open(file, 'a', newline='') as log:
        log.write(
            f'HORÁRIO ==> {pegar_horario()} | TAREFA ==> {texto}\n')


def limpar_logs():
    try:
        os.remove(file)
    except:
        pass
