import os
from robo_sefip.conexao_sefip import *
from waiting_sefip.waiting_sefip_ import *
from time import sleep
from log_.gravar_log import registrar_logs_execucao
from digitar_texto.digitar_textos import digitar_textos
import pdfplumber
from converter_valores.converte_value import converter_flutuante_string, converter_string_flutuante
from config_email.criacao_email import send_email_adm_anexo
from log_.gravar_log import registrar_logs_execucao
import webbrowser
import pyautogui
from image_certificados.identificar_imagem_certificado import identificar_imagem_referente_certificado
from read_files.leitura_arquivos import limpar_pasta_sefip_c, encontrar_sefip_importar_conectividade
from digitar_texto.digitar_textos import digitar_textos
from log_.gravar_log import registrar_logs_execucao
from config_email.criacao_email import send_email_adm_anexo
import webbrowser
from time import sleep
from wait_actions.waiting import *
from log_.gravar_log import registrar_logs_execucao
import os
from wait_actions.waiting import *
from executar_java.executar_java_ import executar_exe_java
from conexao import iniciar_driver
from logar_sistema import efetuar_login_nibo
from time import sleep
from gerenciar_tabela_nibo import *
import shutil
from pastas_rede.manipular_pastas_rede import *


class Process:

    def __init__(self, cod_cliente, cnpj, razao_social, grupo, contador, competencia, configuracao, check, status, obs):

        self.cod_cliente = cod_cliente
        self.cnpj = cnpj
        self.razao_social = razao_social
        self.grupo = grupo
        self.contador = contador
        self.configuracao = configuracao
        self.competencia = competencia.replace('/', '')
        self.data = competencia
        self.check = check
        self.status = status
        self.obs = obs
        self.name_folder = f"{razao_social}-{cod_cliente}"
        self.dict_steps = {}
        self.path_default = os.path.join(os.getcwd(),
                                         'processos', self.name_folder, self.competencia)

    # criar pasta com os passos se não existir

    def create_paths_interno(self):

        for step in range(1, 9):
            step = f'step_{str(step)}'
            if not os.path.exists(os.path.join(self.path_default, step)):

                os.makedirs(os.path.join(
                    self.path_default, step))

    def add_steps(self, name, numero, step):
        self.dict_steps.update({numero: step(name, numero, self.path_default)})

    def criar_caminho_pasta_cliente(self):

        # formato data '01072023'

        caminho_padrao = 'W:\\Pessoal\\Clientes'

        if self.grupo == '---':
            pass
        else:
            caminho_padrao = f"{caminho_padrao}\\GRUPO {self.grupo}"
        print(caminho_padrao)

        nova_data = self.data.split('/')
        ano = nova_data[-1]
        mes = nova_data[0]
        pasta_mes_ano = calcular_mes(mes, ano)
        nome_cliente = ''
        lista_clientes = os.listdir(caminho_padrao)

        # verificar se já existe a pasta do cliente
        for cliente in lista_clientes:
            try:
                if cliente.split('-')[-1].strip() == str(self.cod_cliente):
                    nome_cliente = cliente
                    break
            except:
                pass

        # se exister não fazer nada
        if nome_cliente:
            pass
        # se não existir, criar a pasta do cliente e o caminho de conferencias
        else:
            # avisar o adm que foi criada uma nova pasta do cliente
            send_email_adm_anexo(
                f"sera criada uma nova pasta para o cliente {self.razao_social} pois não existia")

            nome_cliente = f"{self.razao_social} - {self.cod_cliente}"

        try:

            if not existe_essa_pasta(f'{caminho_padrao}\\{nome_cliente}\\FOLHA DE PAGAMENTO\\{ano}\\{pasta_mes_ano}\\DCTFWEB'):

                criar_nova_pasta(
                    f'{caminho_padrao}\\{nome_cliente}\\FOLHA DE PAGAMENTO\\{ano}\\{pasta_mes_ano}\\DCTFWEB')

            if not existe_essa_pasta(f'{caminho_padrao}\\{nome_cliente}\\FOLHA DE PAGAMENTO\\{ano}\\{pasta_mes_ano}\\SEFIP'):

                criar_nova_pasta(
                    f'{caminho_padrao}\\{nome_cliente}\\FOLHA DE PAGAMENTO\\{ano}\\{pasta_mes_ano}\\SEFIP')

            return f'{caminho_padrao}\\{nome_cliente}\\FOLHA DE PAGAMENTO\\{ano}\\{pasta_mes_ano}'

        except Exception as e:

            raise Exception(f'Ocorreu um erro ao criar caminho pastas {e}')


