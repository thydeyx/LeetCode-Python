import java.io.PrintStream;
import java.util.Arrays;
import java.util.Comparator;

/**
 * Created by Administrator on 2016/10/21 0021.
 */
public class H_Index {
    public static int hIndex(int[] citations) {
        int n = citations.length, i=0;
        Integer citation[] = new Integer[n];
        for(int a:citations){
            citation[i++] = a;
        }
        PrintStream out = System.out;
        Comparator comparator = new Comparator<Integer>() {
            @Override
            public int compare(Integer o1, Integer o2) {
                if(o1 >= o2)return -1;
                else return 1;
            }
        };
        Arrays.sort(citation, comparator);
        for(i = n - 1;i>=0;i--)
        {
            if(citation[i] >= i)break;
        }
        return citation[i];
    }

    public static void main(String args[]){
        int a[] = {3, 0, 6, 1, 5};
        PrintStream out = System.out;
        int ans = hIndex(a);
        out.println(ans);
    }
}
