import pyautogui
from time import sleep

from config_email.criacao_email import send_email_adm_anexo

from image_certificados.identificar_imagem_certificado import identificar_imagem_referente_certificado
from log_.gravar_log import registrar_logs_execucao


def empresa_nao_cadastrada_modulo_dp():

    # registrar_logs_execucao('Atualizar.....')

    coordenadas_msg = pyautogui.locateOnScreen(
        image='imagens/empresa_nao_configurada_dp.png',
        grayscale=True,
        confidence=0.9
    )

    if coordenadas_msg:
        registrar_logs_execucao('empresa nao cadastrada no modulo dp...')
        return True
    return False


def clicar_icone_vizualizar_declaracao_enviada():

    tempo = 1

    while (True):

        registrar_logs_execucao('procurando icone de "declaração enviada" ')

        coordenadas_olho_vizualizar_dec = pyautogui.locateOnScreen(
            image='image_ecac/vizualizar_declaracao.png',
            grayscale=True,
            confidence=0.9
        )

        if coordenadas_olho_vizualizar_dec:

            pyautogui.click(coordenadas_olho_vizualizar_dec, duration=2)
            registrar_logs_execucao(
                'icone vizualizar declaração enviada -> encontrado')
            return True

        sleep(1)
        tempo += 1
        if tempo == 60:
            send_email_adm_anexo(
                'AÇÃO DEMORANDO ALÉM DO NECESSÁRIO PARA SER EXECUTADA')
            raise Exception(
                'AÇÃO DEMORANDO ALÉM DO NECESSÁRIO PARA SER EXECUTADA')


def icone_vizualizar_declaracao_enviada():

    registrar_logs_execucao(
        'procurando icone -> visualizar declaração enviada!!!')

    coordenadas_olho_vizualizar_dec = pyautogui.locateOnScreen(
        image='image_ecac/vizualizar_declaracao.png',
        grayscale=True,
        confidence=0.9
    )

    if coordenadas_olho_vizualizar_dec:
        registrar_logs_execucao(
            'icone -> visualizar declaração enviada, encontrado!')
        return True
    return False


def botao_transmitir_declaracao():

    tempo = 1

    while (True):

        registrar_logs_execucao('procurando botao -> transmitir declaração')

        coordenadas_botao_transmitir_declaracao = pyautogui.locateOnScreen(
            image='image_ecac/botao_transmitir_declaracao.png',
            grayscale=True,
            confidence=0.9
        )

        if coordenadas_botao_transmitir_declaracao:
            registrar_logs_execucao('botao transmitir declaração encontrado..')
            pyautogui.click(
                coordenadas_botao_transmitir_declaracao, duration=2)
            return True

        sleep(1)
        tempo += 1
        if tempo == 60:
            send_email_adm_anexo(
                'AÇÃO DEMORANDO ALÉM DO NECESSÁRIO PARA SER EXECUTADA')
            raise Exception(
                'AÇÃO DEMORANDO ALÉM DO NECESSÁRIO PARA SER EXECUTADA')


def botao_executar_java():

    tempo = 1

    while (True):

        registrar_logs_execucao('procurando botao executar java....')

        coordenadas_botao_executar_java = pyautogui.locateOnScreen(
            image='image_ecac/botao_executar_java.png',
            grayscale=True,
            confidence=0.9
        )

        if coordenadas_botao_executar_java:
            registrar_logs_execucao('botao java encontrado...')
            pyautogui.click(coordenadas_botao_executar_java, duration=2)
            return True

        sleep(1)
        tempo += 1
        if tempo == 60:
            send_email_adm_anexo(
                'AÇÃO DEMORANDO ALÉM DO NECESSÁRIO PARA SER EXECUTADA')
            raise Exception(
                'AÇÃO DEMORANDO ALÉM DO NECESSÁRIO PARA SER EXECUTADA')


def botao_ok_final_transmissao():

    tempo = 1

    while (True):

        registrar_logs_execucao('procurando botao OK -> final transmissao...')

        coordenadas_ok_transmissao_final = pyautogui.locateOnScreen(
            image='image_ecac/botao_ok_transmissao_final.png',
            grayscale=True,
            confidence=0.9
        )

        if coordenadas_ok_transmissao_final:
            registrar_logs_execucao('botao final de transmissão encontrado')
            pyautogui.click(coordenadas_ok_transmissao_final, duration=2)
            return True

        sleep(1)
        tempo += 1
        if tempo == 60:
            send_email_adm_anexo(
                'AÇÃO DEMORANDO ALÉM DO NECESSÁRIO PARA SER EXECUTADA')
            raise Exception(
                'AÇÃO DEMORANDO ALÉM DO NECESSÁRIO PARA SER EXECUTADA')


def botao_ok_assinador_doc():

    tempo = 1

    while (True):

        registrar_logs_execucao('procurando ....botao OK assinador doc')

        coordenadas_assinador_doc = pyautogui.locateOnScreen(
            image='image_ecac/ok_assinador_doc.png',
            grayscale=True,
            confidence=0.9
        )
        coordenadas_assinador_doc_1 = pyautogui.locateOnScreen(
            image='image_ecac/ok_assinador_doc_1.png',
            grayscale=True,
            confidence=0.9
        )

        if coordenadas_assinador_doc or coordenadas_assinador_doc_1:
            registrar_logs_execucao('botao ok assinador doc encontrado...')
            if coordenadas_assinador_doc:
                pyautogui.click(coordenadas_assinador_doc, duration=2)
                registrar_logs_execucao('clicou no botao ok assinador doc_0')
            if coordenadas_assinador_doc_1:
                pyautogui.click(coordenadas_assinador_doc_1, duration=2)
                registrar_logs_execucao('clicou no botao ok assinador doc_1')
            return True

        sleep(1)
        tempo += 1
        if tempo == 60:
            send_email_adm_anexo(
                'AÇÃO DEMORANDO ALÉM DO NECESSÁRIO PARA SER EXECUTADA')
            raise Exception(
                'AÇÃO DEMORANDO ALÉM DO NECESSÁRIO PARA SER EXECUTADA')


def botao_confirmar_transmissao_declaracao():

    tempo = 1

    while (True):

        registrar_logs_execucao(
            'procurando botao confirmar transmissao da declaração')

        coordenadas_botao_confirmar_transmissao_dec = pyautogui.locateOnScreen(
            image='image_ecac/botao_confirmar_transmissao_declaracao.png',
            grayscale=True,
            confidence=0.9
        )

        coordenadas_botao_confirmar_transmissao_dec_sem_vinc = pyautogui.locateOnScreen(
            image='image_ecac/transmitir_sem_vinculacoes.png',
            grayscale=True,
            confidence=0.9
        )

        coordenadas_botao_confirmar_transmissao_normal = pyautogui.locateOnScreen(
            image='image_ecac/transmitir_normal.png',
            grayscale=True,
            confidence=0.9
        )

        if coordenadas_botao_confirmar_transmissao_dec_sem_vinc:
            registrar_logs_execucao(
                'botao confirmar transmissão da declaração encontrado...')
            pyautogui.click(
                coordenadas_botao_confirmar_transmissao_dec_sem_vinc, duration=2)
            return True

        if coordenadas_botao_confirmar_transmissao_dec:
            registrar_logs_execucao(
                'botao confirmar transmissão da declaração encontrado...')
            pyautogui.click(
                coordenadas_botao_confirmar_transmissao_dec, duration=2)
            return True

        if coordenadas_botao_confirmar_transmissao_normal:
            registrar_logs_execucao(
                'botao confirmar transmissão da declaração encontrado...')
            pyautogui.click(
                coordenadas_botao_confirmar_transmissao_normal, duration=2)
            return True

        sleep(1)
        tempo += 1
        if tempo == 60:
            send_email_adm_anexo(
                'AÇÃO DEMORANDO ALÉM DO NECESSÁRIO PARA SER EXECUTADA')
            raise Exception(
                'AÇÃO DEMORANDO ALÉM DO NECESSÁRIO PARA SER EXECUTADA')


