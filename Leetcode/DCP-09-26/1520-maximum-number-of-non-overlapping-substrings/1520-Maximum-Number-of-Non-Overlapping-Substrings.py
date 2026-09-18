class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        first = {}
        last = {}
        for i, ch in enumerate(s):
            if ch not in first:
                first[ch] = i
            last[ch] = i

        valid_intervals = []

        for ch in set(s):
            l = first[ch]
            r = last[ch]
            is_valid = True
            
            i = l
            while i <= r:
                if first[s[i]] < l:
                    is_valid = False
                    break
                r = max(r, last[s[i]])
                i += 1

            if is_valid:
                valid_intervals.append((r, l))

        valid_intervals.sort()

        res = []
        prev_end = -1

        for r, l in valid_intervals:
            if l > prev_end:
                res.append(s[l : r + 1])
                prev_end = r

        return res