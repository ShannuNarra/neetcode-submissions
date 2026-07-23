
class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashSet<Integer> arr=new HashSet<Integer>();
        for(int i=0;i<nums.length;i++){
            // for(int j=i+1;j<nums.length;j++){
            //     if(nums[i]==nums[j]){
            //         return true;
            //     }
            // }
            if(arr.contains(nums[i])){
                return true;
            }
            arr.add(nums[i]);
        }
        return false;
    }
}