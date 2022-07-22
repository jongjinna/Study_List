public class Ex04 {
  public static void num1(String[] args) {
    System.out.println("everywhere");
  }

  public static void num2(String[] args) {
    int i = 1;
    int n = 0;
    while (i < 1000) {
      if (i % 3 == 0) {
        n += i;
      }
      i++;
    }
    System.out.println(n);
  }

  public static void num3(String[] args) {
    for (int j = 1; j <= 5; j++) {
      for (int i = 0; i < j; i++) {
        System.out.print("*");
      }
      System.out.println("");
    }
  }

  public static void num4(String[] args) {
    for (int i = 1; i<=100; i++) {
      System.out.println(i);
    }
  }

  public static void num5(String[] args) {
    int[] marks = {70, 60, 55, 75, 95, 90, 80, 80, 85, 100};
    int sum = 0;
    for (int n: marks) {
      sum += n;
    }
    System.out.println(sum/marks.length);
  }

  public static void main(String[] args) {
    // num1(args);
    // num2(args);
    // num3(args);
    // num4(args);
    num5(args);
  }  
}
