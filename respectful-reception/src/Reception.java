import java.util.*;

public class Reception {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int objcount = in.nextInt();
    int[] arr = new int[1 << 20];
    for (int n = 0; n < objcount; n++) {
      int x = in.nextInt();
      int sum = 0;
      for (int i = x; i > 0; i -= i & -i) {
        sum += arr[i]; // sum together node values
      }
      System.out.println(sum);
      for (int i = x; i < arr.length; i += i & -i) {
        arr[i]++; // update node values
      }
    }
    in.close();
  }
}
