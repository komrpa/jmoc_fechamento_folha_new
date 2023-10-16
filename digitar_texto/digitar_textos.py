import pyperclip
import pyautogui
from time import sleep


def digitar_textos(texto):

    pyperclip.copy(texto)
    sleep(1)
    pyautogui.hotkey('ctrl', 'v')
