public class TowersOfHanoi {
    private int totalDisks;

    public TowersOfHanoi(int d) {
        totalDisks = d;
    }
    public void solve() {
        //initial move to move disks from tower 1 to tower 3 using tower 2
        moveTower(totalDisks, 1, 3, 2);
    }
    private void moveTower(int n, int s, int e, int t) {
        if (n == 1) {
            moveOneDisk(s, e);
        }
        else {
            moveTower(n - 1, s, t, e);
            moveOneDisk(s, e);
            moveTower(n - 1, t, e, s);
        }
    }
    private void moveOneDisk(int s, int e) {
        System.out.println("Move one disk from " + s + " to " + e + ".");
    }
}
