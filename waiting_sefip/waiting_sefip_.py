from time import sleep
from log_.gravar_log import registrar_logs_execucao
import pyautogui
from config_email.criacao_email import send_email_adm_anexo
from robo_sefip.conexao_sefip import conectar_sefip


def waiting_botao_sim_sobescrever_sefip():
    registrar_logs_execucao(
        f'botao_sim_sobescrever_sefip == [.......PROCURANDO.......]')

    coordenada_imagem = pyautogui.locateOnScreen(
        image=f'imagens_sefip/botao_sim_sobescrever_sefip.png',
        grayscale=True,
        confidence=0.9
    )

    if coordenada_imagem:

        registrar_logs_execucao(
            f'botao_sim_sobescrever_sefip == [ENCONTRADO \o/\o/]')

        pyautogui.click(coordenada_imagem, duration=2)


def waiting_botao_ok_finalizar_importacao_sefip():

    for i in range(10):
        registrar_logs_execucao(
            f'botao ok finalizar sefip == [.......PROCURANDO.......]')

        coordenada_imagem = pyautogui.locateOnScreen(
            image=f'imagens_sefip/botao_ok_importacao_sefip.png',
            grayscale=True,
            confidence=0.9
        )

        if coordenada_imagem:

            registrar_logs_execucao(
                f'botao ok finalizar sefip == [ENCONTRADO \o/\o/]')

            pyautogui.click(coordenada_imagem, duration=2)
        sleep(1)


def waiting_botao_ok_finalizar_importacao_sefip_2():

    for i in range(10):
        registrar_logs_execucao(
            f'botao ok finalizar sefip == [.......PROCURANDO.......]')

        coordenada_imagem = pyautogui.locateOnScreen(
            image=f'imagens_sefip/botao_ok_finalizacao.png',
            grayscale=True,
            confidence=0.9
        )

        if coordenada_imagem:

            registrar_logs_execucao(
                f'botao ok finalizar sefip == [ENCONTRADO \o/\o/]')

            pyautogui.click(coordenada_imagem, duration=2)
        sleep(1)


def waiting_tela_inicial_carregar_sefip():

    time = 1

    while True:

        registrar_logs_execucao(f'tela_inicial == [.......PROCURANDO.......]')

        coordenada_imagem = pyautogui.locateOnScreen(
            image=f'imagens_sefip/tela_inicial_carregada.png',
            grayscale=True,
            confidence=0.9
        )

        if coordenada_imagem:

            registrar_logs_execucao(f'tela inicial == [ENCONTRADO \o/\o/]')

            return coordenada_imagem

        sleep(1)
        time += 1

        if time == 10:
            conectar_sefip()

        if time == 60:

            send_email_adm_anexo(assunto_email='Erro -> Ação demorando além do necessário',
                                 conteudo='nao carregou tela inicial', anexo_email='')

            raise Exception('Ação demorando além do necessário!!!')


def waiting_executar_sefip():

    time = 1

    while True:

        registrar_logs_execucao(
            f'botao executar sefip == [.......PROCURANDO.......]')

        coordenada_imagem = pyautogui.locateOnScreen(
            image=f'imagens_sefip/botao_executar_sefip.png',
            grayscale=True,
            confidence=0.9
        )

        if coordenada_imagem:

            registrar_logs_execucao(
                f'botao executar sefip == [ENCONTRADO \o/\o/]')

            pyautogui.click(coordenada_imagem, duration=2)

            return coordenada_imagem

        sleep(1)
        time += 1

        if time == 10:
            conectar_sefip()

        if time == 60:

            send_email_adm_anexo(assunto_email='Erro -> Ação demorando além do necessário',
                                 conteudo='nao carregou botao executar sefip', anexo_email='')

            raise Exception('Ação demorando além do necessário!!!')


