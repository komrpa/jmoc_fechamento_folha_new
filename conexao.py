from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service as ChromeService
from time import sleep
from selenium.webdriver.support import expected_conditions as condicao_esperada
import os


# Iniciar o webdriver


def iniciar_driver():
    try:
        chrome_options = Options()

        arguments = ['--lang=en-US', '--window-size=1300,1000',
                     '--incognito']

        for argument in arguments:
            chrome_options.add_argument(argument)

        chrome_options.add_experimental_option('prefs', {
            "download.default_directory": os.getcwd(),
            'download.prompt_for_download': False,
            'profile.default_content_setting_values.notifications': 2,
            'profile.default_content_setting_values.automatic_downloads': 1

        })

        driver = webdriver.Chrome(service=ChromeService(
            ChromeDriverManager().install()), options=chrome_options)

        wait = WebDriverWait(
            driver,
            10,
            poll_frequency=1,
            ignored_exceptions=[
                NoSuchElementException,
                ElementNotVisibleException,
                ElementNotSelectableException,
                UnexpectedAlertPresentException
            ]
        )
    except Exception as e:
        print('*' * 50)
        print(f'erro ao conectar o driver {e}')
        print('*' * 50)

    return driver, wait


if __name__ == '__main__':
    iniciar_driver()