def botao_transmitir_sem_vinculacoes():

    tempo = 1

    while (True):

        registrar_logs_execucao(
            'procurando botao transmitir sem vinculacoes')

        coordenadas_botao_confirmar_transmissao_dec = pyautogui.locateOnScreen(
            image='image_ecac/transmitir_sem_vinculacoes.png',
            grayscale=True,
            confidence=0.9
        )

        if coordenadas_botao_confirmar_transmissao_dec:
            registrar_logs_execucao(
                'botao botao transmitir sem vinculacoes encontrado...')
            pyautogui.click(
                coordenadas_botao_confirmar_transmissao_dec, duration=2)
            return True

        sleep(1)
        tempo += 1
        if tempo == 60:
            send_email_adm_anexo(
                'AÇÃO DEMORANDO ALÉM DO NECESSÁRIO PARA SER EXECUTADA')
            raise Exception(
                'AÇÃO DEMORANDO ALÉM DO NECESSÁRIO PARA SER EXECUTADA')


def botao_downloads():

    tempo = 1

    while (True):

        registrar_logs_execucao(
            'procurando botao de downloads')

        coordenadas_botao_confirmar_transmissao_dec = pyautogui.locateOnScreen(
            image='image_ecac/clica_aparecer_assinador_digital.PNG',
            grayscale=True,
            confidence=0.9
        )

        if coordenadas_botao_confirmar_transmissao_dec:
            registrar_logs_execucao(
                'botao botao de downloads encontrado...')
            pyautogui.click(
                coordenadas_botao_confirmar_transmissao_dec, duration=2)
            return True

        sleep(1)
        tempo += 1
        if tempo == 60:
            send_email_adm_anexo(
                'AÇÃO DEMORANDO ALÉM DO NECESSÁRIO PARA SER EXECUTADA')
            raise Exception(
                'AÇÃO DEMORANDO ALÉM DO NECESSÁRIO PARA SER EXECUTADA')


def botao_confirmar_assinatura_digital_download():

    tempo = 1

    while (True):

        registrar_logs_execucao(
            'procurando botao confirmar assinatura digital download')

        coordenadas_botao_confirmar_assinatura_digital = pyautogui.locateOnScreen(
            image='image_ecac/assinador_digital_downloads.png',
            grayscale=True,
            confidence=0.9
        )

        coordenadas_botao_confirmar_assinatura_digital_1 = pyautogui.locateOnScreen(
            image='image_ecac/assinador_digital_downloads_1.png',
            grayscale=True,
            confidence=0.9
        )

        if coordenadas_botao_confirmar_assinatura_digital or coordenadas_botao_confirmar_assinatura_digital_1:

            if coordenadas_botao_confirmar_assinatura_digital:
                registrar_logs_execucao(
                    'botao -> confirmar assinatura digitar download encontrado....')
                pyautogui.click(
                    coordenadas_botao_confirmar_assinatura_digital, duration=2)
                return True
            if coordenadas_botao_confirmar_assinatura_digital_1:
                registrar_logs_execucao(
                    'botao -> confirmar assinatura digitar download encontrado....')
                pyautogui.click(
                    coordenadas_botao_confirmar_assinatura_digital_1, duration=2)
                return True

        sleep(1)
        tempo += 1
        if tempo == 60:
            send_email_adm_anexo(
                'AÇÃO DEMORANDO ALÉM DO NECESSÁRIO PARA SER EXECUTADA')
            raise Exception(
                'AÇÃO DEMORANDO ALÉM DO NECESSÁRIO PARA SER EXECUTADA')


# def atualizar_versao_java():

#     coordenadas_versao_java = pyautogui.locateOnScreen(
#         image='image_ecac/atualizar_versao_java.png',
#         grayscale=True,
#         confidence=0.9
#     )

#     if coordenadas_versao_java:
#         pyautogui.click(
#             coordenadas_versao_java, duration=2)
#         return True
#     else:
#         return False


# def data_transmissao_em_branco():

#     coordenadas_data_transmissao_branco = pyautogui.locateOnScreen(
#         image='image_ecac/data_transmissao_branco.png',
#         grayscale=True,
#         confidence=0.9
#     )

#     if coordenadas_data_transmissao_branco:

#         return True
#     else:
#         return False


# def origem_esocial_reinf_CP():

#     coordenadas_esocial_reinf = pyautogui.locateOnScreen(
#         image='image_ecac/origem_esocial_reinf_cp.png',
#         grayscale=True,
#         confidence=0.9
#     )

#     if coordenadas_esocial_reinf:
#         return True
#     else:
#         return False


def origem_reinf_cp():

    registrar_logs_execucao('procurando origem reinf cp...')

    coordenadas_reinf_cp = pyautogui.locateOnScreen(
        image='image_ecac/origem_reinf_cp.png',
        grayscale=True,
        confidence=0.9
    )

    if coordenadas_reinf_cp:
        registrar_logs_execucao('origem reinf cp encontrado...')
        return True
    else:
        return False


def nao_encontrou_outorgante():

    registrar_logs_execucao('procurando outorgante!!')

    coordenadas_outorgante_n_encontrado = pyautogui.locateOnScreen(
        image='image_ecac/outorgante_nao_encontrado.png',
        grayscale=True,
        confidence=0.9
    )

    if coordenadas_outorgante_n_encontrado:
        registrar_logs_execucao('outorgante nao encontrado!!!')
        return True
    else:
        return False


def nenhuma_declaracao_encontrada():

    registrar_logs_execucao('verificando se existe alguma declaração..')

    coordenadas_nenhuma_dec_encontrada = pyautogui.locateOnScreen(
        image='image_ecac/nenhuma_declaracao_encontrada.png',
        grayscale=True,
        confidence=0.9
    )

    if coordenadas_nenhuma_dec_encontrada:
        registrar_logs_execucao('nenhuma declaração foi encontrada!!')
        return True
    else:
        return False


def origem_esocial():

    registrar_logs_execucao('procurando se o esocial está na Origem..')

    coordenadas_reinf_cp = pyautogui.locateOnScreen(
        image='image_ecac/origem_esocial.png',
        grayscale=True,
        confidence=0.9
    )

    if coordenadas_reinf_cp:
        registrar_logs_execucao('esocial encontrado na origem....')
        return True
    else:
        return False


# def saldo_pagar_zero():

#     coordenadas_saldo_pagar_zero = pyautogui.locateOnScreen(
#         image='image_ecac/saldo_pagar_zero.png',
#         grayscale=True,
#         confidence=0.9
#     )

#     if coordenadas_saldo_pagar_zero:
#         return True
#     else:
#         return False


def botao_transmitir_declaracao_is_visible():

    registrar_logs_execucao(
        'procurando se botão de transmitir declaração está habilitado....')

    coordenadas_botao_transmitir_dec = pyautogui.locateOnScreen(
        image='image_ecac/botao_transmitir_declaracao.png',
        grayscale=True,
        confidence=0.9
    )

    if coordenadas_botao_transmitir_dec:
        registrar_logs_execucao(
            'botao -> transmitir declaração habilitado, foi encontrado')
        return True
    else:
        return False


