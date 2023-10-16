from models.process_ import *
import os

if __name__ == '__main__':

    process = Process(
        cod_cliente='993',
        cnpj='35.382.136/0001-98',
        razao_social='ICOM COMÉRCIO DE MATERIAS DE CONSTRUÇÃO LTDA',
        grupo='---',
        contador='WJ',
        competencia='09/2023',
        check='',
        status='',
        obs=''
    )

    process.create_paths()

    process.add_steps(name='Questor Folha', numero='step_1', step=Step1)
    process.add_steps(name='SEFIP RE', numero='step_2', step=Step2)
    process.add_steps(name='Bater Valores', numero='step_3', step=Step3)
    process.add_steps(name='Conectividade', numero='step_4', step=Step4)
    process.add_steps(name='SEFIP XML', numero='step_5', step=Step5)
    process.add_steps(name='ECAC', numero='step_6', step=Step6)
    process.add_steps(name='PASTA', numero='step_7', step=Step7)
    process.add_steps(name='NIBO', numero='step_8', step=Step8)

    # try:

    #     process.dict_steps.get('step_2').import_sefip_re()
    #     process.dict_steps.get('step_2').atualizar_fap()
    #     process.dict_steps.get('step_2').gerar_arquivo_SFP()
    #     process.dict_steps.get('step_2').gerar_4_relatorios()

    # except Exception as e:
    #     sleep(5)
    #     erro = f'erro no modulo do sefip - 02 - {e}'
    #     pyautogui.hotkey('alt', 'f4')
    #     registrar_logs_execucao(erro)
    #     send_email_adm_anexo(erro)
    #     raise Exception(erro)

    process.dict_steps.get(
        'step_3').comparar_relatorios_sefip_questor_valor_FGTS()

    process.dict_steps.get('step_1').copy_files('step_1', 'step_2', 'SEFIP.RE')
    process.dict_steps.get('step_1').copy_files('step_1', 'step_7', 'SEFIP.RE')
