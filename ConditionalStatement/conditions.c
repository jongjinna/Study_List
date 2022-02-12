#include <time.h>
#include <stdlib.h>
#include <stdio.h>

int main(void) {
  // 버스 가정, 학생 / 일반인 구분 (20세 기준)
  // int age = 25;
  // if (age >= 20) {
  //   printf("일반인 입니다.\n");
  // }
  // else {
  //   printf("학생입니다.\n");
  // }

  // 초등학생 (8~13) / 중학생 (14~16) / 고등학생 (17~19)
  // int age = 25;
  // if (age >= 8 && age <= 13) {
  //   printf("초등학생 입니다.\n");
  // }
  // else if (age >= 14 && age <= 16) {
  //   printf("중학생 입니다.\n");
  // }
  // else if (age >= 17 && age <= 19) {
  //   printf("고등학생 입니다.\n");
  // }
  // else {
  //   printf("학생이 아닙니다.\n");
  // }

  // break / continue
  // for (int i = 1; i <= 30; i++) {
  //   if (i >= 6) {
  //     printf("나머지 학생은 집에 가세요.\n");
  //     break;
  //   }
  //   printf("%d번 학생은 발표 준비를 하세요.\n", i);
  // }

  // for (int i = 1; i <= 30; i++) {
  //   if (i >= 6 && i <= 10) {
  //     if (i == 7) {
  //       printf("%d번 학생은 결석입니다.\n", i);
  //       continue;
  //     }
  //     printf("%d번 학생은 발표 준비 하세요.\n", i);
  //   }
  // }

  // and(&&) & or(||)
  // int a = 10;
  // int b = 11;
  // int c = 12;
  // int d = 13;
  // if (a == b && c == d) {
  //   printf("a == b && c == d\n");
  // }
  // else
  // {
  //   printf("a != b || c != d\n");
  // }
  
  // 가위 0 / 바위 1 / 보 2
  // srand(time(NULL));
  // int i = rand() % 3;
  // if (i == 0) {
  //   printf("가위\n");
  // }
  // else if (i == 1) {
  //   printf("바위\n");
  // }
  // else {
  //   printf("보\n");
  // }

  // srand(time(NULL));
  // int i = rand() % 3;
  // switch (i)
  // {
  // case 0: printf("가위\n"); break;
  // case 1: printf("바위\n"); break;
  // case 2: printf("보\n"); break;
  // default: printf("몰라요\n");
  // }

  // // 초등학생 (8~13) / 중학생 (14~16) / 고등학생 (17~19)
  // int age = 15;
  // switch(age) {
  //   case 8:
  //   case 9:
  //   case 10:
  //   case 11:
  //   case 12:
  //   case 13: printf("초등학생 입니다.\n"); break;
  //   case 14:
  //   case 15:
  //   case 16: printf("중학생 입니다.\n"); break;
  //   case 17:
  //   case 18:
  //   case 19: printf("고등학생 입니다.\n"); break;
  //   default: printf("학생이 아닙니다.\n");
  // }

  // UP & Down
  srand(time(NULL));
  int num = rand() % 100 + 1;
  printf("숫자 : %d\n", num);
  int answer = 0;
  int chance = 5;
  while (1) {
    printf("남은 기회 %d번 \n", chance--);
    printf("숫자를 맞춰보세요 (1~100) : ");
    scanf("%d", &answer);
    if (answer == num) {
      printf("정답입니다.\n");
      break;
    }
    else if (answer > num) {
      printf("숫자가 너무 큽니다.\n");
    }
    else {
      printf("숫자가 너무 작습니다.\n");
    }
    if (chance == 0) {
      printf("기회가 없습니다.\n");
      break;    
    }
  }

  return 0;
}
