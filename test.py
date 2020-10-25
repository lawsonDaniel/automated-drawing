import pyautogui

print(pyautogui.position())
pyautogui.moveTo(250,323,duration=5)
pyautogui.click()
pyautogui.dragRel(200,0,duration=2)
pyautogui.moveTo(296,265,duration=2)
pyautogui.click()
pyautogui.dragRel(0,200,duration=2)