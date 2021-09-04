import pyautogui
import time
import keyboard
import cv2


while keyboard.is_pressed('q') == False:
    if pyautogui.locateOnScreen('mic.png', confidence=0.5):
        print('Vendo-1')
        time.sleep(1)
        pyautogui.click('mic.png')
        time.sleep(1)

    if pyautogui.locateOnScreen('cam.png', confidence=0.5):
        print('Vendo-2')
        time.sleep(1)
        pyautogui.click('cam.png')
        time.sleep(1)

    if pyautogui.locateOnScreen('entrar1.png', confidence=0.5):
        print('Vendo-3')
        time.sleep(1)
        pyautogui.click('entrar1.png')

    else:
        print('Nao aparece na tela')
        time.sleep(1)

    if keyboard.is_pressed('q') == True:
        exit()

