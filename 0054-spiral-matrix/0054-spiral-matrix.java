 class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        int n = matrix.length;
        int m = matrix[0].length;
        List<Integer> result = new ArrayList<>();
        return spiralMatrix(result, matrix, 0, 0, n, m);
    }

    static List<Integer> spiralMatrix(List<Integer> arrayList, int[][] matrix, int startRow, int startCol, int endRow, int endCol) {
        if (endCol <= startCol || endRow <= startRow) {
            return arrayList;
        }

        //the single row or column condition is making duplicates
        //so instead, check for the condition in the reverse traversing
        //i.e, form right to left(single col) and from bottom to top(single row)

        // Traverse top row from left to right
        for (int j = startCol; j < endCol; j++) {
            arrayList.add(matrix[startRow][j]);
        }

        // Traverse rightmost column from top to bottom
        for (int i = startRow + 1; i < endRow; i++) {
            arrayList.add(matrix[i][endCol - 1]);
        }

        // Traverse bottom row from right to left (only if there's more than 1 row)
        if (endRow - startRow > 1) {
            for (int j = endCol - 2; j >= startCol; j--) {
                arrayList.add(matrix[endRow - 1][j]);
            }
        }

        // Traverse leftmost column from bottom to top (only if there's more than 1 column)
        if (endCol - startCol > 1) {
            for (int i = endRow - 2; i > startRow; i--) {
                arrayList.add(matrix[i][startCol]);
            }
        }

        // Recursive call for the inner matrix
        return spiralMatrix(arrayList, matrix, startRow + 1, startCol + 1, endRow - 1, endCol - 1);
    }
}