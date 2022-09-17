package JumpToJavaWithDuoen;

public class WithDuoen {
  public static void main(String[] args) {
    int aaa = countCharacter("say what!?", 'a');
    System.out.println(aaa);
  }
  
  public static int countCharacter(String str, char letter) {
    int cnt = 0;
    for (int i=0; i < str.length(); i++) {
      if (str.charAt(i) == letter) {
        cnt ++;
      }
    }
    return cnt;
  }
}
