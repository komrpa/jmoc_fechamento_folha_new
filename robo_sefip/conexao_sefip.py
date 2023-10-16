import pyautogui
from time import sleep


def conectar_sefip():

    sleep(5)

    # pressionar win
    pyautogui.hotkey('win', 'r')

    sleep(2)

    # pesquisar SEFIP
    # pyautogui.write('C:\\Users\\kompagrpa\\SEFIP\\Sefip.exe')
    pyautogui.write("C:\Program Files (x86)\CAIXA\SEFIP\Sefip.exe")

    sleep(2)

    # pressionar enter para entrar na SEFIP
    pyautogui.press('enter')
