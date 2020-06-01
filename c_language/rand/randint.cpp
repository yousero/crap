#include <stdio.h>
#include <stdlib.h>

int randint(unsigned int to=1) {
  return ((float)rand() / RAND_MAX) * (to + 1);
}

int main(int argc, char* argv[]) {
  srand(10000);

  printf("%d %d %d \n", randint(2), randint(2), randint(2));
  printf("%d %d %d \n", randint(2), randint(2), randint(2));
  printf("%d %d %d \n", randint(2), randint(2), randint(2));

  return 0;
}
