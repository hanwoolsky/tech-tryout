import pyautogui # powershell에서 python .\file.py 형태로 입력해야 실행된다.

# 1. 현재 마우스의 좌표와 모니터의 크기 출력
print(pyautogui.position()) # Point(x=2438, y=80)
print(pyautogui.size()) # Size(width=1920, height=1080)

# 2. (x, y)로 이동 후 마우스 클릭
pyautogui.moveTo(710, 18)
pyautogui.click()

# 3. (x, y) 클릭
pyautogui.click(710, 18)

# 4.(x, y)에서 마우스 왼쪽 / 오른쪽 / 중간 클릭
pyautogui.click(200, 200, button='right') # left, right, middle

# 5. (x, y)에서 0.5초 간격으로 2번 클릭
pyautogui.click(200, 200, clicks=2, interval=0.5)

# 6. 현재 위치에서 (0, 10)만큼 이동한 후 double click
pyautogui.moveRel(0, 10)
pyautogui.doubleClick()

# 7. 현재 커서의 위치에서 (x, y)의 위치로 마우스 왼쪽 / 오른쪽 / 중간을 클릭한 채로 드래그
pyautogui.dragTo(300, 300, button='left') # 
pyautogui.dragTo(400, 400, 2, button='left') # 2초동안 드래그
pyautogui.dragRel(30, 0, 2, button='right') # 현재 위치에서 x = 30, y = 0만큼 2초 동안 드래그