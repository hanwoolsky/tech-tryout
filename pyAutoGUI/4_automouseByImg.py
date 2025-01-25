# 화면 상의 특정 영역의 이미지 파일을 갖고 있으면
# 1. 이미지 영역 찾기
# 2. 이미지 영역의 가운데 위치 얻기
# 3. 클릭하기
# 의 순서를 통해 항상 똑같은 버튼을 클릭할 수 있다.
# 1920×1080 화면 기준으로, 클릭에 1~2초 정도 소요

import pyautogui

# 1. 이미지 영역 찾기
nine_btn = pyautogui.locateOnScreen('calc_nine.png')
print(nine_btn) # 왼쪽 위의 위치와 영역의 가로, 세로 크기를 튜플의 형태 (left, top, width, height)로 출력
# 없으면 None 출력

# 2. 이미지 영역의 가운데 위치 얻고 클릭하기
nine_btn = pyautogui.locateOnScreen('calc_nine.png')
center = pyautogui.center(nine_btn)
print(center)

# 3. 이미지 영역의 가운데를 한번에 찾아 클릭하기
center = pyautogui.locateCenterOnScreen('calc_nine.png')
pyautogui.click(center)

# 계산기에서 루트 9 계산하기
center = pyautogui.locateCenterOnScreen('calc_nine.png')
pyautogui.click(center)
center = pyautogui.locateCenterOnScreen('calc_root.png')
pyautogui.click(center)
center = pyautogui.locateCenterOnScreen('calc_equal.png')
pyautogui.click(center)