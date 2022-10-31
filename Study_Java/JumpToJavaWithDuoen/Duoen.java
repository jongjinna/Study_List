package JumpToJavaWithDuoen;
import java.util.ArrayList;

public class Duoen {
  public static void main(String[] args) {
   helloWorld(); 
   duoenArrayList(args);
  }

  public static void helloWorld() {
    System.out.println("Hello World!");
  }
  
  public static void duoenArrayList(String[] args) { 
    ArrayList<String> cars = new ArrayList<String>();
    cars.add(0, "Volvo");
    cars.add(1, "Volvo");
    cars.add(2, "Ford");
    cars.add(3, "Mazda");
    System.out.println(cars.remove("Volvo"));
    // cars.remove("Volvo");
    // System.out.println(cars);
  } 
}
