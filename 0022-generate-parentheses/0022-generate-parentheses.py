class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtracking(openP, closeP, s):
            if openP == closeP and openP + closeP == n*2:
                res.append(s)
                return
            if openP < n:
                backtracking(openP + 1, closeP, s + "(")
            if closeP < openP:
                backtracking(openP, closeP + 1, s+ ")")
         
        backtracking(0, 0, "")

        return res