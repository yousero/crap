#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

int randint(unsigned int to=1) {
  return ((float)rand() / RAND_MAX) * (to + 1);
}

int main(int argc, char* argv[]) {
  int seed = time(NULL);

  if (argc > 1) {
    if (strcmp(argv[1], "--help") || strcmp(argv[1], "-h")) {
      puts("usage: randint.exe [seed]\n");
      return 0;
    }

    seed = atoi(argv[1]);
  }

  srand(seed);

  printf("%d %d %d \n", randint(2), randint(2), randint(2));
  printf("%d %d %d \n", randint(2), randint(2), randint(2));
  printf("%d %d %d \n", randint(2), randint(2), randint(2));

  return 0;
}
