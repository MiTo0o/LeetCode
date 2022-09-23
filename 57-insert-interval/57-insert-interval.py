class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        ns, ne = newInterval
        min_start = min(float('inf'), ns)
        max_end = max(float('-inf'), ne)
        for i in intervals:
            cs, ce = i
            if (ns >= cs and ns <= ce or ne <= ce and ne >= cs) or (cs >= ns and cs <= ne or ce <= ne and ce >= ns):
                min_start = min(min_start, cs)
                max_end = max(max_end, ce)
            else:
                res.append(i)
        res.append([min_start, max_end])
        res.sort(key=lambda x: x[0])
        return res
        
        
                
        
            