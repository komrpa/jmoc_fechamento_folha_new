# importar SEFIP.RE
from robo_sefip.conexao_sefip import *
from waiting_sefip.waiting_sefip_ import *
from time import sleep
from log_.gravar_log import registrar_logs_execucao
from digitar_texto.digitar_textos import digitar_textos


def importar_sefip_re():

    conectar_sefip()

    sleep(2)

    waiting_tela_inicial_carregar_sefip()

    sleep(2)

    waiting_botao_maximixar_tela_sefip()

    sleep(2)

    waiting_botao_importar_sefip()

    sleep(2)

    botao_abrir = waiting_botao_abrir_arquivo_sefip()

    sleep(2)

    # digitar caminho onde esta salvo arquivo da sefip
    path_default = f'{path_default}\\SEFIP.RE'
    digitar_textos(path_default)
    # digitar_textos('W:\\Pessoal\\Fechamento de folha automatizado\\Automação Folha\\Configuração 0003 - Teste Folha Automatizada\\072023\\Empresa 0270 - DAROS EDIFICAÇÕES E OBRAS LTDA\\SEFIP.RE')

    sleep(2)

    pyautogui.click(botao_abrir, duration=2)

    sleep(2)

    # tela informação

    # procura tela informacao
    coordenada_imagem_1 = pyautogui.locateOnScreen(
        image=f'imagens_sefip/tela_informacao.png',
        grayscale=True,
        confidence=0.9
    )

    # confirma sim
    pyautogui.press('enter')
    sleep(3)
    # confirma OK
    pyautogui.press('enter')
    sleep(2)
