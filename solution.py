class Solution(object):
    def getPermutation(self, n, k):
        from math import factorial

        numbers = list(range(1, n + 1))
        k -= 1  # Convert to 0-indexed
        result = ""

        for i in range(n, 0, -1):
            f = factorial(i - 1)
            index = k // f
            result += str(numbers.pop(index))
            k %= f

        return result
