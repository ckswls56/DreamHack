#csrf-2 풀이법

---

| URL                | Description                      | Restrictions                                         |
| ------------------ | -------------------------------- | ---------------------------------------------------- |
| /                  | Index page of the website        | None                                                 |
| /vuln              | Displays user input, filters XSS | None                                                 |
| /memo              | Allows users to write memos      | None                                                 |
| /admin/notice_flag | Adds FLAG to a memo (localhost)  | Restricted to localhost and site administrators only |
| /flag              | Accessible to any user           | None                                                 |
| /change_password   | Change user password             | cookie (sessionid)                                   |

Flag를 흭득하기 위하여 admin의 cookie(sessionid)를 흭득하여야 한다. <br>
우선 guest guest로 로그인하여 cookie를 흭득한다.<br>
이후 /flag에 post로 접근하여 session_storage[session_id] = 'admin'가 들어가게 만든다. <br>
이후 cookie를 조작하여 sessionid를 admin으로 수정하고 /change_password?pw='내가원하는비밀번호'로 접근한다.<br>
그러면 users={guest:guest,admin:'내가원하는비밀번호'}로 수정되고 admin으로 로그인하면 된다.<br>

---

CSRF는 이용자가 임의 페이지에 HTTP 요청을 보내는 것을 목적으로 하는 공격입니다. <br>
또한, 공격자는 악성 스크립트가 포함된 페이지에 접근한 이용자의 권한으로 웹 서비스의 임의 기능을 실행할 수 있습니다.
