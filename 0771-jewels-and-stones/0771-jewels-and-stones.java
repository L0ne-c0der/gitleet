class Solution {
    public int numJewelsInStones(String jewels, String stones) {
        HashMap<Character, Integer> map = new HashMap<Character, Integer>();
        for(int i=0; i<jewels.length(); i++){
            map.put(jewels.charAt(i), 0);
        } 
        for(int i=0; i<stones.length(); i++){
            char letter = stones.charAt(i);
            if(map.containsKey(letter)){
                int value = map.get(letter);
                map.replace(letter,value+1);
            }
        }
        int sum = 0;
        for(int i=0; i<jewels.length(); i++){
            char character = jewels.charAt(i);
            int val = map.get(character);
            sum += val;
        }
        return sum;
    }
}