class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_tank = 0
        current_tank = 0
        start_station = 0
        
        for i in range(len(gas)):
            # Calculate the net gas gain/loss at this station
            net_gas = gas[i] - cost[i]
            total_tank += net_gas
            current_tank += net_gas
            
            # If the tank goes negative, we can't reach the next station from our current start
            if current_tank < 0:
                # Any station between start_station and i is invalid, so we try i + 1 next
                start_station = i + 1
                current_tank = 0
                
        # If the total net gas is non-negative, a valid starting point exists
        return start_station if total_tank >= 0 else -1