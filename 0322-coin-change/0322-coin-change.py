class Solution(object):
    def coinChange(self, coins, amount):
        if amount == 0:
            return 0
            
        coins = sorted(list(set(coins)), reverse=True)
        queue = [0]
        visited = {0}
        step = 0
        
        while queue:
            step += 1
            next_queue = []
            for amt in queue:
                for coin in coins:
                    next_amt = amt + coin
                    if next_amt == amount:
                        return step
                    if next_amt < amount and next_amt not in visited:
                        visited.add(next_amt)
                        next_queue.append(next_amt)
            queue = next_queue
            
        return -1
