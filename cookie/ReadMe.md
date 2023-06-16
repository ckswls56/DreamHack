#cookie 풀이법

---

서버 코드를 보면 index 페이지에 접속할 때 username의 cookie를 얻어와 페이지를 반환해주는걸 알 수 있다.
즉 username의 cookie를 조작하는 것이 관건인데 login page에서 pw가 password(form으로 입력한 값)가 같으면 cookie를 설정해서 페이지를 반환한다.
users 에 guset의 비밀번호가 guest임을 알 수 있고 login page에서 id : guest pw : guest로 login 하면
username이라는 cookie가 발급이 된다. 이를 개발자 도구(F12)에서 Application에서 admin으로 조작해주면 Flag를 흭득할 수 있다.

---

Server 코드의 users 배열!!
