class Solution {
    public int reverse(int x) {
        int temp=0;
        int last;
        while(x!=0){
            last = x%10;
            if(temp > Integer.MAX_VALUE/10 || temp < Integer.MIN_VALUE/10 || (temp == Integer.MIN_VALUE && last<-8)){
                return 0;
            }
            temp = temp*10 + last;
            x = x/10;
        }
        return temp;
    }
}