def botao_relatorios_recibo_declaracao():

    tempo = 1

    while (True):

        registrar_logs_execucao(
            'procurando botao relatorio de recibos de declarações...')

        coordenadas_botao_relatorios = pyautogui.locateOnScreen(
            image='image_ecac/botao_relatorios.png',
            grayscale=True,
            confidence=0.9
        )

        if coordenadas_botao_relatorios:
            registrar_logs_execucao(
                'botao de relatórios encontrados...será movido mouse até lá..')

            pyautogui.moveTo(coordenadas_botao_relatorios, duration=2)
            break

        sleep(1)
        tempo += 1
        if tempo == 60:
            send_email_adm_anexo(
                'AÇÃO DEMORANDO ALÉM DO NECESSÁRIO PARA SER EXECUTADA')
            raise Exception(
                'AÇÃO DEMORANDO ALÉM DO NECESSÁRIO PARA SER EXECUTADA')


def botao_sair_seguranca():

    tempo = 1

    while (True):

        registrar_logs_execucao(
            'procurando botao sair com seguranca...')

        coordenadas_botao_relatorios = pyautogui.locateOnScreen(
            image='image_ecac/sair_com_seguranca.png',
            grayscale=True,
            confidence=0.9
        )

        if coordenadas_botao_relatorios:
            registrar_logs_execucao(
                'botao sair com seguranca encontrado...será movido mouse até lá..')

            pyautogui.click(coordenadas_botao_relatorios, duration=2)
            break

        sleep(1)
        tempo += 1
        if tempo == 60:
            send_email_adm_anexo(
                'AÇÃO DEMORANDO ALÉM DO NECESSÁRIO PARA SER EXECUTADA')
            raise Exception(
                'AÇÃO DEMORANDO ALÉM DO NECESSÁRIO PARA SER EXECUTADA')


def botao_sair_seguranca_erro():

    registrar_logs_execucao(
        'procurando botao sair com seguranca...')

    coordenadas_botao_relatorios = pyautogui.locateOnScreen(
        image='image_ecac/sair_com_seguranca.png',
        grayscale=True,
        confidence=0.9
    )

    if coordenadas_botao_relatorios:
        registrar_logs_execucao(
            'botao sair com seguranca encontrado...será movido mouse até lá..')

        pyautogui.click(coordenadas_botao_relatorios, duration=2)


def botao_download_recibo():

    tempo = 1

    while (True):

        registrar_logs_execucao(
            'procurando botao download os recibos...')

        coordenadas_download_recibos = pyautogui.locateOnScreen(
            image='image_ecac/donwload_recibo.png',
            grayscale=True,
            confidence=0.9
        )

        if coordenadas_download_recibos:
            registrar_logs_execucao(
                'botao download dos recibos encontrado...será clicaco..')

            pyautogui.click(coordenadas_download_recibos, duration=2)
            break

        sleep(1)
        tempo += 1
        if tempo == 60:
            send_email_adm_anexo(
                'AÇÃO DEMORANDO ALÉM DO NECESSÁRIO PARA SER EXECUTADA')
            raise Exception(
                'AÇÃO DEMORANDO ALÉM DO NECESSÁRIO PARA SER EXECUTADA')


def botao_download_declaracao_completa():

    tempo = 1

    while (True):

        registrar_logs_execucao(
            'procurando botao download declaraçao completa...')

        coordenadas_download_recibos = pyautogui.locateOnScreen(
            image='image_ecac/download_dec_completa.png',
            grayscale=True,
            confidence=0.9
        )

        if coordenadas_download_recibos:
            registrar_logs_execucao(
                'botao download declaração completa encontrado...será clicaco..')

            pyautogui.click(coordenadas_download_recibos, duration=2)
            break

        sleep(1)
        tempo += 1
        if tempo == 60:
            send_email_adm_anexo(
                'AÇÃO DEMORANDO ALÉM DO NECESSÁRIO PARA SER EXECUTADA')
            raise Exception(
                'AÇÃO DEMORANDO ALÉM DO NECESSÁRIO PARA SER EXECUTADA')


def fechar_mostra_downloads():

    tempo = 1

    while (True):

        registrar_logs_execucao(
            'procurando botao mostra downloads...')

        coord_mostra_donwloads = pyautogui.locateOnScreen(
            image='image_ecac/fechar_barra_mostra_donwloads.png',
            grayscale=True,
            confidence=0.9
        )

        if coord_mostra_donwloads:
            registrar_logs_execucao(
                'botao mostra de donwloads sera clicado.....')

            pyautogui.click(coord_mostra_donwloads, duration=2)
            break

        sleep(1)
        tempo += 1
        if tempo == 60:
            send_email_adm_anexo(
                'AÇÃO DEMORANDO ALÉM DO NECESSÁRIO PARA SER EXECUTADA')
            raise Exception(
                'AÇÃO DEMORANDO ALÉM DO NECESSÁRIO PARA SER EXECUTADA')


def clicar_botao_voltar_tela_declaracoes():

    tempo = 1

    while (True):

        registrar_logs_execucao(
            'procurando botao voltar...')

        coord_mostra_donwloads = pyautogui.locateOnScreen(
            image='image_ecac/botao_voltar_tela_relacao_declaracoes.png',
            grayscale=True,
            confidence=0.9
        )

        if coord_mostra_donwloads:
            registrar_logs_execucao(
                'botao voltar será clicado.....')

            pyautogui.click(coord_mostra_donwloads, duration=2)
            break

        sleep(1)
        tempo += 1
        if tempo == 60:
            send_email_adm_anexo(
                'AÇÃO DEMORANDO ALÉM DO NECESSÁRIO PARA SER EXECUTADA')
            raise Exception(
                'AÇÃO DEMORANDO ALÉM DO NECESSÁRIO PARA SER EXECUTADA')


def aguarde_aparecer_guia_esocial():

    tempo = 1

    while (True):

        coordenadas_guia_ecac = pyautogui.locateOnScreen(
            'image/guia_esocial.png',  grayscale=True, confidence=0.9)

        if coordenadas_guia_ecac:
            registrar_logs_execucao('aba esocial encontrada na tela...')
            return True
        else:
            registrar_logs_execucao('PROCURANDO!!! aba esocial na tela...')

        sleep(1)
        tempo += 1
        if tempo == 60:
            send_email_adm_anexo(
                'AÇÃO DEMORANDO ALÉM DO NECESSÁRIO PARA SER EXECUTADA')
            raise Exception(
                'AÇÃO DEMORANDO ALÉM DO NECESSÁRIO PARA SER EXECUTADA')


def aguarde_aparecer_janela_periodicos_sem_mov_1299():

    tempo = 1

    while (True):

        coordenadas_janela_period_sem_mov_1299 = pyautogui.locateOnScreen(
            'image/janela_periodicos_sem_movimento_1299.png',  grayscale=True, confidence=0.9)

        if coordenadas_janela_period_sem_mov_1299:
            registrar_logs_execucao(
                'janela periódicos sem movimento 1299 encontrada...')
            return True
        else:
            registrar_logs_execucao(
                'PROCURANDO!!! janela periódicos sem movimento 1299...')

        sleep(1)
        tempo += 1
        if tempo == 60:
            send_email_adm_anexo(
                'AÇÃO DEMORANDO ALÉM DO NECESSÁRIO PARA SER EXECUTADA')
            raise Exception(
                'AÇÃO DEMORANDO ALÉM DO NECESSÁRIO PARA SER EXECUTADA')


def aguarde_aparecer_janela_esocial_1299():

    tempo = 1

    while (True):

        coordenadas_janela_period_sem_mov_1299 = pyautogui.locateOnScreen(
            'image/janela_esocial_1299.png',  grayscale=True, confidence=0.9)

        if coordenadas_janela_period_sem_mov_1299:
            registrar_logs_execucao('janela esocial 1299 encontrada...')
            return True
        else:
            registrar_logs_execucao(
                'PROCURANDO!!! janela esocial 1299 encontrada...')

        sleep(1)
        tempo += 1
        if tempo == 60:
            send_email_adm_anexo(
                'AÇÃO DEMORANDO ALÉM DO NECESSÁRIO PARA SER EXECUTADA')
            raise Exception(
                'AÇÃO DEMORANDO ALÉM DO NECESSÁRIO PARA SER EXECUTADA')


