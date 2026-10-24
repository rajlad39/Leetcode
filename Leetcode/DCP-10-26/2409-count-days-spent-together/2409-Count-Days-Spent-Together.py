class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        def to_days(date_str: str) -> int:
            m, d = map(int, date_str.split('-'))
            total = d
            for i in range(m - 1):
                total += days_in_months[i]
            return total
        
        alice_start = to_days(arriveAlice)
        alice_end = to_days(leaveAlice)
        bob_start = to_days(arriveBob)
        bob_end = to_days(leaveBob)
        
        overlap_start = max(alice_start, bob_start)
        overlap_end = min(alice_end, bob_end)
        
        if overlap_start <= overlap_end:
            return overlap_end - overlap_start + 1
        return 0