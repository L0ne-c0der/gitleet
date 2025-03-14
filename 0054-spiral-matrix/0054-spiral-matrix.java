class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        int n = matrix.length;
 	    int m = matrix[0].length;
	    List<Integer> result = new ArrayList<Integer>();
	    List<Integer> finalResult = spiralMatrix(result, matrix, 0, 0, n, m);
	    return finalResult;
    }

    static List<Integer> spiralMatrix(List<Integer> arrayList,int[][] matrix,int startRow,int startCol,int endRow,int endCol){
        if(endCol<startCol || endRow<startRow){
            return arrayList;
        }
        if(endCol-startCol==1 || endRow - startRow == 1){
            for(int i=startRow; i<endRow; i++){
                for(int j=startCol; j<endCol; j++){
                    arrayList.add(matrix[i][j]);
                }
            }
            return arrayList;
        }
        int i=startRow;
        int j=startCol;
        for(j=startCol; j<endCol-1; j++){
            arrayList.add(matrix[i][j]);
        }
        for(i=startRow; i<endRow-1; i++){
            arrayList.add(matrix[i][j]);
        }

        for(;j>startCol;j--){ //changed to go till startCol not startCol+1
            arrayList.add(matrix[i][j]);
        }
        
        for(; i>startRow; i--){ //it changed to startRow instead of startCol
            arrayList.add(matrix[i][j]);
        }
        System.out.println((startRow+1)+" "+(endRow-1));
        System.out.println((startCol+1)+" "+(endCol-1));
        return spiralMatrix(arrayList, matrix, startRow+1, startCol+1, endRow-1, endCol-1); //issue here, the start row is becoming greater than start col
    }
}