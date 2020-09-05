format ELF executable 3

entry start

start:
  lop:  
    mov eax, 3
    mov ebx, 0
    mov ecx, str0
    mov edx, 0x100
    int 0x80
    
    jz exit
  
    mov edx, [eax]
    mov eax, 4
    mov ebx, 1
    mov ecx, str0    
    int 0x80

    jmp lop

  exit:
    mov eax, 1
    xor ebx, ebx
    int 0x80

str0 rb 0x100
