#include <stdio.h>

int main(void) {
  // printf("Hello world\n");
  // printf("Hello world\n");
  // printf("Hello world\n");
  // printf("Hello world\n");
  
  // int a = 10;
  // printf("a 는 %d\n", a);
  // a++;
  // printf("a 는 %d\n", a);
  
  // int b = 20;
  // printf("b 는 %d\n", ++b); // ++한 뒤 b
  // printf("b 는 %d\n", b++); // b한 뒤 ++
  // printf("b 는 %d\n", b);

  // int i = 1;
  // printf("Hello world %d\n", i++);
  // printf("Hello world %d\n", i++);
  // printf("Hello world %d\n", i++);
  // printf("Hello world %d\n", i++);
  // printf("Hello world %d\n", i++);
  // printf("Hello world %d\n", i++);
  // printf("Hello world %d\n", i++);
  // printf("Hello world %d\n", i++);

  // 반복문 (for, while, do while)
  // for (int i = 1; i <= 10; i++) {
  //   printf("Hello world %d\n", i);
  // }

  // int i = 1;
  // while (i <= 10) {
  //   printf("Hello world %d\n", i++);
  // }
  
  // int i = 1;
  // do {
  //   printf("Hello world %d\n", i++);
  // } while (i <= 10);

  // 2중 반복문
  // for (int i = 1; i <= 3; i++) {
  //   printf("첫번째 반복문 : %d\n", i);
  //   for (int j = 1; j <= 5; j++) {
  //     printf("  두번째 반복문 : %d\n", j);
  //   }
  // }

  // 구구단
  // for (int i = 2; i <= 9; i++) {
  //   printf("%d단 계산\n", i);
  //   for(int j = 1; j <= 9; j++) {
  //     printf("  %d x %d = %d \n", i, j, i*j);
  //   }
  // }

  // for (int i = 0; i <= 5; i++) {
  //   for (int j = 0; j <= i; j++) {
  //     printf("*");
  //   }
  //   printf("\n");
  // }

  // for (int i = 0; i <= 5; i++) {
  //   for (int j = 1; j <= 5-i; j++) {
  //     printf(" ");
  //   }
  //   for (int k = 0; k <= i; k++) {
  //     printf("*");
  //   }
  //   printf("\n");
  // } 

  // 피라미드를 쌓아라 프로젝트
  int floor;
  printf("몇 층으로 쌓을 것인가? : ");
  scanf("%d", &floor);
  for (int i = 1; i <= floor; i++) {
    for (int j = 1; j<= floor-i; j++){
      printf(" ");
    }
    for (int k = 1; k<=2*i-1; k++) {
      printf("*");
    }
    printf("\n");
  }

  return 0;
}