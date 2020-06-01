#include <stdio.h>
#include <stdlib.h>

int main() {
  int a = 123;
  int b = 321;

  int *c = (int *)calloc(sizeof(int), 1);
  *c = b - a;

  printf("%d %d %d\n", a, b, *c);

  return 0;
}
