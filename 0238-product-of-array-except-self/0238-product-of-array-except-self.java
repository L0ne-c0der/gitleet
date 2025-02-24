class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] output = new int[nums.length];

        //initializing array
        for(int i=0; i<output.length; i++){
            output[i] = 1;
        }
        int left = 1;
        for(int i=0; i<output.length; i++){
            output[i] *= left;
            left *= nums[i];           
        }

        int right = 1;
        for(int i=output.length-1; i>=0; i--){
            output[i] *= right;
            right *= nums[i];
        }

        return output;
    }
}