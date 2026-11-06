class Solution:
    def numTrees(self, n: int) -> int:
        # dp[i] will store the number of structurally unique BSTs with 'i' nodes
        dp = [0] * (n + 1)
        
        # Base cases: 
        # 0 nodes -> 1 tree (empty tree)
        # 1 node  -> 1 tree
        dp[0] = 1
        dp[1] = 1
        
        # Fill the DP array from 2 up to n
        for nodes in range(2, n + 1):
            total_trees = 0
            # Try every possible root from 1 to 'nodes'
            for root in range(1, nodes + 1):
                left_subtrees = dp[root - 1]
                right_subtrees = dp[nodes - root]
                total_trees += left_subtrees * right_subtrees
                
            dp[nodes] = total_trees
            
        return dp[n]