#csrf-1 풀이법

---

| URL                | Description                      | Restrictions                                         |
| ------------------ | -------------------------------- | ---------------------------------------------------- |
| /                  | Index page of the website        | None                                                 |
| /vuln              | Displays user input, filters XSS | None                                                 |
| /memo              | Allows users to write memos      | None                                                 |
| /admin/notice_flag | Adds FLAG to a memo (localhost)  | Restricted to localhost and site administrators only |
| /flag              | Accessible to any user           | None                                                 |

admin/notice_flag에는 localhost의 접근을 제한하는 코드가 있어서 우회하는 전략을 사용한다. <br>

**&lt;img src="https:/admin/notice_flag?userid=admin"> 를 /flag에서 입력하여 Flag를 흭득한다.**

---

CSRF는 이용자가 임의 페이지에 HTTP 요청을 보내는 것을 목적으로 하는 공격입니다. <br>
또한, 공격자는 악성 스크립트가 포함된 페이지에 접근한 이용자의 권한으로 웹 서비스의 임의 기능을 실행할 수 있습니다.
