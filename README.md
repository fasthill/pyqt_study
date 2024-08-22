# pyqt_study

 * [교육내용 참고 사이트](https://wikidocs.net/70990)

.venv에 환경변수 설정 (아래 그림과 같이, 변수이름과 변수값은 설치된 디렉토리를 찾아서 지정)

 ![image](https://github.com/user-attachments/assets/a87e89eb-57a1-4865-be69-f580a15f5eca)


 * self.event_loop = QEventLoop() 선언 후
 * self.event_loop.exec_() 이 호출될 때마다 신규 이벤트 발생
 * self.event_loop.exit() --> .exec_()가 호출되고 난 후에 .exit()로 이벤트 종료
 * .exec_() 이 발생하지 않으면 .exec()는 의미없이 pass됨.
 * 주의: .exit()미 포함되어 있는 def()이 마지막 명령어까지 수행된 후에 .exec() 이후 명령어가 수행됨.
