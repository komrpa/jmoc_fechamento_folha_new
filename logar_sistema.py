
from selenium.webdriver.support import expected_conditions as condicao_esperada
from selenium.webdriver.common.by import By
from time import sleep


def efetuar_login_nibo(driver, wait):

    driver.get('https://contador.nibo.com.br/Obligation/Pendencies')
    driver.maximize_window()

    # DIGITAR USUARIO
    wait.until(condicao_esperada.element_to_be_clickable(
        (By.XPATH, '//input[@id="emailAddress"]'))).send_keys('diogo.rodrigues@komcorp.com.br')

    # DIGITAR SENHA
    wait.until(condicao_esperada.element_to_be_clickable(
        (By.XPATH, '//input[@id="password"]'))).send_keys('D@241708i')

    # DIGITAR ENTER
    wait.until(condicao_esperada.element_to_be_clickable(
        (By.XPATH, '//input[@type="submit"]'))).click()