class Step:

    def __init__(self, name, numero, path_default):

        self.name = name
        self.numero = numero
        self.path_default = path_default

    def copy_files_intern(self, pasta_origem, pasta_destino, file):

        origem = os.path.join(self.path_default, pasta_origem, file)
        destino = os.path.join(self.path_default, pasta_destino, file)

        shutil.copy(src=origem, dst=destino)

    def rename_file(self, old_name, new_name, path):

        try:
            old = os.path.join(path, old_name)
            new = os.path.join(path, new_name)

            if old != new:
                os.rename(old, new)
        except Exception as e:
            print(f'erro {e}')


class Step1(Step):

    def mover_arquivos_gerados_questor(self, configuracao, competencia, cod_cliente):
        # competencia 072023
        # caminho_padrao_origem = f'W:\\Pessoal\\Fechamento de folha automatizado\\Automação Folha\\Configuração 0003 - Teste Folha Automatizada\\{competencia}'
        caminho_padrao_origem = PathFiles().found_folder_config(
            config=configuracao, competencia=competencia)

        try:
            registrar_logs_execucao(f'{os.listdir(caminho_padrao_origem)}')
            for empresa in os.listdir(caminho_padrao_origem):
                registrar_logs_execucao(
                    f"{int(empresa.split('-')[0].split()[1])}, {int(cod_cliente)}")
                if int(cod_cliente) == int(empresa.split('-')[0].split()[1]):
                    origem = f'{caminho_padrao_origem}\\{empresa}\\'
                    registrar_logs_execucao(origem)
                    for arquivo in os.listdir(origem):
                        caminho_origem = os.path.join(origem+os.sep+arquivo)
                        registrar_logs_execucao(
                            f'movendo---->{caminho_origem}')
                        shutil.move(caminho_origem, os.path.join(
                            self.path_default, 'step_1'))

                    # os.rmdir(origem)
        except Exception as e:
            raise Exception(f'nao conseguiu finaliza copia dos arquivos {e}')

    # gerar folha no questor
    # copiar arquivos da pasta origem dos arquivos gerados
    # W:\Pessoal\Fechamento de folha automatizado\Automação Folha\Configuração 0006 - FOLHA AUTOMATIZADA - JM\102023\Empresa 1104 - ARS CENTRO NOVO OTICA LTDA

    # para o step1


