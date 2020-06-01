#include <stdio.h>
#include <stdlib.h>

int main(int argc, char* argv[]) {

  if (argc < 2 || argc > 3) {
    puts("usage: fread.exe <text.txt>\n");
    return 1;
  }

  char * file_name = argv[1];

  FILE * f;
  fopen_s(&f, file_name, "r");
  char* buff = (char *)malloc(1024);
  for (int i = 0; i < 1024; ++i) {
    buff[i] = '\0';
  }
  fread_s(buff, 1024, 1, 1024, f);
  fclose(f);

  puts(buff);

  return 0;
}
