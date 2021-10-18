; Hello World em Assembly x86
; compile com o comando a baixo (precisa do build essentials no linux)
; voce pode instalar com apt-get install build-essential
; ld -m elf_i386 -s -o hello hello.o
section .text align=0

global _start

mensagem db 'Hello world', 0x0a ; espaço de memoria destinado a conter nossa mensagem

len equ $ - mensagem ;tamanho da mensagem

_start:
    mov eax, 4 ;SYS_write 
    mov ebx, 1 ;file descriptor (1=stdout)
    mov ecx, mensagem ;string pointer.
    mov edx, len ; buffer size
    int 0x80

    mov eax, 1
    int 0x8