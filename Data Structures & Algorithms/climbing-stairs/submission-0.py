class Solution:
    def climbStairs(self, n: int) -> int:
        fib = [0, 1]
        while n > 0:
            temp = fib[1]
            fib[1] = fib[0] + fib[1]
            fib[0] = temp
            n -= 1
        return fib[1]


















