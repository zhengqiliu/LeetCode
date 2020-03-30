class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        res = []
        while nums1 and nums2:
            if nums1[0] <= nums2[0]:
                res.append(nums1[0])
                nums1 = nums1[1:]
            else:
                res.append(nums2[0])
                nums2 = nums2[1:]
        
        res += nums1 + nums2
        n = len(res)
        if n % 2 == 0:
            return (res[n//2] + res[n//2 - 1]) / 2.0
        return res[n//2]
