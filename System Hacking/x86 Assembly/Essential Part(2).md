push val: val을 스택 Top에 push

    rsp -= 8
    [rsp] = val

pop reg: 스택 Top의 값을 꺼내 reg에 대입

    rsp += 8
    reg = [rsp-8]

call addr: addr에 위치한 프로시져 호출

    push return_address
    jmp addr

leave: 스택 프레임 정리

    mov rsp, rbp
    pop rbp

ret: return address로 반환

    pop rip

syscall :

    요청 : rax
    인자 순서 : rdi -> rsi -> rdx -> rcx -> r8 -> r9 -> stack

| Syscall  | Code | Arguments                                                               |
| -------- | ---- | ----------------------------------------------------------------------- |
| read     | 0x00 | unsigned int fd, char \*buf, size_t count                               |
| write    | 0x01 | unsigned int fd, const char \*buf, size_t count                         |
| open     | 0x02 | const char \*filename, int flags, umode_t mode                          |
| close    | 0x03 | unsigned int fd                                                         |
| mprotect | 0x0a | unsigned long start, size_t len, unsigned long prot                     |
| connect  | 0x2a | int sockfd, struct sockaddr \*addr, int addrlen                         |
| execve   | 0x3b | const char *filename, const char *const *argv, const char *const \*envp |
