//      Author : TangHanYi
//      E-mail : thydeyx@163.com
// Create Date : 16-10-26 20:06:39
//   File Name : Search_in_Rotated_Sorted_Array_II.cpp
//        Desc :


#include<iostream>
#include<vector>
using namespace std;

class Solution {
public:
    int search(vector<int>& nums, int target) {
        int l=0,r=nums.size()-1;
        while(l<=r)
        {
            int mid=(r+l)/2;
            if(nums[mid]==target)return true;
            if(nums[l] < nums[mid])
            {
                if(nums[mid]>target && target>=nums[l])r=mid-1;
                else l=mid+1;
            }else if(nums[l] > nums[mid])
            {
                if(target>nums[mid] && target <= nums[r])l=mid+1;
                else r=mid-1;
            }else l++;
        }
        return false;
    }
};

int main()
{
	Solution s;
	int iarray[] = {1,2,3,4,5,6,7,8,9,0};
	int target = 20;
	vector<int> nums(iarray,iarray + sizeof(iarray)/sizeof(int));
	cout << s.search(nums, target) << endl;
	return 0;
}
