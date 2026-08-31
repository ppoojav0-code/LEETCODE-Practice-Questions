class Solution:
    def subarraySum(self, nums, k):

        d = {0: 1}
        prefix = 0
        count = 0

        for num in nums:
            prefix += num

            if prefix - k in d:
                count += d[prefix - k]

            d[prefix] = d.get(prefix, 0) + 1

        return count        