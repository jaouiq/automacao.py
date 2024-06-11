# importação da biblioteca
import pyautogui as auto

# define espera para cada comando auto
auto.PAUSE = 1

# abre o menu iniciar 
auto.press('win')

# abre o Chrome
auto.write('edge')
auto.press('enter')

# abre o github
auto.write('github.com')
auto.press('enter')

# abre o classroom em uma nova guia
auto.hotkey('ctrl', 't')
auto.write('classroom.google.com')
auto.press('enter')