def clicar_guia_efd_reinf_desabilitada():

    tempo = 1

    while (True):

        coordenadas_efd_reinf = pyautogui.locateOnScreen(
            image='image/guia_efd-reinf_desabilitada.png',
            grayscale=True,
            confidence=0.9
        )

        if coordenadas_efd_reinf:
            registrar_logs_execucao('aba efd-reinf desabilitada encontrada...')
            pyautogui.click(coordenadas_efd_reinf)
            registrar_logs_execucao(
                'CLICOU!!! aba efd-reinf desabilitada encontrada...')
            return True
        else:
            registrar_logs_execucao(
                'PROCURANDO!!! aba efd-reinf desabilitada...')

        sleep(1)
        tempo += 1
        if tempo == 60:
            send_email_adm_anexo(
                'AÇÃO DEMORANDO ALÉM DO NECESSÁRIO PARA SER EXECUTADA')
            raise Exception(
                'AÇÃO DEMORANDO ALÉM DO NECESSÁRIO PARA SER EXECUTADA')


def clicar_botao_fechar_periodicos():

    tempo = 1

    while (True):

        coordenadas_button_fechar_periodicos = pyautogui.locateOnScreen(
            image='image/button_fechar_periodicos.png',
            grayscale=True,
            confidence=0.9
        )

        if coordenadas_button_fechar_periodicos:
            registrar_logs_execucao('botao fechar periodicos...')
            pyautogui.click(coordenadas_button_fechar_periodicos, duration=2)
            registrar_logs_execucao('CLICOU!!! botao fechar periodicos...')
            return True
        else:
            registrar_logs_execucao('PROCURANDO!!! botao fechar periodicos...')

        sleep(1)
        tempo += 1
        if tempo == 60:
            send_email_adm_anexo(
                'AÇÃO DEMORANDO ALÉM DO NECESSÁRIO PARA SER EXECUTADA')
            raise Exception(
                'AÇÃO DEMORANDO ALÉM DO NECESSÁRIO PARA SER EXECUTADA')


def mensagem_validacao_fechamento_reinf(codigo_cliente):

    tempo = 1

    i = 1
    while (True):

        registrar_logs_execucao('procurando msg validacao fechamento reinf..')

        coordenadas_validacao_periodico_sucesso = pyautogui.locateOnScreen(
            image='image/periodico_sucesso.png',
            grayscale=True,
            confidence=0.9
        )

        coordenadas_validacao_periodico_erro = pyautogui.locateOnScreen(
            image='image/erro.png',
            grayscale=True,
            confidence=0.9
        )

        if coordenadas_validacao_periodico_sucesso:
            registrar_logs_execucao(
                'msg validacao fechamento reinf encontrado com [sucesso]....')
            return True
        if coordenadas_validacao_periodico_erro:
            registrar_logs_execucao(
                'msg validacao fechamento reinf encontrado com [erro]....')
            gravar_imagem_erro_periodicos(codigo_cliente)
            return False
        if i == 60:
            gravar_imagem_erro_periodicos(codigo_cliente)
            return False

        i += 1

        sleep(1)
        tempo += 1
        if tempo == 90:
            send_email_adm_anexo(
                'AÇÃO DEMORANDO ALÉM DO NECESSÁRIO PARA SER EXECUTADA')
            raise Exception(
                'AÇÃO DEMORANDO ALÉM DO NECESSÁRIO PARA SER EXECUTADA')


def aguarde_aparecer_guia_efd_reinf():

    tempo = 1

    while (True):

        coordenadas_efd_reinf = pyautogui.locateOnScreen(
            image='image/guia_efd-reinf_habilitada.png',
            grayscale=True,
            confidence=0.9
        )

        if coordenadas_efd_reinf:
            registrar_logs_execucao('aba efd-reinf habilitada encontrada...')
            return True
        else:
            registrar_logs_execucao(
                'PROCURANDO!!! aba efd-reinf habilitada...')

        sleep(1)
        tempo += 1
        if tempo == 60:
            send_email_adm_anexo(
                'AÇÃO DEMORANDO ALÉM DO NECESSÁRIO PARA SER EXECUTADA')
            raise Exception(
                'AÇÃO DEMORANDO ALÉM DO NECESSÁRIO PARA SER EXECUTADA')


def aguarde_aparecer_tela_aviso_periódicos_1299():

    sleep(5)

    # tempo = 1

    while (True):

        # procurar botao sim
        botao_sim()

        coordenadas_efd_reinf = pyautogui.locateOnScreen(
            image='image/avisos_periodicos_1299.png',
            grayscale=True,
            confidence=0.9
        )

        if coordenadas_efd_reinf:
            registrar_logs_execucao(
                'tela avisos periódicos 1299 encontrada...')
            return True
        else:
            registrar_logs_execucao(
                'NÃO ENCONTRADO!!! tela de avisos periódicos 1299...')
            break


def aguarde_aparecer_janela_periodicos_reab_fech():

    tempo = 1

    while (True):

        # atualizar()

        coordenadas_janela_periodicos = pyautogui.locateOnScreen(
            image='image/janela_efd_reinf_fechamento_reabertura_periodicos.png',
            grayscale=True,
            confidence=0.9
        )

        if coordenadas_janela_periodicos:
            registrar_logs_execucao('janela periócios encontrada...')
            return True
        else:
            registrar_logs_execucao('PROCURANDO!!! janela periócios...')

        sleep(1)
        tempo += 1
        if tempo == 60:
            send_email_adm_anexo(
                'AÇÃO DEMORANDO ALÉM DO NECESSÁRIO PARA SER EXECUTADA')
            raise Exception(
                'AÇÃO DEMORANDO ALÉM DO NECESSÁRIO PARA SER EXECUTADA')


def gravar_imagem_erro_periodicos(codigo_cliente):

    tempo = 1

    while (True):

        imagem = pyautogui.screenshot(
            region=(331, 674, 1253, 142), imageFilename=f'anexos_conteudo_email/erro periodicos {codigo_cliente}.png')

        if imagem:
            registrar_logs_execucao(
                'Situação de erro periódicos encontrada com sucesso!')
            registrar_logs_execucao(imagem)
            return True
        else:
            registrar_logs_execucao(
                'PROCURANDO!! capturando mensagem de erro de periódicos')

        sleep(1)
        tempo += 1
        if tempo == 60:
            send_email_adm_anexo(
                'AÇÃO DEMORANDO ALÉM DO NECESSÁRIO PARA SER EXECUTADA')
            raise Exception(
                'AÇÃO DEMORANDO ALÉM DO NECESSÁRIO PARA SER EXECUTADA')


def gravar_imagem_padrao_tela_s_1299(codigo_cliente):

    tempo = 1

    while (True):

        # atualizar()
        coordenadas_janela_padrao_s_1299 = pyautogui.locateOnScreen(
            image='image/janela_esocial_1299.png',
            grayscale=True,
            confidence=0.9
        )

        if coordenadas_janela_padrao_s_1299:

            registrar_logs_execucao(
                'janela imagem padrao tela s-1299 encontrada!')

            pyautogui.screenshot(

                region=(0, 150, 1879, 682), imageFilename=f'anexos_conteudo_email/janela padrao tela s-1299 {codigo_cliente}.png')

            return True
        else:
            registrar_logs_execucao('PROCURANDO!! imagem padrao tela s-1299')

        sleep(1)
        tempo += 1
        if tempo == 60:
            send_email_adm_anexo(
                'AÇÃO DEMORANDO ALÉM DO NECESSÁRIO PARA SER EXECUTADA')
            raise Exception(
                'AÇÃO DEMORANDO ALÉM DO NECESSÁRIO PARA SER EXECUTADA')


