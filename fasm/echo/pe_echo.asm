
format PE CONSOLE

include '%FASM%\include\win32ax.inc'

.code

start:
    invoke  AllocConsole
    invoke  GetStdHandle, STD_OUTPUT_HANDLE
    mov     [output], eax
    invoke  GetStdHandle, STD_INPUT_HANDLE
    mov     [input], eax

  lop:
    invoke  ReadConsole, [input],buffer,1024,written,0
    invoke  WriteConsole, [output],buffer,[written],0,0
    jmp lop

  quit:
    invoke  FreeConsole
    invoke  ExitProcess, 0

.data

input rd 1
output rd 1

msg db 'echo',10
buffer rb 1024
written dd ?

.end start
