class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        k = k1 + k2
        n = len(nums1)
        
        # Calculate absolute differences
        diffs = [abs(nums1[i] - nums2[i]) for i in range(n)]
        max_diff = max(diffs)
        
        if max_diff == 0:
            return 0
        
        # Frequency array for differences
        freq = [0] * (max_diff + 1)
        for d in diffs:
            freq[d] += 1
            
        # Greedily reduce largest differences
        for d in range(max_diff, 0, -1):
            if freq[d] == 0:
                continue
            
            if k >= freq[d]:
                k -= freq[d]
                freq[d - 1] += freq[d]
                freq[d] = 0
            else:
                freq[d] -= k
                freq[d - 1] += k
                k = 0
                break
                
        # Sum of squared differences
        return sum(f * (d ** 2) for d, f in enumerate(freq) if f > 0)