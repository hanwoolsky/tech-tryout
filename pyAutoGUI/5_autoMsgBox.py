import pyautogui

# 1. Alert가 적힌 알림창 띄우기
pyautogui.alert('Alert!')

# 2. Alert 알림창 띄운 후 반환값 출력
alert = pyautogui.alert('Alert!')
print(alert) # OK 문자열 반환

# 3. 확인을 위한 메세지 박스 출력 (Ok / Cancel)
pyautogui.confirm('Shall I proceed?')

# 4. 클릭한 버튼에 따라 Ok / Cancel 출력
confirm = pyautogui.confirm('Shall I proceed?')
print(confirm)

# 5. buttons 리스트를 사용해서 버튼의 개수와 표시될 문자열 설정
a = pyautogui.confirm('Enter option', buttons=['A', 'B', 'C'])

if a == 'A':
    print('You selected A')
elif a == 'B':
    print('You selected B')
else:
    print('You selected C')

# 6. prompt 띄워서 사용자 입력값 받기
name = pyautogui.prompt('What is your name?')
print(name) # OK 누르면 사용자 입력값, Cancel 누르면 None 반환

# 7. 문자열 표시되지 않게 입력값 받기 (비밀번호)
pw = pyautogui.password('Enter password (hidden mode)')
print(pw)

# 8. 안전장치
pyautogui.FAILSAFE = False # 마우스 커서가 화면의 왼쪽 위 모서리(x=0, y=0)로 이동하면, 안전장치가 가동되어 프로그램을 종료하는 안전장치를 사용하고 싶지 않을 때
pyautogui.PAUSE = 2.5 # PAUSE를 설정한 이후 각각의 함수(moveTo, click 등) 뒤에 2.5초의 딜레이를 갖는다. default는 0.1초 (prompt나 password에는 지연이 적용되지 않음)