# Gerar 4 relatórios SEFIP
# gerar Arquivo.SP
class Step2(Step):

    # Importar SEFIP.RE (oriundo do step1)
    def import_sefip_re(self):

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

        path_file_sefip_RE = os.path.join(
            self.path_default, self.numero, 'SEFIP.RE')
        # digitar caminho onde esta salvo arquivo da sefip
        # path_default = f'{path_file_sefip_RE}\\SEFIP.RE'
        digitar_textos(path_file_sefip_RE)
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

    def atualizar_fap(self):

        # COLOCAR O FAP
        coordenada_empresa = pyautogui.locateOnScreen(
            image=f'imagens_sefip/selecionar_empresa.png',
            grayscale=True,
            confidence=0.9
        )

        pyautogui.click(coordenada_empresa, duration=2)

        sleep(2)

        dados_movimento_button = pyautogui.locateOnScreen(
            image=f'imagens_sefip/dados_do_movimento.png',
            grayscale=True,
            confidence=0.9
        )

        pyautogui.click(dados_movimento_button, duration=2)

        sleep(2)

        # clicar campo fap
        pyautogui.doubleClick(614, 224)

        sleep(2)

        with open(os.path.join(self.path_default, self.numero, 'fap.txt')) as file:
            vlr_fap = file.read().replace('\n', '')

        sleep(2)

        pyautogui.write(vlr_fap)

        button_salvar = pyautogui.locateOnScreen(
            image=f'imagens_sefip/salvar_info_fap.png',
            grayscale=True,
            confidence=0.9
        )

        sleep(2)

        pyautogui.click(button_salvar, duration=2)

        # confirmacao_dados
        button_salvar = pyautogui.locateOnScreen(
            image=f'imagens_sefip/confirmacao_dados.png',
            grayscale=True,
            confidence=0.9
        )

        sleep(1)

        pyautogui.press('enter')

    def gerar_arquivo_SFP(self):
        # voltar tela execução (calculadora)
        # confirmacao_dados
        button_calculadora = pyautogui.locateOnScreen(
            image=f'imagens_sefip/calculadora.png',
            grayscale=True,
            confidence=0.9
        )

        sleep(2)

        pyautogui.click(button_calculadora, duration=2)

        waiting_executar_sefip()
        sleep(5)

        while (True):
            # procura tela informacao (I)
            coordenada_imagem_2 = pyautogui.locateOnScreen(
                image=f'imagens_sefip/informacao_i.png',
                grayscale=True,
                confidence=0.9
            )

            if coordenada_imagem_2:
                # clica no enter -> OK (confirmar leitura informaçao)
                pyautogui.press('enter')
                break

        sleep(5)

        # GRAVACAO SEFIP
        while (True):
            # PROCURA TELA GRAVACAO SEIFP
            coordenada_imagem_3 = pyautogui.locateOnScreen(
                image=f'imagens_sefip/sefip_tela_geracao_arquivo_saida.png',
                grayscale=True,
                confidence=0.9
            )

            # salvar arquivo sefip
            if coordenada_imagem_3:
                pyautogui.press('enter')
                break

        sleep(5)
        # clicar OK confirmar informacao
        pyautogui.press('enter')
        sleep(5)
        # clicar OK confirmar informacao
        pyautogui.press('enter')
        sleep(5)
        # clicar OK confirmar informacao
        pyautogui.press('enter')
        sleep(5)

        # C:\Program Files (x86)\CAIXA\SEFIP   -> .SFP

    def gerar_4_relatorios(self):
        # GERAÇÃO DOS RELATÓRIOS
        # ANALÍTICO GRF (1)
        pyautogui.hotkey('N')

        # reconhecer relatório analítico GRF
        while (True):
            # procura imagem relatório analítico GRF
            coordenada_imagem_3 = pyautogui.locateOnScreen(
                image=f'imagens_sefip/relatorios/analitico_GRF.png',
                grayscale=True,
                confidence=0.9
            )

            # salvar arquivo sefip
            if coordenada_imagem_3:
                # imprimir pdf
                pyautogui.hotkey('p')
                sleep(5)
                # salvar
                pyautogui.press('enter')
                sleep(5)
                # confirmar
                pyautogui.press('enter')
                sleep(5)
                # fechar janela
                pyautogui.hotkey('f')
                break

        sleep(5)
        # GERAÇÃO DOS RELATÓRIOS
        # relatório RE
        pyautogui.hotkey('R')
        # reconhecer relatório RE - Relação de Trabalhadores
        while (True):
            # procura imagem RE - Relação de Trabalhadores
            coordenada_imagem_3 = pyautogui.locateOnScreen(
                image=f'imagens_sefip/relatorios/relatorio_re.png',
                grayscale=True,
                confidence=0.9
            )

            # salvar arquivo sefip
            if coordenada_imagem_3:
                # imprimir pdf
                pyautogui.hotkey('g')
                sleep(5)
                # salvar
                pyautogui.press('enter')
                sleep(5)
                # confirmar
                pyautogui.press('enter')
                sleep(5)
                # fechar janela
                pyautogui.hotkey('f')
                break

        sleep(5)
        # GERAÇÃO DOS RELATÓRIOS
        # Comprovante de declarçaão a previdencia
        pyautogui.hotkey('M')
        # reconhecer Comprovante de declarçaão a previdencia
        while (True):
            # procura comprv declaração previdencia
            coordenada_imagem_3 = pyautogui.locateOnScreen(
                image=f'imagens_sefip/relatorios/comprov_declara_previdencia.png',
                grayscale=True,
                confidence=0.9
            )

            # salvar arquivo sefip
            if coordenada_imagem_3:
                # imprimir pdf
                pyautogui.hotkey('g')
                sleep(5)
                # salvar
                pyautogui.press('enter')
                sleep(5)
                # confirmar
                pyautogui.press('enter')
                sleep(5)
                # fechar janela
                pyautogui.hotkey('f')
                break

        sleep(5)
        # GERAÇÃO DOS RELATÓRIOS
        # analitico GPS
        pyautogui.hotkey('A')
        # reconhecer analitico GPS|
        while (True):
            # procura analitico GPS|
            coordenada_imagem_3 = pyautogui.locateOnScreen(
                image=f'imagens_sefip/relatorios/analitico_GPS.png',
                grayscale=True,
                confidence=0.9
            )

            # salvar arquivo sefip
            if coordenada_imagem_3:
                # imprimir pdf
                pyautogui.hotkey('g')
                sleep(5)
                # salvar
                pyautogui.press('enter')
                sleep(5)
                # confirmar
                pyautogui.press('enter')
                sleep(5)
                # fechar janela
                pyautogui.hotkey('f')
                break

        sleep(5)
        pyautogui.hotkey('alt', 'f4')
        sleep(5)
        registrar_logs_execucao('Processo finalizado com sucesso!!!')


