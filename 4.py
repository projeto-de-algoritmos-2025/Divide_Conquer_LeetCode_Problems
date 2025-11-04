class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        m, n = len(nums1), len(nums2)
        low, high = 0, m
        
        k = (m + n + 1) // 2

        while low <= high:
            cut1 = low + (high - low) // 2
            cut2 = k - cut1
            
            L1 = nums1[cut1 - 1] if cut1 > 0 else float('-inf')
            R1 = nums1[cut1] if cut1 < m else float('inf')
            
            L2 = nums2[cut2 - 1] if cut2 > 0 else float('-inf')
            R2 = nums2[cut2] if cut2 < n else float('inf')

            if L1 <= R2 and L2 <= R1:
                if (m + n) % 2 == 1:
                    return float(max(L1, L2))
                else:
                    max_of_left = max(L1, L2)
                    min_of_right = min(R1, R2)
                    return (max_of_left + min_of_right) / 2.0
            
            elif L1 > R2:
                high = cut1 - 1
            else: 
                low = cut1 + 1
        return 0.0