def scrollar_ate_o_fim_guia_eventos():

    registrar_logs_execucao('clicando na barra de rolagem')
    pyautogui.click(207, 219, duration=1)
    registrar_logs_execucao('scrolando......')
    pyautogui.scroll(-10)
    sleep(0.5)
    pyautogui.scroll(-10)
    sleep(0.5)
    pyautogui.scroll(-10)
    sleep(0.5)
    pyautogui.scroll(-10)
    registrar_logs_execucao('scrolagem finalizada')


def scrollar_ate_o_inicio_guia_eventos():

    registrar_logs_execucao('clicando na barra de rolagem')
    pyautogui.click(207, 905, duration=1)
    registrar_logs_execucao('scrolando......')
    pyautogui.scroll(10)
    sleep(0.5)
    pyautogui.scroll(10)
    sleep(0.5)
    pyautogui.scroll(10)
    sleep(0.5)
    pyautogui.scroll(10)
    registrar_logs_execucao('scrolagem finalizada')


def botao_agilizar_envio_clicar():

    tempo = 1

    while (True):

        registrar_logs_execucao('procurando o botão agilizar envio....')

        coordenadas_button_agilizar_envio = pyautogui.locateOnScreen(
            image='image/agilizar_consulta.png',
            grayscale=True,
            confidence=0.9
        )

        if coordenadas_button_agilizar_envio:
            registrar_logs_execucao(
                'botao -> agilizar envio, encontrado, será clicado')
            pyautogui.click(coordenadas_button_agilizar_envio, duration=2)
            pyautogui.move(200, 0)
            return True

        sleep(1)
        tempo += 1
        if tempo == 60:
            send_email_adm_anexo(
                'AÇÃO DEMORANDO ALÉM DO NECESSÁRIO PARA SER EXECUTADA')
            raise Exception(
                'AÇÃO DEMORANDO ALÉM DO NECESSÁRIO PARA SER EXECUTADA')


def clicar_gov_br():

    tempo = 1

    while (True):

        registrar_logs_execucao('procurando o gov br')

        coordenadas_botao_gov = pyautogui.locateOnScreen(
            image='image_ecac/gov_br.png',
            grayscale=True,
            confidence=0.9
        )

        if coordenadas_botao_gov:
            registrar_logs_execucao('encontrado o gov br, será clicado')
            pyautogui.click(coordenadas_botao_gov, duration=2)
            return True

        sleep(1)
        tempo += 1
        if tempo == 60:
            send_email_adm_anexo(
                'AÇÃO DEMORANDO ALÉM DO NECESSÁRIO PARA SER EXECUTADA')
            raise Exception(
                'AÇÃO DEMORANDO ALÉM DO NECESSÁRIO PARA SER EXECUTADA')


def clicar_botao_acessar_certificao():

    tempo = 1

    while (True):

        registrar_logs_execucao('procurando o botao -> acessar certificado')

        coordenadas_botao_certificado = pyautogui.locateOnScreen(
            image='image_ecac/certificado_botao.png',
            grayscale=True,
            confidence=0.9
        )

        if coordenadas_botao_certificado:
            sleep(1)
            registrar_logs_execucao(
                'botao -> acessar certificado, encontrado! será clicado')
            pyautogui.click(coordenadas_botao_certificado, duration=2)
            return True

        sleep(1)
        tempo += 1
        if tempo == 60:
            send_email_adm_anexo(
                'AÇÃO DEMORANDO ALÉM DO NECESSÁRIO PARA SER EXECUTADA')
            raise Exception(
                'AÇÃO DEMORANDO ALÉM DO NECESSÁRIO PARA SER EXECUTADA')


def clicar_botao_declaracoes_demonstrativos():

    tempo = 1

    while (True):

        registrar_logs_execucao(
            'procurando botao-> declarações demonstrativos')

        coordenadas_botao_declaracoes_demonstrativos = pyautogui.locateOnScreen(
            image='image_ecac/botao_declaracoes_demonstrativos.png',
            grayscale=True,
            confidence=0.9
        )

        if coordenadas_botao_declaracoes_demonstrativos:
            registrar_logs_execucao(
                'botao-> declarações demonstrativos encontrado, será clicado')
            pyautogui.click(
                coordenadas_botao_declaracoes_demonstrativos, duration=2)
            return True

        sleep(1)
        tempo += 1
        if tempo == 60:
            send_email_adm_anexo(
                'AÇÃO DEMORANDO ALÉM DO NECESSÁRIO PARA SER EXECUTADA')
            raise Exception(
                'AÇÃO DEMORANDO ALÉM DO NECESSÁRIO PARA SER EXECUTADA')


def clicar_link_assinar_dctfweb():

    tempo = 1

    while (True):

        registrar_logs_execucao('procurando link -> assinar dctfweb')

        coordenadas_link_assinar_dctfweb = pyautogui.locateOnScreen(
            image='image_ecac/link_assinar_dctfweb.png',
            grayscale=True,
            confidence=0.9
        )

        if coordenadas_link_assinar_dctfweb:
            registrar_logs_execucao(
                'link assinar dctfweb encontrado, será clicado')
            pyautogui.click(
                coordenadas_link_assinar_dctfweb, duration=2)
            return True

        sleep(1)
        tempo += 1
        if tempo == 60:
            send_email_adm_anexo(
                'AÇÃO DEMORANDO ALÉM DO NECESSÁRIO PARA SER EXECUTADA')
            raise Exception(
                'AÇÃO DEMORANDO ALÉM DO NECESSÁRIO PARA SER EXECUTADA')


def click_i_am_human():

    tempo = 1

    while (True):

        registrar_logs_execucao('procurando imagem do anti robo...')

        coordenadas_link_human = pyautogui.locateOnScreen(
            image='image_ecac/i_a_human.png',
            grayscale=True,
            confidence=0.9
        )

        coordenadas_botao_seguir_desab = pyautogui.locateOnScreen(
            image='image_ecac/prosseguir_desabilitado.png',
            grayscale=True,
            confidence=0.9
        )

        if coordenadas_link_human and coordenadas_botao_seguir_desab:
            registrar_logs_execucao(
                'mensagem anti robo encontrado, será clicado...')
            pyautogui.click(
                coordenadas_link_human, duration=2)
            return True

        sleep(1)
        tempo += 1
        if tempo == 60:
            send_email_adm_anexo(
                'AÇÃO DEMORANDO ALÉM DO NECESSÁRIO PARA SER EXECUTADA')
            raise Exception(
                'AÇÃO DEMORANDO ALÉM DO NECESSÁRIO PARA SER EXECUTADA')


def espera_click_prosseguir_human():

    tempo = 1

    while (True):

        registrar_logs_execucao(
            'aguardando botao -> prosseguir ficar habilitado')

        coordenadas_link_human = pyautogui.locateOnScreen(
            image='image_ecac/human_ok.png',
            grayscale=True,
            confidence=0.9
        )

        if coordenadas_link_human:
            registrar_logs_execucao('botao -> prosseguir, habilitado!!')
            return True

        sleep(1)
        tempo += 1
        if tempo == 60:
            send_email_adm_anexo(
                'AÇÃO DEMORANDO ALÉM DO NECESSÁRIO PARA SER EXECUTADA')
            raise Exception(
                'AÇÃO DEMORANDO ALÉM DO NECESSÁRIO PARA SER EXECUTADA')


