| GDB 명령어 | 설명 (영어)                                                                            | 설명 (한국어)                                                               |
| ---------- | -------------------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `b`        | Break. Sets a breakpoint at a specified location.                                      | 중단점 설정. 지정한 위치에 중단점을 설정합니다.                             |
| `c`        | Continue. Continues running the program until a breakpoint or an error.                | 계속. 중단점이나 오류가 발생할 때까지 프로그램을 계속 실행합니다.           |
| `r`        | Run. Starts the execution of the program from the beginning.                           | 실행. 프로그램을 처음부터 실행합니다.                                       |
| `si`       | Step Into. Executes the next line of code, stepping into functions if they are called. | 단계 진입. 다음 코드 라인을 실행하되, 함수가 호출되면 그 안으로 진입합니다. |
| `finish`   | Exit function. Runs until the current function is finished.                            | 함수 종료. 현재 함수가 완료될 때까지 실행합니다.                            |
| `ni`       | Next instruction. Executes the next machine code instruction.                          | 다음 명령어. 다음 기계어 명령어를 실행합니다.                               |
| `i`        | Info. Shows various information about the program's state.                             | 정보. 프로그램 상태에 관한 다양한 정보를 보여줍니다.                        |
| `k`        | Kill. Terminates the running program.                                                  | 종료. 실행 중인 프로그램을 종료합니다.                                      |
| `pd`       | Pdisas. Disassembles the code at a specified location.                                 | 코드 분석. 지정한 위치의 코드를 분석합니다.                                 |

---

x를 이용하면 특정 주소에서 원하는 길이만큼의 데이터를 원하는 형식으로 인코딩하여 볼수 있습니다.

| Option | Category   | Description (English)          | Description (Korean)  |
| ------ | ---------- | ------------------------------ | --------------------- |
| `N`    | Item Count | The number of items to display | 출력할 항목의 개수    |
| `x`    | Format     | Hexadecimal format             | 16진수 형식           |
| `d`    | Format     | Signed decimal format          | 부호 있는 10진수 형식 |
| `u`    | Format     | Unsigned decimal format        | 부호 없는 10진수 형식 |
| `o`    | Format     | Octal format                   | 8진수 형식            |
| `t`    | Format     | Binary format                  | 이진수 형식           |
| `a`    | Format     | Address format                 | 주소 형식             |
| `c`    | Format     | Character format               | 문자 형식             |
| `f`    | Format     | Floating-point format          | 부동 소수점 형식      |
| `i`    | Format     | Machine instruction format     | 기계 명령어 형식      |
| `b`    | Unit       | Byte                           | 바이트                |
| `h`    | Unit       | Halfword (2 bytes)             | Halfword (2바이트)    |
| `w`    | Unit       | Word (4 bytes)                 | Word (4바이트)        |
| `g`    | Unit       | Giant word (8 bytes)           | Giant word (8바이트)  |

---

pwntools API 사용법 ( http://docs.pwntools.com/en/latest/ )

| 함수명              | 설명                                                          |
| ------------------- | ------------------------------------------------------------- |
| process             | 로컬 바이너리를 대상으로 하는 익스플로잇을 위한 함수          |
| remote              | 원격 서버를 대상으로 하는 익스플로잇을 위한 함수              |
| send                | 데이터를 프로세스에 전송하기 위한 함수                        |
| recv                | 프로세스에서 데이터를 받기 위한 함수                          |
| packing & unpacking | 데이터의 패킹과 언패킹을 위한 함수                            |
| interactive         | 대화식 모드로 프로세스와 상호작용하기 위한 함수               |
| ELF                 | ELF 파일 정보를 조작하기 위한 클래스                          |
| context.log         | 로그 레벨을 설정하고 로그를 출력하기 위한 객체                |
| context.arch        | 사용할 아키텍처를 설정하고 현재 아키텍처를 확인하기 위한 객체 |
| shellcraft          | 쉘 코드 생성을 위한 템플릿 및 함수들을 제공하는 모듈          |
| asm                 | 어셈블리 코드를 생성하기 위한 함수                            |
