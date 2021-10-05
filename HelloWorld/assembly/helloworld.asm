;; Programa Hello World
section .text
global _start

_start:
        mov     edx,len                             ;comprimento da mensagem
        mov     ecx,msg                             ;mensagem a ser escrita
        mov     ebx,1                               ;descritor de arquivo (stdout)
        mov     eax,4                               ;número da system call
; (sys_write)
        int     0x80                                ;call kernel

        mov     eax,1                               ;numero da syscall
; (sys_exit)
        int     0x80                                ;call kernel

section     .data
        msg     db  'Hello, world!',0xa                 ;nossa string lindona
        len     equ $ - msg                             ;comprimento da lindona
