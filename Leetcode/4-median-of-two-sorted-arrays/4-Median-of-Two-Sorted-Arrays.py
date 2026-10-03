class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # Ensure nums1 is the smaller array to minimize binary search range
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        low, high = 0, m
        half_len = (m + n + 1) // 2

        while low <= high:
            i = (low + high) // 2
            j = half_len - i

            # Handle edge boundaries using infinity
            Aleft = nums1[i - 1] if i > 0 else float('-inf')
            Aright = nums1[i] if i < m else float('inf')
            Bleft = nums2[j - 1] if j > 0 else float('-inf')
            Bright = nums2[j] if j < n else float('inf')

            # Check if partition is correct
            if Aleft <= Bright and Bleft <= Aright:
                # Odd total elements
                if (m + n) % 2 == 1:
                    return float(max(Aleft, Bleft))
                # Even total elements
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2.0
            
            elif Aleft > Bright:
                high = i - 1
            else:
                low = i + 1

        return 0.0