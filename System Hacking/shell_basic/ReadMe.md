#shell_basic 풀이법

---

flag를 출력하는 쉘 코드를 작성해야 한다.
그러나 execuve 시스템 콜을 사용할수 없어서, orw(Open-Read_Write) 쉘코드를 작성해야 한다.
pwntools에 쉘 코드를 작성해주는 함수인 shellcraft()가 있습니다.

shellcraft.py 익스플로잇 코드를 작성한 후
python3 shellcraft.py 로 실행하면 Flag를 흭득할 수 있다.

---

<참고 문헌> https://docs.pwntools.com/en/stable/shellcraft/amd64.html