def clicar_selecionar_certificado(certificado):

    imagem1, imagem2 = identificar_imagem_referente_certificado(certificado)
    scrolada = -10
    x = 1208
    y = 178

    tempo = 1

    while (True):

        registrar_logs_execucao(
            'procurando imagem equivalente ao certificado esperado....')

        coordenadas_certificado_1 = pyautogui.locateOnScreen(
            image=f'image_certificados/{imagem1}',
            grayscale=True,
            confidence=0.9
        )

        coordenadas_certificado_2 = pyautogui.locateOnScreen(
            image=f'image_certificados/{imagem2}',
            grayscale=True,
            confidence=0.9
        )

        if coordenadas_certificado_1:
            registrar_logs_execucao('certificado encontrado, será clicado')
            pyautogui.click(coordenadas_certificado_1, duration=2)

            return True
        elif coordenadas_certificado_2:
            registrar_logs_execucao('certificado encontrado, será clicado')

            pyautogui.click(coordenadas_certificado_2, duration=2)
            return True
        elif imagem1 and imagem2:
            registrar_logs_execucao(
                'nao encontrou certificado, vamos scrollar para encontrar...')
            # scrolar:
            # clicar na barra de rolagem

            pyautogui.click(x, y, duration=1)

            pyautogui.scroll(scrolada)
            y += 10

        sleep(1)
        tempo += 1
        if tempo == 60:
            send_email_adm_anexo(
                'AÇÃO DEMORANDO ALÉM DO NECESSÁRIO PARA SER EXECUTADA')
            raise Exception(
                'AÇÃO DEMORANDO ALÉM DO NECESSÁRIO PARA SER EXECUTADA')


def clicar_botao_ok_certificado_digital():

    tempo = 1

    while (True):

        registrar_logs_execucao('procurando botao -> ok certificado digital')

        coordenadas_botao_azul_certificado = pyautogui.locateOnScreen(
            image='image_ecac/botao_ok_certificado_digital.png',
            grayscale=True,
            confidence=0.9
        )

        if coordenadas_botao_azul_certificado:
            registrar_logs_execucao(
                'botao-> ok certificado digital, encontrado, será clicado....')
            pyautogui.click(coordenadas_botao_azul_certificado, duration=2)
            return True

        sleep(1)
        tempo += 1
        if tempo == 60:
            send_email_adm_anexo(
                'AÇÃO DEMORANDO ALÉM DO NECESSÁRIO PARA SER EXECUTADA')
            raise Exception(
                'AÇÃO DEMORANDO ALÉM DO NECESSÁRIO PARA SER EXECUTADA')


def clicar_botao_prosseguir():

    tempo = 1

    while (True):

        registrar_logs_execucao('procurando botao-> prosseguir..')

        botao_prosseguir = pyautogui.locateOnScreen(
            image='image_ecac/botao_prosseguir.png',
            grayscale=True,
            confidence=0.9
        )

        if botao_prosseguir:
            registrar_logs_execucao('botao-> prosseguir, encontrado....')
            pyautogui.click(botao_prosseguir, duration=2)
            return True

        sleep(1)
        tempo += 1
        if tempo == 60:
            send_email_adm_anexo(
                'AÇÃO DEMORANDO ALÉM DO NECESSÁRIO PARA SER EXECUTADA')
            raise Exception(
                'AÇÃO DEMORANDO ALÉM DO NECESSÁRIO PARA SER EXECUTADA')


def clicar_filtro_sou_procurador():

    tempo = 1

    while (True):

        registrar_logs_execucao('procurando o check box -> procurador')

        check_box_procurador = pyautogui.locateOnScreen(
            image='image_ecac/check_box_procurador.png',
            grayscale=True,
            confidence=0.9
        )

        if check_box_procurador:
            registrar_logs_execucao('check box encontrado, será clicado....')
            pyautogui.click(check_box_procurador, duration=2)
            return True

        sleep(1)
        tempo += 1
        if tempo == 60:
            send_email_adm_anexo(
                'AÇÃO DEMORANDO ALÉM DO NECESSÁRIO PARA SER EXECUTADA')
            raise Exception(
                'AÇÃO DEMORANDO ALÉM DO NECESSÁRIO PARA SER EXECUTADA')


def reconhecer_campo_periodo_apuracao_inicial():

    tempo = 1

    while (True):

        registrar_logs_execucao('procurando campo apuração inicial....')

        campo_periodo_carregado = pyautogui.locateOnScreen(
            image='image_ecac/campo_periodo_inicial_carregado.png',
            grayscale=True,
            confidence=0.9
        )

        if campo_periodo_carregado:
            registrar_logs_execucao('campo apuração inicial encontrado....')
            pyautogui.click(campo_periodo_carregado)
            sleep(2)
            pyautogui.move(0, 20)
            sleep(2)
            pyautogui.click()
            return True

        sleep(1)
        tempo += 1
        if tempo == 60:
            send_email_adm_anexo(
                'AÇÃO DEMORANDO ALÉM DO NECESSÁRIO PARA SER EXECUTADA')
            raise Exception(
                'AÇÃO DEMORANDO ALÉM DO NECESSÁRIO PARA SER EXECUTADA')


def reconhecer_campo_saldo_pagar():

    tempo = 1

    while (True):

        registrar_logs_execucao('procurando campo saldo a pagar....')

        campo_periodo_carregado = pyautogui.locateOnScreen(
            image='image_ecac/saldo_pagar.png',
            grayscale=True,
            confidence=0.9
        )

        if campo_periodo_carregado:
            registrar_logs_execucao('campo saldo a pagar encontrado....')
            pyautogui.click(campo_periodo_carregado)
            sleep(2)
            pyautogui.move(0, 30, duration=2)
            sleep(2)
            pyautogui.doubleClick()
            sleep(2)
            pyautogui.hotkey('ctrl', 'c')

            return True

        sleep(1)
        tempo += 1
        if tempo == 60:
            send_email_adm_anexo(
                'AÇÃO DEMORANDO ALÉM DO NECESSÁRIO PARA SER EXECUTADA')
            raise Exception(
                'AÇÃO DEMORANDO ALÉM DO NECESSÁRIO PARA SER EXECUTADA')


def reconhecer_campo_periodo_final():

    tempo = 1

    while (True):

        registrar_logs_execucao('procurando campo apuração final....')

        campo_periodo_carregado = pyautogui.locateOnScreen(
            image='image_ecac/periodo_final.png',
            grayscale=True,
            confidence=0.9
        )

        if campo_periodo_carregado:
            registrar_logs_execucao('campo apuração final encontrado....')
            pyautogui.click(campo_periodo_carregado)
            sleep(2)
            pyautogui.move(0, 20)
            sleep(2)
            pyautogui.click()
            return True

        sleep(1)
        tempo += 1
        if tempo == 60:
            send_email_adm_anexo(
                'AÇÃO DEMORANDO ALÉM DO NECESSÁRIO PARA SER EXECUTADA')
            raise Exception(
                'AÇÃO DEMORANDO ALÉM DO NECESSÁRIO PARA SER EXECUTADA')


def reconhecer_cliente():

    tempo = 1

    while (True):

        registrar_logs_execucao('procurando cliente final....')

        cnpj = pyautogui.locateOnScreen(
            image='image_ecac/cnpj.png',
            grayscale=True,
            confidence=0.9
        )
        cpf = pyautogui.locateOnScreen(
            image='image_ecac/cpf.png',
            grayscale=True,
            confidence=0.9
        )

        if cnpj or cpf:
            registrar_logs_execucao('cliente final encontrado....')
            pyautogui.click(cnpj) if cnpj else pyautogui.click(cpf)

            return True

        sleep(1)
        tempo += 1
        if tempo == 60:
            send_email_adm_anexo(
                'AÇÃO DEMORANDO ALÉM DO NECESSÁRIO PARA SER EXECUTADA')
            raise Exception(
                'AÇÃO DEMORANDO ALÉM DO NECESSÁRIO PARA SER EXECUTADA')


