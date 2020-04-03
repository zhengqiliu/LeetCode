class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] <= 8:
            digits[-1] += 1
            return digits
        digits[-1] = 0
        for i in range(len(digits) - 2, -1, -1):
            if digits[i] <= 8:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
        
        
        return [1] + digits
