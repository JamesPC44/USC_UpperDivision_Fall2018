import java.util.*;

public class LightsCond3 {

  public static class Pnt implements Comparable<Pnt> {
    int x, y;

    public Pnt(int x, int y) {
      this.x = x + y;
      this.y = y - x;
    }

    public int compareTo(Pnt arg0) {
      return arg0.x - this.x;
    }
  }

  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int targm = in.nextInt();
    int start = in.nextInt();
    ArrayList<Pnt> objs = new ArrayList<Pnt>();
    for (int i = 0; i < start; i++) {
      objs.add(new Pnt(in.nextInt(), in.nextInt()));
    }
    in.close();

    Collections.sort(objs);
    Pnt[] arr = new Pnt[start];
    int minh = Integer.MIN_VALUE;
    int max = Integer.MIN_VALUE;
    for (Pnt p : objs) {
      if (p.y > max) {
        start--;
        arr[start] = p;
        max = p.y;
        minh = Math.max(minh, p.x + p.y);
      }
    }

    int res = minh;
    if (!core(arr, start, targm, minh)) {
      int maxh = arr[start].y + arr[arr.length - 1].x;
      for (int i = 0; i < targm && start < arr.length; i++) {
        // find index of first element with which the start point can be paired
        int nextstart = start;
        int high = arr.length;
        while (nextstart != high) {
          int mid = (nextstart + high) / 2;
          int h = arr[start].y + arr[mid].x;
          if (h > minh && (h >= maxh || core(arr, start, targm - i, h))) {
            high = mid;
          } else {
            nextstart = mid + 1;
          }
        }
        maxh = Math.min(maxh, arr[start].y + arr[nextstart].x);
        minh = Math.max(minh, arr[start].y + arr[nextstart - 1].x);
        start = nextstart;
      }
      res = maxh;
    }

    System.out.print(res / 2);
    if (res % 2 == 0) {
      System.out.println(".0");
    } else {
      System.out.println(".5");
    }
  }

  public static boolean core(Pnt[] list, int start, int m, int h) {
    // give true if <= m, false if > m
    for (int i = 0; i < m && start < list.length; i++) {
      int y = list[start].y;
      int high = list.length;
      while (start != high) {
        int mid = (start + high) / 2;
        if (list[mid].x <= h - y) {
          start = mid + 1;
        } else {
          high = mid;
        }
      }
    }
    return start == list.length;
  }
}
