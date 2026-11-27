class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Initialize dp array with a value larger than any possible answer
        # (amount + 1 is a safe upper bound since the smallest coin is at least 1)
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        
        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    # The minimum coins for amount 'i' is the minimum of:
                    # 1. The current best for 'i'
                    # 2. 1 + the minimum coins for the remaining amount (i - coin)
                    dp[i] = min(dp[i], dp[i - coin] + 1)
                    
        # If dp[amount] is still amount + 1, it means the amount cannot be formed
        return dp[amount] if dp[amount] != amount + 1 else -1