import pyautogui

# 1. screenshot 찍기
im1 = pyautogui.screenshot() # 스크린샷 이미지 객체 im1 반환
im2 = pyautogui.screenshot('my_screenshot.png') # 전체화면 스크린샷을 my_screenshot.png로 저장
im3 = pyautogui.screenshot('my_region.png', region=(0, 0, 300, 300)) # 주 모니터의 (0, 0) ~ (300, 300) 까지의 영역을 my_region.png로 저장