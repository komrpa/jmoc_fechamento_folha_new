import os
import shutil
from config_email.criacao_email import send_email_adm_anexo
from models.path_files import PathFiles
from log_.gravar_log import registrar_logs_execucao


def calcular_mes(valor, ano):

    dict = {
        '01': f'01.{ano}',
        '02': f'02.{ano}',
        '03': f'03.{ano}',
        '04': f'04.{ano}',
        '05': f'05.{ano}',
        '06': f'06.{ano}',
        '07': f'07.{ano}',
        '08': f'08.{ano}',
        '09': f'09.{ano}',
        '10': f'10.{ano}',
        '11': f'11.{ano}',
        '12': f'12.{ano}',
    }

    return dict.get(valor)


def criar_nova_pasta(caminho):
    os.makedirs(caminho)


def existe_essa_pasta(caminho):
    return os.path.exists(caminho)


def get_download_path():
    """Returns the default downloads path for linux or windows"""
    if os.name == 'nt':
        import winreg
        sub_key = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
        downloads_guid = '{374DE290-123F-4565-9164-39C4925E467B}'
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
            location = winreg.QueryValueEx(key, downloads_guid)[0]
        return location
    return os.path.join(os.path.expanduser('~'), 'downloads')


def mover_arquivos_gerados_questor(competencia, dados, caminho_destino):

    # competencia 072023

    # caminho_padrao_origem = f'W:\\Pessoal\\Fechamento de folha automatizado\\Automação Folha\\Configuração 0003 - Teste Folha Automatizada\\{competencia}'
    caminho_padrao_origem = PathFiles().found_folder_config(
        config=dados['Configuracao'], competencia=competencia)

    try:
        registrar_logs_execucao(f'{os.listdir(caminho_padrao_origem)}')
        for empresa in os.listdir(caminho_padrao_origem):
            registrar_logs_execucao(
                f"{int(empresa.split('-')[0].split()[1])}, {int(dados['CÓD'])}")
            if int(dados['CÓD']) == int(empresa.split('-')[0].split()[1]):
                origem = f'{caminho_padrao_origem}\\{empresa}\\'
                registrar_logs_execucao(origem)
                for arquivo in os.listdir(origem):
                    caminho_origem = os.path.join(origem+os.sep+arquivo)
                    registrar_logs_execucao(f'movendo---->{caminho_origem}')
                    shutil.move(caminho_origem, caminho_destino)

                # os.rmdir(origem)
    except Exception as e:
        raise Exception(f'nao conseguiu finaliza copia dos arquivos {e}')


def mover_arquivo_SFP_SEFIP(caminho_destino):

    caminho_origem = 'C:\\Users\\kompagrpa\\SEFIP'

    for file in os.listdir(caminho_origem):
        if file.split('.')[-1] == 'SFP':
            origem = os.path.join(caminho_origem, file)
            shutil.move(origem, caminho_destino)


def mover_arquivos_downloads(caminho_destino):

    # caminho_origem = 'C:\\Users\\kompagrpa\\SEFIP'
    caminho_origem = get_download_path()

    for file in os.listdir(caminho_origem):
        if file.split('.')[-1].upper() in ['PDF', 'XML']:
            origem = os.path.join(caminho_origem, file)
            shutil.move(origem, caminho_destino)


def clear_downloads():

    caminho_origem = get_download_path()

    for file in os.listdir(caminho_origem):
        file_delete = os.path.join(caminho_origem, file)
        try:
            if os.path.isfile(file_delete):
                os.remove(file_delete)
        except:
            pass


def mover_arquivos_extensions_para_pasta_sefip(path_default):

    pasta_sefip = os.path.join(path_default, 'SEFIP')

    for file in os.listdir(path_default):
        if file.split('.')[-1].upper() in ['RE', 'XML', 'SFP']:
            origem = os.path.join(path_default, file)
            shutil.move(origem, pasta_sefip)


def remover_arquivo_fap(path_default):

    pasta_sefip = os.path.join(path_default)

    for file in os.listdir(path_default):
        if file.split('.')[-1].upper() in ['TXT']:
            origem = os.path.join(path_default, file)
            if os.path.isfile(origem):
                os.remove(origem)


def mover_arquivos_para_pasta_sefip(path_default):

    pasta_sefip = os.path.join(path_default, 'SEFIP')

    for file in os.listdir(path_default):
        for subfile in ['ANALITICOGPS', 'PROTOCOLO', 'RUBRICA']:
            if subfile in file.upper():
                origem = os.path.join(path_default, file)
                shutil.move(origem, pasta_sefip)


def mover_arquivos_para_pasta_dctfweb(path_default):

    PASTA_DCTFWEB = os.path.join(path_default, 'DCTFWEB')

    for file in os.listdir(path_default):
        for subfile in ['DECLARACAOCOMPLETA', 'RECIBO_']:
            if subfile in file.upper():
                origem = os.path.join(path_default, file)
                shutil.move(origem, PASTA_DCTFWEB)


def movendo_quatro_relatorios_sefip(caminho_destino):

    caminho_origem = 'W:\\Publico\\LabKom\\robo_temp'

    for file in os.listdir(caminho_origem):
        origem = os.path.join(caminho_origem, file)
        shutil.move(origem, caminho_destino)


def movendo_guia_fgts(caminho_destino):

    caminho_origem = 'W:\\Publico\\LabKom\\robo_temp'

    for file in os.listdir(caminho_origem):
        origem = os.path.join(caminho_origem, file)
        shutil.move(origem, caminho_destino)
