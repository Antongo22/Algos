class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a list of integers
    def intersect(self, A, B):
        res = []
        
        pointerA = 0
        pointerB = 0
        
        
        while pointerA < len(A) and pointerB < len(B):
            if A[pointerA] == B[pointerB]:
                res.append(A[pointerA])
                pointerA += 1
                pointerB += 1
            elif A[pointerA] < B[pointerB]:
                pointerA += 1
            else:
                pointerB += 1
                
        return res       