import java.util.PriorityQueue;
import java.util.Scanner;

/*
    URI Online Judge: task 2531 - Hotel Rewards

    solution by alexandre corlet
 */
public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt(), k = in.nextInt();

        PriorityQueue<Integer> pq = new PriorityQueue<>();

        int cost = 0;
        for (int i = 1; i <= n; i++) {
            int p = in.nextInt();
            cost += p;
            if (i % (k + 1) == 0) {
                pq.add(p);
                cost -= p;
            } else if (k + 1 < i && pq.element() < p) {
                cost += pq.element();
                cost -= p;
                pq.poll();
                pq.add(p);
            }
        }

        System.out.println(cost);
    }
}