def waiting_botao_maximixar_tela_sefip():

    time = 1

    while True:

        registrar_logs_execucao(
            f'botao maximixar tela == [.......PROCURANDO.......]')

        coordenada_imagem = pyautogui.locateOnScreen(
            image=f'imagens_sefip/maximizar_janela_sefip.png',
            grayscale=True,
            confidence=0.9
        )

        if coordenada_imagem:

            registrar_logs_execucao(
                f'botao maximixar tela == [ENCONTRADO \o/\o/]')

            pyautogui.click(coordenada_imagem, duration=2)

            break

        sleep(1)
        time += 1

        if time == 60:

            send_email_adm_anexo(assunto_email='Erro -> Ação demorando além do necessário',
                                 conteudo='nao encontrou botao maximixar tela', anexo_email='')

            raise Exception('Ação demorando além do necessário!!!')


def waiting_tela_principal_sefip():

    time = 1

    while True:

        registrar_logs_execucao(
            f'tela principal sefip == [.......PROCURANDO.......]')

        coordenada_imagem = pyautogui.locateOnScreen(
            image=f'imagens_sefip/tela_principal_sefip.png',
            grayscale=True,
            confidence=0.9
        )

        if coordenada_imagem:

            registrar_logs_execucao(
                f'tela principal sefip == [ENCONTRADO \o/\o/]')

            pyautogui.click(coordenada_imagem, duration=2)

            break

        sleep(1)
        time += 1

        if time == 60:

            send_email_adm_anexo(assunto_email='Erro -> Ação demorando além do necessário',
                                 conteudo='nao encontrou botao maximixar tela', anexo_email='')

            raise Exception('Ação demorando além do necessário!!!')


def waiting_botao_importar_sefip():

    time = 1

    while True:

        registrar_logs_execucao(
            f'botao importar sefip == [.......PROCURANDO.......]')

        coordenada_imagem = pyautogui.locateOnScreen(
            image=f'imagens_sefip/botao_importar_sefip.png',
            grayscale=True,
            confidence=0.9
        )

        if coordenada_imagem:

            registrar_logs_execucao(
                f'botao importar sefip == [ENCONTRADO \o/\o/]')

            pyautogui.click(coordenada_imagem, duration=2)

            break

        sleep(1)
        time += 1

        if time == 60:

            send_email_adm_anexo(assunto_email='Erro -> Ação demorando além do necessário',
                                 conteudo='nao encontrou botao maximixar tela', anexo_email='')

            raise Exception('Ação demorando além do necessário!!!')


def waiting_botao_ok_finalizar_execucao_sefip():

    time = 1

    while True:

        registrar_logs_execucao(
            f'botao ok finalizar execução sefip == [.......PROCURANDO.......]')

        coordenada_imagem = pyautogui.locateOnScreen(
            image=f'imagens_sefip/botao_ok_importacao_sefip.png',
            grayscale=True,
            confidence=0.9
        )

        if coordenada_imagem:

            registrar_logs_execucao(
                f'botao ok finalizar execução sefip == [ENCONTRADO \o/\o/]')

            return coordenada_imagem

        sleep(1)
        time += 1

        if time == 60:

            send_email_adm_anexo(assunto_email='Erro -> Ação demorando além do necessário',
                                 conteudo='nao encontrou botao maximixar tela', anexo_email='')

            raise Exception('Ação demorando além do necessário!!!')


def waiting_botao_ok_finalizar_execucao_sefip_2():

    time = 1

    while True:

        registrar_logs_execucao(
            f'botao ok finalizar execução sefip == [.......PROCURANDO.......]')

        coordenada_imagem = pyautogui.locateOnScreen(
            image=f'imagens_sefip/botao_ok_importacao_sefip_2.png',
            grayscale=True,
            confidence=0.9
        )

        if coordenada_imagem:

            registrar_logs_execucao(
                f'botao ok finalizar execução sefip == [ENCONTRADO \o/\o/]')

            return coordenada_imagem

        sleep(1)
        time += 1

        if time == 60:

            send_email_adm_anexo(assunto_email='Erro -> Ação demorando além do necessário',
                                 conteudo='nao encontrou botao maximixar tela', anexo_email='')

            raise Exception('Ação demorando além do necessário!!!')


