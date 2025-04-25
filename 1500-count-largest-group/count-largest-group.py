class Solution(object):
    def countLargestGroup(self, n):
        from collections import defaultdict

        digit_sum_groups = defaultdict(int)

        for i in range(1, n + 1):
            digit_sum = sum(int(d) for d in str(i))
            digit_sum_groups[digit_sum] += 1

        max_size = max(digit_sum_groups.values())
        return list(digit_sum_groups.values()).count(max_size)
