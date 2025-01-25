import pyautogui

# 1. (x, y) 위치를 클릭한 후 0.1초마다 한 글자씩 Hello world 타이핑
pyautogui.click(500, 500)
pyautogui.typewrite('Hello world!', interval=0.1)

# 2. 리스트 형태로 입력하여도 한 글자씩 abc 타이핑 (띄어쓰기 없음)
pyautogui.click(500, 500)
pyautogui.typewrite(['a', 'b', 'c'], interval=0.1)

# 3. 단축키 (ctrl+c, ctrl+v)
pyautogui.hotkey('ctrl', 'c')  # ctrl-c to copy
pyautogui.hotkey('ctrl', 'v')  # ctrl-v to paste

# 4. c키를 누르고 c키 떼기
pyautogui.keyDown('c')
pyautogui.keyUp('c')

# 5. c키를 누르고 c키 떼기
pyautogui.press('c')

# 6. PyAutoGUI 모듈의 모든 키 리스트
print(pyautogui.KEYBOARD_KEYS)
# ['\t', '\n', '\r', ' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~', 'accept', 'add', 'alt', 'altleft', 'altright', 'apps', 'backspace', 'browserback', 'browserfavorites', 'browserforward', 'browserhome', 'browserrefresh', 'browsersearch', 'browserstop', 'capslock', 'clear', 'convert', 'ctrl', 'ctrlleft', 'ctrlright', 'decimal', 'del', 'delete', 'divide', 'down', 'end', 'enter', 'esc', 'escape', 'execute', 'f1', 'f10', 'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f2', 'f20', 'f21', 'f22', 'f23', 'f24', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'final', 'fn', 'hanguel', 'hangul', 'hanja', 'help', 'home', 'insert', 'junja', 'kana', 'kanji', 'launchapp1', 'launchapp2', 'launchmail', 'launchmediaselect', 'left', 'modechange', 'multiply', 'nexttrack', 'nonconvert', 'num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6', 'num7', 'num8', 'num9', 'numlock', 'pagedown', 'pageup', 'pause', 'pgdn', 'pgup', 'playpause', 'prevtrack', 'print', 'printscreen', 'prntscrn', 'prtsc', 'prtscr', 'return', 'right', 'scrolllock', 'select', 'separator', 'shift', 'shiftleft', 'shiftright', 'sleep', 'space', 'stop', 'subtract', 'tab', 'up', 'volumedown', 'volumemute', 'volumeup', 'win', 'winleft', 'winright', 'yen', 'command', 'option', 'optionleft', 'optionright']

# 단축키 window + r을 누르는 두 가지 방법
# O
pyautogui.hotkey('winleft', 'r')

# O
pyautogui.keyDown('winleft')
pyautogui.keyDown('r')
pyautogui.keyUp('winleft') # keyUp 안 하면 실행 후 window가 계속 눌린 상태로 있어서 정상 동작을 못한다.
pyautogui.keyDown('r')

# X
pyautogui.press('winleft')
pyautogui.press('r') # winleft를 눌렀다가 [뗀 다음에] r을 누르기 때문에 검색이 된다.