import pyautogui, pyscreeze
'''
#mover
pyautogui.moveTo(1112, 1052, duration=.5)
pyautogui.moveRel(100,0, duration=.5)
pyautogui.moveRel(0,-100,duration=.5)


#arrastar
pyautogui.moveTo(257,128, duration=.5)
pyautogui.dragTo(27, 19, duration=.5)


#clicar
pyautogui.click(57,17, duration=.5, clicks=2)
'''

#Localizar um item na tela
btnXY = pyautogui.locateCenterOnScreen('./aula7/btn_edit.png')
pyautogui.click(btnXY, duration=.5)