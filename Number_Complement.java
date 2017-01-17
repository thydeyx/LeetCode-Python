/*
   1、第一步的作用是把最高位1右移移位，并与原数据按位取或。那么这就使得最高位和它的下一位是连续两个1。
   2、第二步的作用是把刚刚移位得到连续两个1继续右移两位并与原数据按位取或。那么这就使得最高两位和它的下两个连续位组成四个连续的1。
   3、 以此类推，最终得到的i是从开始的最高位到结束全是1。并减去i不带符号的右移一位，即可得到一个int数据的最高位的值。
   4、上述情况是针对于i不为零和负数的情况，如果i为零，那么得到的结果始终为零。如果i位负数，那么得到的结果始终是-2147483648。即等于Integer.MIN_VALUE。（原因在于负数的最高位始终为1，即是负数的符号位）
   publicstaticinthighestOneBit(int i) {  
        // HD, Figure 3-1  
		i |= (i >>  1);  
		i |= (i >>  2);  
		i |= (i >>  4);  
		i |= (i >>  8);  
		i |= (i >> 16);  
		return i - (i >>> 1);  
	}  
*/

public class Solution {
    public int findComplement(int num) {
        return ~num & ((Integer.highestOneBit(num) << 1) - 1);
    }
}