class Step3(Step):

    def comparar_relatorios_sefip_questor_valor_FGTS(self):

        guia_sefip = 0
        valor_relacao_calculo_sefip = 0
        valor_recolhimento_sefip = 0
        path_default = os.path.join(self.path_default, self.numero)

        try:

            for arquivo in os.listdir(path_default):

                if arquivo.split('.')[-1].upper() == 'PDF':

                    lista_pdfs = pdfplumber.open(
                        os.path.join(path_default, arquivo))

                    pdf_full = lista_pdfs.pages

                    for pdf in pdf_full:

                        lista_texto = pdf.extract_text().split('\n')
                        # print(lista_texto)

                        if 'RELATÓRIO ANALÍTICO DA GRF' in ' '.join(lista_texto):

                            for pdf in pdf_full:

                                lista_texto = pdf.extract_text().split('\n')

                                for texto in lista_texto:

                                    if 'RECOLHER' in texto:

                                        guia_sefip = converter_string_flutuante(
                                            texto.split()[-1])

                        if 'Relação de Cálculo - Período:' in ' '.join(lista_texto) and '13o Salário Adiantamento' not in ' '.join(lista_texto):

                            for pdf in pdf_full:

                                lista_texto = pdf.extract_text().split('\n')

                                for texto in lista_texto:

                                    if 'Total Recolhido em Sefip' in texto:
                                        valor_relacao_calculo_sefip = converter_string_flutuante(
                                            texto.split()[-1])

                        if '13o Salário Adiantamento' in ' '.join(lista_texto):

                            for pdf in pdf_full:

                                lista_texto = pdf.extract_text().split('\n')

                                for texto in lista_texto:

                                    if 'Total Recolhido em Sefip' in texto:
                                        valor_relacao_calculo_sefip_13 = converter_string_flutuante(
                                            texto.split()[-1])
                                        # print(valor_relacao_calculo_sefip_13)

                        if 'Resumo de Recolhimento de FGTS por Contrato do Empregado' in ' '.join(lista_texto):

                            for pdf in pdf_full:
                                lista_texto = pdf.extract_text().split('\n')

                                for texto in lista_texto:

                                    if 'Total Geral' in texto:

                                        valor_recolhimento_sefip = converter_string_flutuante(texto.split()[
                                            3]) + converter_string_flutuante(texto.split()[
                                                6])
                                        # valor_recolhimento_sefip_pdf = converter_flutuante_string(
                                        #     valor_recolhimento_sefip)

            print(f'RELATORIO ANALITICO GRF {guia_sefip}')
            print(
                f'RELAÇÃO DE CALCULO {valor_relacao_calculo_sefip + valor_relacao_calculo_sefip_13}')
            print(f'RESUMO DE RECOLHIMENTO {valor_recolhimento_sefip}')
            if (guia_sefip - (valor_relacao_calculo_sefip + valor_relacao_calculo_sefip_13) - valor_recolhimento_sefip) > 1:
                print('diferenca acima de 1 real, temos problemas')
            elif (guia_sefip - (valor_relacao_calculo_sefip + valor_relacao_calculo_sefip_13) - valor_recolhimento_sefip) > 1:
                print('diferenca acima de 1 real, temos problemas')
            else:
                registrar_logs_execucao(
                    f'guia sefip R$ {guia_sefip} | valor recolhimento sefip R$ {valor_recolhimento_sefip} valor relação de cálculo sefip R$ {valor_relacao_calculo_sefip + valor_relacao_calculo_sefip_13}')
                print(
                    f'guia sefip R$ {guia_sefip} | valor recolhimento sefip R$ {valor_recolhimento_sefip} valor relação de cálculo sefip R$ {valor_relacao_calculo_sefip + valor_relacao_calculo_sefip_13}')
                send_email_adm_anexo(
                    f'guia sefip R$ {guia_sefip} | valor recolhimento sefip R$ {valor_recolhimento_sefip} | valor relação de cálculo sefip R$ {valor_relacao_calculo_sefip + valor_relacao_calculo_sefip_13}')
                registrar_logs_execucao(
                    'valores de sefip batendo, segue o baile!!!')
                print(
                    'valores de sefip batendo, segue o baile!!!')

        except Exception as e:
            erro = 'Erro na comparação dos PDFs FGTS'
            registrar_logs_execucao(f'{erro} => {e}')
            send_email_adm_anexo(f'{erro} => {e}')
            raise Exception(f'{erro} => {e}')


