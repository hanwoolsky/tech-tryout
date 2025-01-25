# Selenium

## How To Run?
```
STEP 1. apt-get update
$ sudo apt-get update
$ sudo apt-get install -y curl unzip xvfb libxi6 libgconf-2-4

STEP 2. Install Chrome
$ wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
$ sudo apt install ./google-chrome-stable_current_amd64.deb

$ google-chrome --version
Google Chrome <version>

STEP 3. Install Chrome Driver
$ wget https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/<version>/linux64/chromedriver-linux64.zip
chromedriver_linux64.zip 압축 해제 후 chromedriver만 selenium/ 으로 옮기기

$ sudo mv chromedriver /usr/bin/chromedriver
$ sudo chown root:root /usr/bin/chromedriver
$ sudo chmod +x /usr/bin/chromedriver

$ chromedriver --version
ChromeDriver <version>

STEP 4. Install X Server
https://sourceforge.net/projects/vcxsrv/
C:\Program Files\VcXsrv 에서 xlaunch.exe 실행
Default + Disable access control 체크

$ echo $SHELL
/usr/bin/zsh
$ vi ~/.zshrc
export DISPLAY=$(cat /etc/resolv.conf | grep nameserver | awk '{print $2; exit;}'):0.0

$ source ~/.zshrc
$ echo $DISPLAY
172.17.64.1:0.0

STEP 5. RUN
$ google-chrome
```
