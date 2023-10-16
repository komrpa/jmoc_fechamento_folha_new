from selenium.webdriver.support import expected_conditions as condicao_esperada
from selenium.webdriver.common.by import By
from time import sleep


def tabela_nao_esta_vazia(wait):
    try:
        tabela = wait.until(condicao_esperada.presence_of_element_located(
            (By.XPATH, '//table//tbody//tr')))
        return True
    except:
        return False
      # tabela[0].click()

    #   {len(tabela)}


def qtde_elementos_tabela(wait):
    tabela = wait.until(condicao_esperada.presence_of_all_elements_located(
        (By.XPATH, '//table//tbody//tr')))
    return len(tabela)


def aguardando_carga_elements(wait):
    while (True):
    
        try:
            wait.until(condicao_esperada.presence_of_element_located(
                (By.XPATH, '//div[@class="panel-progress-bar-header"]')))
        
        except:

            break


def carregar_arquivos_para_tabela(wait, files):

    element = wait.until(condicao_esperada.presence_of_all_elements_located(
        (By.XPATH, '//input[@ng-if="vm.isObligationsEnabled"]')))

    element[0].send_keys(files)

# def carregar_arquivos_para_tabela(wait, path_declaracao, path_recibo):

#     element = wait.until(condicao_esperada.presence_of_all_elements_located(
#         (By.XPATH, '//input[@type="file"]')))

#     element[0].send_keys(f'{path_declaracao} \n {path_recibo}')

# //span[@class="fa text-small ng-scope fa-circle text-success"]


def habilitar_elementos_tabela_envio(wait):

    try:
        checkbox = wait.until(condicao_esperada.presence_of_all_elements_located(
            (By.XPATH, '//span[@ng-if="file.comments.length"]')))
        sleep(2)
        checkbox[0].click()
        sleep(2)
        opcao_correcao = wait.until(condicao_esperada.presence_of_all_elements_located(
            (By.XPATH, '//span[@class="far clickable fa-circle text-brand"]')))
        sleep(2)
        opcao_correcao[0].click()
        sleep(2)
        checkbox[1].click()
        sleep(2)
        opcao_correcao = wait.until(condicao_esperada.presence_of_all_elements_located(
            (By.XPATH, '//span[@class="far clickable fa-circle text-brand"]')))
        sleep(2)
        opcao_correcao[0].click()

    except:
        pass


def confirmar_desvinculao_regra(wait):
    try:
        agora_nao = wait.until(condicao_esperada.presence_of_all_elements_located(
            (By.XPATH, '//button[@class="btn btn-link text-washed"]')))

        agora_nao[0].click()

        print('clicou no agora nao')

    except:
        pass


#

def selecionar_todos_elementos_tabela(wait):

    selecionar_todos = wait.until(condicao_esperada.presence_of_all_elements_located(
        (By.XPATH, '//label[@class="far mr-1 fa-square"]')))

    selecionar_todos[0].click()


def excluir_todos_elementos_tabela(wait):

    excluir_todos = wait.until(condicao_esperada.presence_of_all_elements_located(
        (By.XPATH, '//div[@class="col-xs-12"]//a[@class="clickable"]')))
    excluir_todos[0].click()

    botao_confirmar_exclusao = wait.until(condicao_esperada.presence_of_all_elements_located(
        (By.XPATH, '//button[@class="btn btn-primary ng-binding"]')))
    botao_confirmar_exclusao[0].click()


# //div[@class="panel-progress-bar-header"]


def protocolar_declaracoes(wait, driver):
    protocolar_todos = wait.until(condicao_esperada.presence_of_all_elements_located(
        (By.XPATH, '//div[@class="row pl-1 pr-1"]//a')))

    print(f'protocolo_todos => {protocolar_todos}')

    protocolar_todos[0].click()

    print('finalizari o protocolo')

# def protocolar_declaracoes(wait, driver):
#     protocolar_todos = wait.until(condicao_esperada.presence_of_all_elements_located(
#         (By.XPATH, "//a[text()='Protocolar']")))

#     driver.execute_script('arguments[0].click()', protocolar_todos[0])