class Step4(Step):

    def conectividade_sefip(self, certificado):

        try:

            sleep(5)

            webbrowser.open(
                'https://conectividadesocialv2.caixa.gov.br/sicns/')

            # CAIXA POSTAL -> CONECTIVIDADE
            while (True):

                coordenada_caixa_postal = pyautogui.locateOnScreen(
                    image=f'imagens_conectividade/caixa_postal.png',
                    grayscale=True,
                    confidence=0.9
                )

                if coordenada_caixa_postal:
                    pyautogui.click(coordenada_caixa_postal, duration=2)
                    break

            # SELECT CERTIFICADO
            imagem1, imagem2 = identificar_imagem_referente_certificado(
                certificado)

            scrolada = -10
            x = 1206
            y = 173

            tempo = 1
            sleep(10)

            while (True):

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
                    pyautogui.click(coordenadas_certificado_1, duration=2)
                    break
                elif coordenadas_certificado_2:
                    pyautogui.click(coordenadas_certificado_2, duration=2)
                    break
                elif imagem1 or imagem2:

                    pyautogui.click(x, y, duration=1)
                    pyautogui.scroll(scrolada)
                    y += 10

            # CLICAR EM OK, DEPOIS DO CERTIFICADO SELECIONADO
            while (True):

                coordenada_botao_ok = pyautogui.locateOnScreen(
                    image=f'imagens_conectividade/confirmar_selecao_certificado.png',
                    grayscale=True,
                    confidence=0.9
                )

                if coordenada_botao_ok:
                    pyautogui.click(coordenada_botao_ok, duration=2)
                    break

            # CLICAR EM NOVA MENSAGEM
            while (True):

                coordenada_nova_mensagem = pyautogui.locateOnScreen(
                    image=f'imagens_conectividade/nova_mensagem.png',
                    grayscale=True,
                    confidence=0.9
                )

                if coordenada_nova_mensagem:
                    pyautogui.click(coordenada_nova_mensagem, duration=2)
                    break

            # CLICAR EM SELECIONAR SERVIÇO
            while (True):

                coordenada_selecionar_servico = pyautogui.locateOnScreen(
                    image=f'imagens_conectividade/selecionar_servico.png',
                    grayscale=True,
                    confidence=0.9
                )

                if coordenada_selecionar_servico:
                    pyautogui.click(coordenada_selecionar_servico, duration=2)
                    break

            # CLICAR EM SELECIONAR ENVIO ARQUIVO SEFIP
            while (True):

                coordenada_selecionar_servico = pyautogui.locateOnScreen(
                    image=f'imagens_conectividade/selecionar_envio_arquivo_sefip.png',
                    grayscale=True,
                    confidence=0.9
                )

                if coordenada_selecionar_servico:
                    pyautogui.click(coordenada_selecionar_servico, duration=2)
                    break

            # CLICAR EM NOME DA MENSAGEM
            while (True):

                coordenada_nome_mensagem = pyautogui.locateOnScreen(
                    image=f'imagens_conectividade/nome_da_mensagem.png',
                    grayscale=True,
                    confidence=0.9
                )

                if coordenada_nome_mensagem:
                    pyautogui.click(coordenada_nome_mensagem, duration=2)
                    break

            sleep(1)
            # escrever nome mensagem
            pyautogui.write('SEFIP')

            # SELECIONAR O ESTADO
            while (True):

                coordenada_selecao_estado = pyautogui.locateOnScreen(
                    image=f'imagens_conectividade/selecionar_estado.png',
                    grayscale=True,
                    confidence=0.9
                )

                if coordenada_selecao_estado:
                    pyautogui.click(coordenada_selecao_estado)
                    sleep(1)
                    pyautogui.write('santa')
                    sleep(1)
                    pyautogui.press('enter')
                    break

            # SELECIONAR A BASE DE ARRECADAÇÃO
            while (True):

                coordenada_selecao_estado = pyautogui.locateOnScreen(
                    image=f'imagens_conectividade/selecionar_base_arrecadacao_floripa.png',
                    grayscale=True,
                    confidence=0.9
                )

                if coordenada_selecao_estado:
                    pyautogui.click(coordenada_selecao_estado)
                    sleep(1)
                    pyautogui.write('floria')
                    sleep(2)
                    pyautogui.press('enter')
                    break

            sleep(1)
            # CLICAR EM ADICIONAR ARQUIVO
            while (True):

                coordenada_adicionar_arquivo = pyautogui.locateOnScreen(
                    image=f'imagens_conectividade/botao_adicionar.png',
                    grayscale=True,
                    confidence=0.9
                )

                if coordenada_adicionar_arquivo:
                    pyautogui.click(coordenada_adicionar_arquivo, duration=1)
                    break

            sleep(1)
            # ESPERAR RECONHECER TELA PARA ABRIR ARQUIVO
            while (True):

                coordenada_adicionar_arquivo = pyautogui.locateOnScreen(
                    image=f'imagens_conectividade/tela_procurar_arquivo.png',
                    grayscale=True,
                    confidence=0.9
                )

                if coordenada_adicionar_arquivo:
                    # pyautogui.click(coordenada_adicionar_arquivo, duration=1)
                    break

            sleep(2)

            # ENCONTRAR O CAMINHO DO ARQUIVO
            file = encontrar_sefip_importar_conectividade(
                'C:\\Users\\kompagrpa\\SEFIP')
            # DIGITAR CAMINHO DO ARQUIVO
            digitar_textos(file)
            # C:\Program Files (x86)\CAIXA\Arquivos
            sleep(2)
            # LIMPAR PASTA
            pyautogui.press('enter')
            sleep(2)
            # limpar_pasta_sefip_c()

            # CLICAR PARA ENVIAR ARQUIVO PELO CONECTIVIDADE
            while (True):

                coordenada_sefip_botao_enviar = pyautogui.locateOnScreen(
                    image=f'imagens_conectividade/botao_enviar_sefip.png',
                    grayscale=True,
                    confidence=0.9
                )

                if coordenada_sefip_botao_enviar:
                    pyautogui.click(coordenada_sefip_botao_enviar, duration=1)
                    break

            sleep(2)

            # # FECHAR ERRO

            # while True:
            #     coordenada_fechar_erro = pyautogui.locateOnScreen(
            #         image=f'imagens_conectividade/fechar_erro.png',
            #         grayscale=True,
            #         confidence=0.9
            #     )

            #     if coordenada_fechar_erro:
            #         pyautogui.click(coordenada_fechar_erro, duration=1)
            #         break

            # CLICAR PARA ENVIAR ARQUIVO CONFIRMAR ASSINATURA ENVIO SEFIP
            while (True):

                coordenada_aceitar_envio = pyautogui.locateOnScreen(
                    image=f'imagens_conectividade/aceitar_envio_sefip.png',
                    grayscale=True,
                    confidence=0.9
                )

                if coordenada_aceitar_envio:
                    pyautogui.click(coordenada_aceitar_envio, duration=1)
                    break

            # CLICAR BAIXAR PROTOCOLO
            while (True):

                coordenada_protocolo_sefip = pyautogui.locateOnScreen(
                    image=f'imagens_conectividade/salvar_protocolo_envio_sefip.png',
                    grayscale=True,
                    confidence=0.9
                )

                if coordenada_protocolo_sefip:
                    pyautogui.click(coordenada_protocolo_sefip, duration=2)
                    break

            sleep(2)
            # CLICAR BAIXAR ARQUIVO PARA SEFIP
            while (True):

                coordenada_baixar_arquivo_sefip = pyautogui.locateOnScreen(
                    image=f'imagens_conectividade/clicar_baixar_arquivo_para_programa_sefip.png',
                    grayscale=True,
                    confidence=0.9
                )

                if coordenada_baixar_arquivo_sefip:
                    print(coordenada_baixar_arquivo_sefip)
                    pyautogui.click(
                        coordenada_baixar_arquivo_sefip, duration=2)
                    break

            sleep(10)

            pyautogui.hotkey('alt', 'f4')

        except Exception as e:
            erro = f'Ocorreu um erro no conectividade {e}'
            registrar_logs_execucao(erro)
            send_email_adm_anexo(erro)
            pyautogui.hotkey('alt', 'f4')
            raise Exception(erro)


