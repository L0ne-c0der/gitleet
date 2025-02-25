class Solution {
    public int[][] merge(int[][] intervals) {
        if(intervals.length==1){
            return intervals;
        }
        Arrays.sort(intervals, (a, b) -> Integer.compare(a[0], b[0]));
        ArrayList<int[]> output = new ArrayList<>();
        int i=1;
        int left = intervals[0][0];
        int right = intervals[0][1];
        while(i<intervals.length){
            if(right>=intervals[i][0]){
                right = Math.max(intervals[i][1], right);
                left = Math.min(left, intervals[i][0]);
            }
            else{
                output.add(new int[]{left, right});
                left = intervals[i][0];
                right = intervals[i][1];
            }
            i++;
        }
        output.add(new int[]{left , right});
        int [][] array = output.toArray(new int[output.size()][2]);
        return array;
    }
}