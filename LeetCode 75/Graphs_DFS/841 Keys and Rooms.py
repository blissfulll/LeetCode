class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        def dfsRec(node, visited_nodes, stack):

            stack.pop()

            if node not in visited_nodes:
                visited_nodes.append(node)
            
                for key in rooms[node]:
                    stack.append(key)

            if stack:
                dfsRec(stack[-1], visited_nodes, stack)

        visited_nodes = []
        dfsRec(0, visited_nodes, [0])

        if len(visited_nodes) == len(rooms):
            return True
        
        return False
        
