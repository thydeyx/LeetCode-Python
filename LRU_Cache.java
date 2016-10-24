import java.io.PrintStream;
import java.util.LinkedHashMap;
import java.util.Map;

/**
 * Created by Administrator on 2016/10/24 0024.
 */
//使用LinkedHashMap，其中的哈希函数和HashMap中的一样,但保存了先后顺序.
public class LRU_Cache {

    private Map<Integer, Integer> map;
    public LRU_Cache(int capacity) {
        map = new MyLinkedHashMap<>(capacity);
    }

    public int get(int key) {
        return this.map.getOrDefault(key, -1);
    }

    public void set(int key, int value) {
        this.map.put(key, value);
    }

    private static class MyLinkedHashMap<K, V> extends LinkedHashMap<K,V>{
        int maximumCapacity;
        public  MyLinkedHashMap(int capacity){
            super(16, 0.75F, true);
            this.maximumCapacity = capacity;
        }

        protected boolean removeEldestEntry(Map.Entry eldest){
            return size() > this.maximumCapacity;
        }
    }

    public static void main(String args[]){
        LRU_Cache l = new LRU_Cache(1);
        PrintStream out = System.out;
        l.set(2, 1);
        out.println(l.get(2));
        l.set(3,2);
        out.println(l.get(2));
        out.println(l.get(3));
    }
}
