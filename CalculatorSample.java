class Calculator {
  int result = 0;

  int add(int a) {
    result += a;
    return result;
  }
  int subtract(int a) {
    result -= a;
    return result;
  }
  int multiply(int a) {
    result *= a;
    return result;
  }
  int divide(int a) {
    result /= a;
    return result;
  }
}

public class CalculatorSample {
  public static void main(String[] args) {
    Calculator cal1 = new Calculator();
    System.out.println(cal1.add(5));
    System.out.println(cal1.subtract(3));
    System.out.println(cal1.multiply(5));
    System.out.println(cal1.divide(5));
    System.out.println(cal1.result);
  }
}