class Step5(Step):

    def found_files(self, default_path, extension):
        for file in os.listdir(default_path):
            if file.split('.')[-1].upper() == extension:
                file_found = os.path.join(default_path, file)
        return file_found

    def gerar_guia_fgts_sefip(self, default_path):

        try:

            conectar_sefip()

            sleep(5)

            waiting_tela_inicial_carregar_sefip()

            sleep(5)

            waiting_botao_maximixar_tela_sefip()

            sleep(5)

            waiting_tela_principal_sefip()

            sleep(5)

            pyautogui.hotkey('alt')

            sleep(2)

            pyautogui.hotkey('r')

            sleep(2)

            pyautogui.hotkey('g')

            sleep(2)

            pyautogui.hotkey('i')

            sleep(5)

            botao_abrir = waiting_botao_abrir_arquivo_sefip()

            sleep(5)

            file_found = self.found_files(default_path, 'XML')

            registrar_logs_execucao(f'file_found {file_found}')

            # # found file
            # for file in os.listdir(default_path):
            #     if file.split('.')[-1].upper() == 'XML':
            #         file_found = os.path.join(default_path, file)

            # digitar caminho onde esta salvo arquivo da sefip
            digitar_textos(file_found)

            sleep(5)

            pyautogui.click(botao_abrir, duration=2)

            sleep(5)

            waiting_mensagem_erro_arquivo()

            sleep(5)

            pyautogui.press('enter')

            sleep(5)

            botao_localizar_caminho_arquivo()

            sleep(5)

            botao_abrir = waiting_botao_abrir_arquivo_sefip()

            sleep(5)

            file_found_2 = self.found_files(
                'C:\\Users\\kompagrpa\\SEFIP', 'SFP')

            registrar_logs_execucao(f'file_found_2 {file_found_2}')
            #   # found file
            # for file in os.listdir(default_path):
            #     if file.split('.')[-1].upper() == 'XML':
            #         file_found = os.path.join(default_path, file)

            # digitar caminho onde esta salvo arquivo da sefip
            digitar_textos(file_found_2)

            sleep(5)

            pyautogui.click(botao_abrir, duration=2)

            sleep(5)

            botao_validar_arquivo()

            sleep(5)

            tela_grf_guia()

            sleep(5)

            pyautogui.hotkey('p')

            sleep(5)

            tela_gravacao_guia()

            # salvar a guia
            pyautogui.press('enter')

            sleep(5)

            guia_informacao_finalizado()

            pyautogui.press('enter')

            sleep(5)

            tela_grf_guia()

            sleep(5)

            pyautogui.press('f')

            sleep(1)

            pyautogui.press('esc')
            sleep(1)
            pyautogui.press('esc')
            sleep(1)
            pyautogui.press('esc')

            sleep(5)
            pyautogui.hotkey('alt', 'f4')

        except Exception as e:

            erro = f'Ocorreu um erro na geração da guia fgts pass 5/7  --> {e}'
            registrar_logs_execucao(erro)
            send_email_adm_anexo(erro)
            sleep(5)
            pyautogui.hotkey('alt', 'f4')
            raise Exception(erro)