def waiting_botao_ok_finalizar_execucao_sefip_3():

    time = 1

    while True:

        registrar_logs_execucao(
            f'botao ok finalizar execução sefip == [.......PROCURANDO.......]')

        coordenada_imagem = pyautogui.locateOnScreen(
            image=f'imagens_sefip/botao_ok_importacao_sefip_4.png',
            grayscale=True,
            confidence=0.9
        )

        if coordenada_imagem:

            registrar_logs_execucao(
                f'botao ok finalizar execução sefip == [ENCONTRADO \o/\o/]')

            return coordenada_imagem

        sleep(1)
        time += 1

        if time == 60:

            send_email_adm_anexo(assunto_email='Erro -> Ação demorando além do necessário',
                                 conteudo='nao encontrou botao maximixar tela', anexo_email='')

            raise Exception('Ação demorando além do necessário!!!')


def waiting_botao_salvar_sefip_final():

    time = 1

    while True:

        registrar_logs_execucao(
            f'botao salvar sefip final == [.......PROCURANDO.......]')

        coordenada_imagem = pyautogui.locateOnScreen(
            image=f'imagens_sefip/botao_salvar_sefip_final.png',
            grayscale=True,
            confidence=0.9
        )

        if coordenada_imagem:

            registrar_logs_execucao(
                f'botao salvar sefip final == [ENCONTRADO \o/\o/]')

            pyautogui.click(coordenada_imagem, duration=2)

            break

        sleep(1)
        time += 1

        if time == 60:

            send_email_adm_anexo(assunto_email='Erro -> Ação demorando além do necessário',
                                 conteudo='nao encontrou botao maximixar tela', anexo_email='')

            raise Exception('Ação demorando além do necessário!!!')


def waiting_botao_abrir_arquivo_sefip():

    time = 1

    while True:

        registrar_logs_execucao(
            f'botao abrir arquivo sefip == [.......PROCURANDO.......]')

        coordenada_imagem = pyautogui.locateOnScreen(
            image=f'imagens_sefip/botao_abrir_arquivo_sefip.png',
            grayscale=True,
            confidence=0.9
        )

        if coordenada_imagem:

            registrar_logs_execucao(
                f'botao abrir arquivo sefip == [ENCONTRADO \o/\o/]')

            return coordenada_imagem

        sleep(1)
        time += 1

        if time == 60:

            send_email_adm_anexo(assunto_email='Erro -> Ação demorando além do necessário',
                                 conteudo='nao encontrou botao maximixar tela', anexo_email='')

            raise Exception('Ação demorando além do necessário!!!')


def waiting_mensagem_erro_arquivo():

    time = 1

    while True:

        registrar_logs_execucao(
            f'mensagem erro == [.......PROCURANDO.......]')

        coordenada_imagem = pyautogui.locateOnScreen(
            image=f'imagens_sefip/erro_arquivo_de_dados_nao_localizado.png',
            grayscale=True,
            confidence=0.9
        )

        if coordenada_imagem:

            registrar_logs_execucao(
                f'mensagem erro == [ENCONTRADO \o/\o/]')

            return coordenada_imagem

        sleep(1)
        time += 1

        if time == 60:

            send_email_adm_anexo(assunto_email='Erro -> Ação demorando além do necessário',
                                 conteudo='nao encontrou botao maximixar tela', anexo_email='')

            raise Exception('Ação demorando além do necessário!!!')


