class Solution {
    public int[] twoSum(int[] nums, int target) {
        //Brute-Force
        // int[] result=new int[2];
        // for(int i=0;i<nums.length;i++){
        //     for(int j=i+1;j<nums.length;j++){
        //         if(nums[i]+nums[j]==target){
        //             result[0]=i;
        //             result[1]=j;
        //         }
        //     }
        // }
        // return result;
        HashMap<Integer,Integer> prevMap=new HashMap<>();
        for(int i=0;i<nums.length;i++){
            int num=nums[i];
            int diff=target-num;
            if(prevMap.containsKey(diff)){
                return new int[] { prevMap.get(diff), i };
            }
            prevMap.put(num,i);
        }
        return new int[]{};
    }
}