class Step6(Step):

    def sou_um_humano(self):

        click_i_am_human()

        sleep(3)

        espera_click_prosseguir_human()

        sleep(3)

        clicar_botao_prosseguir()

        sleep(3)

    def sou_procurador(self):

        clicar_filtro_sou_procurador()

        sleep(5)

    def acessar_assinatura_reinf_esocial(self):

        clicar_botao_declaracoes_demonstrativos()

        sleep(3)

        clicar_link_assinar_dctfweb()

        sleep(3)

    def ecac_acesso_web_pagina_fixa(self, certificado):

        webbrowser.open(
            'https://cav.receita.fazenda.gov.br/autenticacao/Login')

        sleep(3)

        clicar_gov_br()

        sleep(3)

        clicar_botao_acessar_certificao()

        sleep(3)

        clicar_selecionar_certificado(certificado)

        sleep(3)

        clicar_botao_ok_certificado_digital()

        sleep(3)

    def converter_string_flutuante(self, valor):

        valor = valor.replace('(', '').replace(')', '')

        if '.' in valor and ',' in valor:
            valor = float(valor.replace('.', '').replace(',', '.'))
        elif ',' in valor:
            valor = float(valor.replace(',', '.'))
        valor = float(valor)
        return round(valor, 2)

    def baixar_relatorios_recibo_declaracao(self):

        botao_relatorios_recibo_declaracao()
        sleep(2)
        botao_download_recibo()
        sleep(2)
        botao_relatorios_recibo_declaracao()
        sleep(2)
        botao_download_declaracao_completa()
        sleep(2)

        with open('W:\\Publico\\LabKom\\robo_temp\\saldo_a_pagar.txt', 'r') as file:
            valor = file.readlines()

        if converter_string_flutuante(valor[0]) == 0:
            pass
        else:
            botao_emitir_darf()
            sleep(2)
            botao_ok_guia()
        sleep(10)

    def gerar_recibos(self):

        clicar_icone_vizualizar_declaracao_enviada()
        sleep(2)
        # baixar relatorios
        self.baixar_relatorios_recibo_declaracao()

        # salvar_pdf_cliente(v, DATA_INICIAL)
        # sleep(2)
        # fechar_mostra_downloads()
        # sleep(2)
        # clicar_botao_voltar_tela_declaracoes()
        # sleep(2)
        # sou_um_humano()
        # seleciona_outorgante_cpf_cnpj()
        # sleep(2)

        # clicar_botao_cancela_selecao_outorgantes()

        # sleep(2)
        # # clicar fora
        # pyautogui.click(383, 802, duration=2)

    def inserir_competencia(self, DATA_INICIAL, DATA_FINAL):

        reconhecer_campo_periodo_apuracao_inicial()

        # clica campo periodo de apuração inicial servidor
        # pyautogui.click(28, 448, duration=1)

        # pyautogui.click(32, 468, duration=2)

        sleep(1)

        # inseri a data inicial
        pyautogui.write(DATA_INICIAL)

        sleep(1)

        reconhecer_campo_periodo_final()

        # # clica no campo de período final servidor
        # pyautogui.click(347, 446, duration=1)

        # pyautogui.click(352, 480, duration=2)

        sleep(1)

        # inseri a data final
        pyautogui.write(DATA_FINAL)

        sleep(3)

    def gerar_esocial_e_guia(self, data_inicial, data_final, CNPJ, path_default, certificado):

        saldo_pagar = 'W:\\Publico\\LabKom\\robo_temp\\saldo_a_pagar.txt'

        try:

            self.ecac_acesso_web_pagina_fixa(certificado)

            self.acessar_assinatura_reinf_esocial()

            self.sou_um_humano()

            self.sou_procurador()

            self.inserir_competencia(data_inicial, data_final)

            seleciona_outorgante()

            # inserir credenciais
            sleep(2)

            pyautogui.write(CNPJ)

            sleep(5)

            reconhecer_cliente()

            sleep(2)

            pesquisar_cliente()

            sleep(2)

            reconhecer_campo_saldo_pagar()

            sleep(2)

            pyautogui.hotkey('win', 'r')

            sleep(2)

            pyautogui.write(f'%windir%\\system32\\notepad.exe')

            sleep(2)

            pyautogui.press('enter')

            sleep(2)

            tela_bloco_de_notas()

            pyautogui.hotkey('ctrl', 'v')

            sleep(2)

            pyautogui.hotkey('ctrl', 's')

            sleep(2)

            botao_salvar_ = botao_salvar()

            pyautogui.write(saldo_pagar)

            sleep(5)

            pyautogui.click(botao_salvar_)

            sleep(2)

            botao_salvar_sobrescrever_sim()

            sleep(3)

            # fechar_janela_bloco()
            pyautogui.hotkey('alt', 'f4')

            sleep(2)

            # if not ha_diferenca_guia_pdfs(saldo_pagar, path_default, CNPJ, data_inicial):
            if True:
                # gerar esocial, etc
                registrar_logs_execucao('pode gerar a guia')

                if botao_transmitir_declaracao_is_visible():

                    botao_transmitir_declaracao()
                    sleep(2)
                    botao_confirmar_transmissao_declaracao()
                    # sleep(2)
                    # transmitir sem vinculacoes
                    # botao_transmitir_sem_vinculacoes()
                    sleep(15)

                    executar_exe_java()
                    sleep(2)
                    botao_executar_java()

                    sleep(5)
                    botao_ok_assinador_doc()
                    # executar o arquivo java nos donwloados

                    botao_ok_final_transmissao()

                    sleep(5)
                if icone_vizualizar_declaracao_enviada():
                    self.gerar_recibos()
            else:
                erro = 'diferença nos valores calculos no questor para os valores do ecac'
                registrar_logs_execucao(erro)
                send_email_adm_anexo(erro)
                raise Exception(erro)

            if os.path.isfile(saldo_pagar):
                os.remove(saldo_pagar)

            sleep(10)

            pyautogui.hotkey('alt', 'f4')

        except Exception as e:
            erro = f'Ocorreu um erro ao gerar o Ecac_Esocial e guia ==> {e}'
            if os.path.isfile(saldo_pagar):
                os.remove(saldo_pagar)
            registrar_logs_execucao(erro)
            send_email_adm_anexo(erro)
            sleep(10)

            pyautogui.hotkey('alt', 'f4')

            raise Exception(erro)


