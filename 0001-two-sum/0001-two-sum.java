class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> numMap= new HashMap<Integer, Integer>();
        int n = nums.length;
        for(int i=0; i<n; i++){
            int comp = target - nums[i];
            if(numMap.containsKey(comp)){
                return new int[]{i, numMap.get(comp)};
            }
            else{
                numMap.put(nums[i],i);
            }
        }
        return new int[]{};
    }
}