def seleciona_outorgante():

    tempo = 1

    while (True):

        registrar_logs_execucao('procurando icone-> todos outorgantes..')

        drop_box_todos_outorgantes = pyautogui.locateOnScreen(
            image='image_ecac/todos_outorgantes.png',
            grayscale=True,
            confidence=0.9
        )

        drop_box_todos_outorgantes_1 = pyautogui.locateOnScreen(
            image='image_ecac/todos_outorgantes_1.png',
            grayscale=True,
            confidence=0.9
        )

        drop_box_todos_outorgantes_2 = pyautogui.locateOnScreen(
            image='image_ecac/todos_outorgantes_2.png',
            grayscale=True,
            confidence=0.9
        )

        if drop_box_todos_outorgantes or drop_box_todos_outorgantes_1:
            registrar_logs_execucao(
                'icone->todos outorgantes, encontrado, será clicado....')
            if drop_box_todos_outorgantes:
                pyautogui.click(drop_box_todos_outorgantes, duration=2)
            elif drop_box_todos_outorgantes_1:
                pyautogui.click(drop_box_todos_outorgantes_1, duration=2)
            elif drop_box_todos_outorgantes_2:
                pyautogui.click(drop_box_todos_outorgantes_2, duration=2)

            return True

        sleep(1)
        tempo += 1
        if tempo == 60:
            send_email_adm_anexo(
                'AÇÃO DEMORANDO ALÉM DO NECESSÁRIO PARA SER EXECUTADA')
            raise Exception(
                'AÇÃO DEMORANDO ALÉM DO NECESSÁRIO PARA SER EXECUTADA')


def seleciona_outorgante_cpf_cnpj():

    tempo = 1

    while (True):

        drop_box_outorgante_cnpj = pyautogui.locateOnScreen(
            image='image_ecac/outorgante_cnpj.png',
            grayscale=True,
            confidence=0.9
        )

        drop_box_outorgante_cpf = pyautogui.locateOnScreen(
            image='image_ecac/outorgante_cpf.png',
            grayscale=True,
            confidence=0.9
        )

        if drop_box_outorgante_cnpj or drop_box_outorgante_cpf:
            if drop_box_outorgante_cpf:
                pyautogui.click(drop_box_outorgante_cpf, duration=2)
            elif drop_box_outorgante_cnpj:
                pyautogui.click(drop_box_outorgante_cnpj, duration=2)

            return True

        sleep(1)
        tempo += 1
        if tempo == 60:
            send_email_adm_anexo(
                'AÇÃO DEMORANDO ALÉM DO NECESSÁRIO PARA SER EXECUTADA')
            raise Exception(
                'AÇÃO DEMORANDO ALÉM DO NECESSÁRIO PARA SER EXECUTADA')


def clicar_botao_cancela_selecao_outorgantes():

    tempo = 1

    while (True):

        registrar_logs_execucao('procurando cancelar selecao outorgantes...')

        botao_cancela_selecao_outorgante = pyautogui.locateOnScreen(
            image='image_ecac/outorgantes_cancela_selecao.png',
            grayscale=True,
            confidence=0.9
        )

        if botao_cancela_selecao_outorgante:
            pyautogui.click(botao_cancela_selecao_outorgante, duration=2)
            return True

        sleep(1)
        tempo += 1
        if tempo == 60:
            send_email_adm_anexo(
                'AÇÃO DEMORANDO ALÉM DO NECESSÁRIO PARA SER EXECUTADA')
            raise Exception(
                'AÇÃO DEMORANDO ALÉM DO NECESSÁRIO PARA SER EXECUTADA')


def tela_bloco_de_notas():

    tempo = 1

    while (True):

        registrar_logs_execucao('procurando tela bloco notas...')

        tela_bloco_notas = pyautogui.locateOnScreen(
            image='image_ecac/tela_bloco_notas.png',
            grayscale=True,
            confidence=0.9
        )

        if tela_bloco_notas:
            registrar_logs_execucao('tela bloco de notas encontrada')
            # pyautogui.click(botao_cancela_selecao_outorgante, duration=2)
            return True

        sleep(1)
        tempo += 1
        if tempo == 60:
            send_email_adm_anexo(
                'AÇÃO DEMORANDO ALÉM DO NECESSÁRIO PARA SER EXECUTADA')
            raise Exception(
                'AÇÃO DEMORANDO ALÉM DO NECESSÁRIO PARA SER EXECUTADA')


def fechar_janela_bloco():

    tempo = 1

    while (True):

        registrar_logs_execucao('procurando cancelar selecao outorgantes...')

        fechar_janela_bloco = pyautogui.locateOnScreen(
            image='image_ecac/fechar_janela_bloco.png',
            grayscale=True,
            confidence=0.9
        )

        if fechar_janela_bloco:
            pyautogui.click(fechar_janela_bloco, duration=2)
            return True

        sleep(1)
        tempo += 1
        if tempo == 60:
            send_email_adm_anexo(
                'AÇÃO DEMORANDO ALÉM DO NECESSÁRIO PARA SER EXECUTADA')
            raise Exception(
                'AÇÃO DEMORANDO ALÉM DO NECESSÁRIO PARA SER EXECUTADA')


def botao_salvar():

    tempo = 1

    while (True):

        registrar_logs_execucao('procurando botao salvar...')

        botao_salvar = pyautogui.locateOnScreen(
            image='image_ecac/botao_salvar.png',
            grayscale=True,
            confidence=0.9
        )

        if botao_salvar:
            registrar_logs_execucao('botao salvar encontrado')
            # pyautogui.click(botao_cancela_selecao_outorgante, duration=2)
            return botao_salvar

        sleep(1)
        tempo += 1
        if tempo == 60:
            send_email_adm_anexo(
                'AÇÃO DEMORANDO ALÉM DO NECESSÁRIO PARA SER EXECUTADA')
            raise Exception(
                'AÇÃO DEMORANDO ALÉM DO NECESSÁRIO PARA SER EXECUTADA')


def botao_salvar_sobrescrever_sim():

    for i in range(3):

        registrar_logs_execucao('procurando botao sobrescrever arquivo...')

        botao_salvar = pyautogui.locateOnScreen(
            image='image_ecac/botao_sim_sobrescrever.png',
            grayscale=True,
            confidence=0.9
        )

        if botao_salvar:
            registrar_logs_execucao('botao sobrescrever encontrado...')
            pyautogui.click(botao_salvar, duration=2)
            return True
    registrar_logs_execucao('nao encontrado botao sobrescrever')


def botao_emitir_darf():

    tempo = 1

    while (True):

        registrar_logs_execucao('procurando botao emitir darf...')

        botao_salvar = pyautogui.locateOnScreen(
            image='image_ecac/button_emitir_darf.png',
            grayscale=True,
            confidence=0.9
        )

        if botao_salvar:
            registrar_logs_execucao('encontrado botao emitir darf...')
            pyautogui.click(botao_salvar, duration=2)
            return True

        sleep(1)
        tempo += 1
        if tempo == 60:
            send_email_adm_anexo(
                'AÇÃO DEMORANDO ALÉM DO NECESSÁRIO PARA SER EXECUTADA')
            raise Exception(
                'AÇÃO DEMORANDO ALÉM DO NECESSÁRIO PARA SER EXECUTADA')


