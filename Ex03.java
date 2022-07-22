import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.HashMap;
import java.util.HashSet;

public class Ex03 {
  public static void num1(int koreans, int englishs, int maths) {
    int total = koreans + englishs + maths;
    int average = total / 3;
    System.out.println("평균 : " + average);  
  }
  
  public static void num2(int n) {
    int m = n % 2;
    if (m == 0) {
      System.out.println("짝수");
    } else {
      System.out.println("홀수");
    }
  }

  public static void num3(String n) {
    String y = n.substring(0, 6);
    String m = n.substring(7, 14);
    System.out.println(y);
    System.out.println(m);
  }

  public static void num4(String n) {
    char m = n.charAt(7);
    System.out.println(m);
  }

  public static void num5(String n) {
    System.out.println(n.replace(":", "#"));
  }

  public static void num6(String[] arg) {
    ArrayList<Integer> myList = new ArrayList<>(Arrays.asList(1, 3, 5, 4, 2));
    myList.sort(Comparator.reverseOrder()); // [5, 4, 3, 2, 1] 출력
    System.out.println(myList); // 1 출력
  }

  public static void num7(String[] arg) {
    ArrayList<String> myList = new ArrayList<>(Arrays.asList("Life", "is", "too", "short"));
    String result = String.join(" ", myList);
    System.out.println(result); // "Life is too short" 출력
  }

  public static void num8(String[] arg) {
    HashMap<String, Integer> grade = new HashMap<>();
    grade.put("A", 90);
    grade.put("B", 80);
    grade.put("C", 70);
    int result = grade.remove("B");
    System.out.println(result); // 80 출력
    System.out.println(grade); // null 출력
  }

  public static void num9(String[] arg) {
    ArrayList<Integer> numbers = new ArrayList<>(Arrays.asList(1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5));
    HashSet<Integer> n = new HashSet<>(numbers);
    ArrayList<Integer> n2 = new ArrayList<>(n);
    System.out.println(n2);  // [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5] 출력
  }
  
  public static void num10(String[] arg) {
    printCoffeePrice(CoffeeType.Americano);  // "가격은 3000원 입니다." 출력
    printCoffeePrice(CoffeeType.IceAmericano);
  }
  
  enum CoffeeType {
    Americano,
    IceAmericano,
    CafeLatte,
  }
  static void printCoffeePrice(CoffeeType type) {
    HashMap<CoffeeType, Integer> priceMap = new HashMap<>();
    priceMap.put(CoffeeType.Americano, 3000);  // 1: 아메리카노
    priceMap.put(CoffeeType.IceAmericano, 4000);  // 2: 아이스 아메리카노
    priceMap.put(CoffeeType.CafeLatte, 5000);  // 3: 카페라떼
    int price = priceMap.get(type);
    System.out.println(String.format("가격은 %d원 입니다.", price));
  }
  public static void main(String[] args) {
    num1(80, 75, 55);
    num2(13);
    num3("881120-1068234");
    num4("881120-1068234");
    num5("a:b:c:d");
    num6(args);
    num7(args);
    num8(args);
    num9(args);
    num10(args);
  }
}
