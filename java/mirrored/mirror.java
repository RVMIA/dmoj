import java.util.*;

public class mirror {
    public static void main(String[] args) {
        System.out.println("Ready");
        String inp;
        Scanner sc = new Scanner(System.in).useDelimiter("\n");
        while (sc.hasNext()) {
            inp = sc.nextLine();
            if (inp.equals("  ")) {
                sc.close();
                break;
            } else if (inp.equals("qp") || inp.equals("pq") || inp.equals("db") || inp.equals("bd")) {
                System.out.println("Mirrored pair");
            } else {
                System.out.println("Ordinary pair");
            }
        }
        sc.close();
    }
}