def botao_ok_guia():

    tempo = 1

    while (True):

        registrar_logs_execucao('procurando botao ok guia...')
        registrar_logs_execucao('procurando botao ok guia...')

        botao_salvar = pyautogui.locateOnScreen(
            image='image_ecac/button_ok_guia.png',
            grayscale=True,
            confidence=0.9
        )

        if botao_salvar:
            registrar_logs_execucao('encontrado botao ok guia...')
            pyautogui.click(botao_salvar, duration=2)
            return True

        sleep(1)
        tempo += 1
        if tempo == 60:
            send_email_adm_anexo(
                'AÇÃO DEMORANDO ALÉM DO NECESSÁRIO PARA SER EXECUTADA')
            raise Exception(
                'AÇÃO DEMORANDO ALÉM DO NECESSÁRIO PARA SER EXECUTADA')


def pesquisar_cliente():

    tempo = 1

    while (True):

        registrar_logs_execucao('procurando botao -> pesquisar cliente...')

        botao_pesquisar_clientes = pyautogui.locateOnScreen(
            image='image_ecac/botao_pesquisar.png',
            grayscale=True,
            confidence=0.9
        )

        if botao_pesquisar_clientes:
            registrar_logs_execucao(
                'botao-> pesquisar cliente, encontrado....')
            pyautogui.click(botao_pesquisar_clientes, duration=2)
            return True

        sleep(1)
        tempo += 1
        if tempo == 60:
            send_email_adm_anexo(
                'AÇÃO DEMORANDO ALÉM DO NECESSÁRIO PARA SER EXECUTADA')
            raise Exception(
                'AÇÃO DEMORANDO ALÉM DO NECESSÁRIO PARA SER EXECUTADA')


def se_nao_ha_informacoes_serem_mostradas():

    coordenadas_nao_ha_inf = pyautogui.locateOnScreen(
        'image/nao_ha_informacoes_pesquisa_s_1299.png',  grayscale=True, confidence=0.9)

    if coordenadas_nao_ha_inf:
        registrar_logs_execucao(
            'nao ha informacoes a serem mostradas na consulta da tarefa em andamento...')
        return True
    else:
        return False


def botao_sim():
    botao_sim = pyautogui.locateOnScreen(
        'image/botao_sim.png',  grayscale=True, confidence=0.9)
    pyautogui.click(botao_sim)
    # botao_sim.click()


def reagendar_agilizar_tarefa():
    sleep(1)
    # clicar na tarefa para reagendar
    pyautogui.click(21, 530, duration=2)

    sleep(1)
    # clicar no botao reagendar
    pyautogui.click(562, 453, duration=2)
    sleep(1)

    # clicar pra confirmar
    botao_sim()
    sleep(5)

    # clicar em agilizar
    pyautogui.click(586, 452, duration=2)

    i = 1
    total = 30
    while (i <= 30):
        registrar_logs_execucao(
            f'aguardando agilizar tarefa {i} / {total}')
        sleep(1)
        i += 1
    registrar_logs_execucao(
        'tempo esgotado...seguindo para proxima etapa....')

    sleep(30)


# def reagendar_agilizar_tarefa_esocial():
#     pass


def status_tarefa_andamento(CODIGO_CLIENTE, NOME_CLIENTE, competencia):
    # clicar em status da tarefa
    sleep(1)
    pyautogui.click(986, 409, duration=2)
    sleep(1)
    pyautogui.write('Em')
    sleep(1)
    pyautogui.press('enter')
    sleep(1)
    # clicar em consultar
    pyautogui.click(1480, 406, duration=2)
    sleep(2)

    if se_nao_ha_informacoes_serem_mostradas():
        return True
    else:
        reagendar_agilizar_tarefa()
        return False


def status_tarefa_pendentes(CODIGO_CLIENTE, NOME_CLIENTE, competencia):
    sleep(1)
    # clicar em status da tarefa
    pyautogui.click(986, 409, duration=2)
    sleep(1)
    pyautogui.write('pe')
    sleep(1)
    pyautogui.press('enter')
    sleep(1)
    # clicar em consultar
    pyautogui.click(1480, 406, duration=2)
    sleep(2)

    if se_nao_ha_informacoes_serem_mostradas():
        return False
    else:

        gravar_imagem_padrao_tela_s_1299(CODIGO_CLIENTE)
        # enviar_email_padrao_s_1299(
        #     CODIGO_CLIENTE, NOME_CLIENTE, competencia, 'pendencias')
        return True


def status_tarefa_rejeitada(CODIGO_CLIENTE, NOME_CLIENTE, competencia):
    sleep(1)
    # clicar em status da tarefa
    pyautogui.click(986, 409, duration=1)
    sleep(1)
    pyautogui.write('r')
    sleep(1)
    pyautogui.press('enter')
    sleep(1)
    # clicar em consultar
    pyautogui.click(1480, 406, duration=1)
    sleep(2)

    if se_nao_ha_informacoes_serem_mostradas():
        return False
    else:
        gravar_imagem_padrao_tela_s_1299(CODIGO_CLIENTE)
        # enviar_email_padrao_s_1299(
        #     CODIGO_CLIENTE, NOME_CLIENTE, competencia, 'rejeitadas')
        return True


def status_tarefa_processada(CODIGO_CLIENTE, NOME_CLIENTE, dic_dados, nome_pasta_excel, competencia):
    sleep(1)
    # clicar em status da tarefa
    pyautogui.click(986, 409, duration=2)
    sleep(1)
    pyautogui.write('pr')
    sleep(1)
    pyautogui.press('enter')
    sleep(1)
    # clicar em consultar
    pyautogui.click(1480, 406, duration=2)
    sleep(2)

    if se_nao_ha_informacoes_serem_mostradas():
        return False
    else:
        gravar_imagem_padrao_tela_s_1299(CODIGO_CLIENTE)

        dic_dados.get(CODIGO_CLIENTE)['Questor_s_1299'] = True
        # gravar_valores_excel(dic_dados, nome_pasta_excel)

        # enviar_email_padrao_s_1299(
        #     CODIGO_CLIENTE, NOME_CLIENTE, competencia, 'processadas')
        return True


def verificar_status_tarefas_atual(CODIGO_CLIENTE, NOME_CLIENTE, dic_dados, nome_pasta_excel, competencia):

    tempo = 1
    tentativas = False
    while (True):

        andamento = status_tarefa_andamento(
            CODIGO_CLIENTE, NOME_CLIENTE, competencia)

        pendente = status_tarefa_pendentes(
            CODIGO_CLIENTE, NOME_CLIENTE, competencia)

        if pendente and not tentativas:
            reagendar_agilizar_tarefa()
            tentativas = True

        if pendente and tentativas:
            break

        rejeitada = status_tarefa_rejeitada(
            CODIGO_CLIENTE, NOME_CLIENTE, competencia)

        if rejeitada:
            break

        processada = status_tarefa_processada(
            CODIGO_CLIENTE, NOME_CLIENTE, dic_dados, nome_pasta_excel, competencia)

        if processada:
            break

        gravar_imagem_padrao_tela_s_1299(CODIGO_CLIENTE)

        # enviar_email_padrao_s_1299(
        #     CODIGO_CLIENTE, NOME_CLIENTE, competencia, 'generico')
        break
        # mandar email genérico com msg que não foi possivel gerar nesta data
        # possivelmente há pendências anteriores


def aguardar_conclusao_processamento_reinf_s_1299(CODIGO_CLIENTE, NOME_CLIENTE, dic_dados, nome_pasta_excel, competencia):

    verificar_status_tarefas_atual(
        CODIGO_CLIENTE, NOME_CLIENTE, dic_dados, nome_pasta_excel, competencia)
