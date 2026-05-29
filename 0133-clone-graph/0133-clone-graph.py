class Solution(object):
    def cloneGraph(self, node):
        if not node:
            return None
            
        cloned_map = {node: Node(node.val)}
        queue = [node]
        
        for current in queue:
            for neighbor in current.neighbors:
                if neighbor not in cloned_map:
                    cloned_map[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                cloned_map[current].neighbors.append(cloned_map[neighbor])
                
        return cloned_map[node]