def botao_localizar_caminho_arquivo():

    time = 1

    while True:

        registrar_logs_execucao(
            f'botao localizar caminho arquivo == [.......PROCURANDO.......]')

        coordenada_imagem = pyautogui.locateOnScreen(
            image=f'imagens_sefip/botao_localizar_caminho_arquivo.png',
            grayscale=True,
            confidence=0.9
        )

        if coordenada_imagem:

            registrar_logs_execucao(
                f'botao localizar caminho arquivo == [ENCONTRADO \o/\o/]')

            pyautogui.click(coordenada_imagem, duration=2)

            break

        sleep(1)
        time += 1

        if time == 60:

            send_email_adm_anexo(assunto_email='Erro -> Ação demorando além do necessário',
                                 conteudo='nao encontrou botao maximixar tela', anexo_email='')

            raise Exception('Ação demorando além do necessário!!!')


def botao_validar_arquivo():

    time = 1

    while True:

        registrar_logs_execucao(
            f'botao validar arquivo == [.......PROCURANDO.......]')

        coordenada_imagem = pyautogui.locateOnScreen(
            image=f'imagens_sefip/validar_arquivo.png',
            grayscale=True,
            confidence=0.9
        )

        if coordenada_imagem:

            registrar_logs_execucao(
                f'botao validar arquivo == [ENCONTRADO \o/\o/]')

            pyautogui.click(coordenada_imagem, duration=2)

            break

        sleep(1)
        time += 1

        if time == 60:

            send_email_adm_anexo(assunto_email='Erro -> Ação demorando além do necessário',
                                 conteudo='nao encontrou botao maximixar tela', anexo_email='')

            raise Exception('Ação demorando além do necessário!!!')


def tela_grf_guia():

    time = 1

    while True:

        registrar_logs_execucao(
            f'tela GRF guia == [.......PROCURANDO.......]')

        coordenada_imagem = pyautogui.locateOnScreen(
            image=f'imagens_sefip/tela_grf_guia.png',
            grayscale=True,
            confidence=0.9
        )

        if coordenada_imagem:

            registrar_logs_execucao(
                f'tela GRF guia == [ENCONTRADO \o/\o/]')

            pyautogui.click(coordenada_imagem, duration=2)

            break

        sleep(1)
        time += 1

        if time == 60:

            send_email_adm_anexo(assunto_email='Erro -> Ação demorando além do necessário',
                                 conteudo='nao encontrou botao maximixar tela', anexo_email='')

            raise Exception('Ação demorando além do necessário!!!')


def tela_gravacao_guia():

    time = 1

    while True:

        registrar_logs_execucao(
            f'tela caminho gravação guia == [.......PROCURANDO.......]')

        coordenada_imagem = pyautogui.locateOnScreen(
            image=f'imagens_sefip/tela_caminho_gravacao_guia.png',
            grayscale=True,
            confidence=0.9
        )

        if coordenada_imagem:

            registrar_logs_execucao(
                f'tela caminho gravação guia == [ENCONTRADO \o/\o/]')

            pyautogui.click(coordenada_imagem, duration=2)

            break

        sleep(1)
        time += 1

        if time == 60:

            send_email_adm_anexo(assunto_email='Erro -> Ação demorando além do necessário',
                                 conteudo='nao encontrou botao maximixar tela', anexo_email='')

            raise Exception('Ação demorando além do necessário!!!')


def guia_informacao_finalizado():

    time = 1

    while True:

        registrar_logs_execucao(
            f'guia informacao == [.......PROCURANDO.......]')

        coordenada_imagem = pyautogui.locateOnScreen(
            image=f'imagens_sefip/guia_informacao.png',
            grayscale=True,
            confidence=0.9
        )

        if coordenada_imagem:

            registrar_logs_execucao(
                f'guia informacao == [ENCONTRADO \o/\o/]')

            pyautogui.click(coordenada_imagem, duration=2)

            break

        sleep(1)
        time += 1

        if time == 60:

            send_email_adm_anexo(assunto_email='Erro -> Ação demorando além do necessário',
                                 conteudo='nao encontrou botao maximixar tela', anexo_email='')

            raise Exception('Ação demorando além do necessário!!!')