class Step7(Step):
    pass


class Step8(Step):

    # DEIXEI O RELATÓRIO DE FGTS FORA DA POSTAGEM POR ENQUANTO

    def post_files_nibo(path_default):

        for file in ['Relação Cálculo Completa.pdf', 'Relação de Eventos.pdf', 'Relação de Cálculo Resumo.pdf']:
            try:
                if os.path.isfile(f'{path_default}\\{file}'):
                    os.remove(f'{path_default}\\{file}')
            except:
                pass

        files_path = [f'{path_default}\\{file}' for file in os.listdir(
            path_default) if file.split('.')[-1] == 'pdf']
        files_path_recibo = [f'{path_default}\\DCTFWEB\\{file}' for file in os.listdir(
            f'{path_default}\\DCTFWEB') if 'RECIBO' in file.upper()]

        files_full = files_path + files_path_recibo
        files_full = '\n'.join(files_path)

        # arquivos para postar no nibo
        # print(files_full)

        try:
            # POST THE FILES
            # CONECTAR NO NIBO
            driver, wait = iniciar_driver()

            print('*' * 50)

            # LOGAR NO SISTEMA
            efetuar_login_nibo(driver, wait)

            if tabela_nao_esta_vazia(wait):

                # SELECIONAR TODOS
                selecionar_todos_elementos_tabela(wait)
                sleep(5)

                # EXCLUIR TODOS
                excluir_todos_elementos_tabela(wait)
                sleep(5)

            # FAZER UPLOAD DOS ARQUIVOS
            carregar_arquivos_para_tabela(wait, files_full)

            aguardando_carga_elements(wait)

            # CORRIGIR BUG E HABILITAR PARA ENVIO SE TIVER DESABILITADO
            # habilitar_elementos_tabela_envio(wait)
            # sleep(5)

            selecionar_todos_elementos_tabela(wait)
            sleep(5)

            protocolar_declaracoes(wait, driver)
            sleep(5)

            confirmar_desvinculao_regra(wait)

            sleep(5)

            driver.close()

        except Exception as e:

            driver.close()

            print(f'ocorreu um erro {e}')
