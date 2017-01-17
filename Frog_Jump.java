/*朴素DP*/
public class Solution {
    public boolean canCross(int[] stones) {
        Map<Integer, Set<Integer>> stoneMap = new HashMap<>();
        for (int i=1;i<stones.length;i++) {
            stoneMap.put(stones[i], new HashSet<Integer>());
        }
        
        if (stones[0]+1 == stones[1]) {
            stoneMap.get(stones[1]).add(1);
        }
        
        for(int i=1;i<stones.length;i++) {
            int nowStone = stones[i];
            for(Integer k:stoneMap.get(nowStone)) {
                if (k != 1 && stoneMap.containsKey(nowStone + k - 1)) {
                    stoneMap.get(nowStone + k - 1).add(k - 1);
                }
                if(stoneMap.containsKey(nowStone + k)) {
                    stoneMap.get(nowStone + k).add(k);
                }
                if(stoneMap.containsKey(nowStone + k + 1)) {
                    stoneMap.get(nowStone + k + 1).add(k + 1);
                }
            }
        } 
        return stoneMap.get(stones[stones.length - 1]).size() >= 1;
    }
}

public class Main {
	public static void main(String args[]) {
		Solution s = new Solution();
		int[] stones = {0,1,2,3,4,8,9,11};
		System.out.println(s.canCross(stones));
	}
}
